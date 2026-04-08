import json
from datetime import datetime
import os
import time
from urllib.parse import urlparse, parse_qs

import requests

MAX_ATTEMPTS = int(os.getenv('SERPAPI_MAX_ATTEMPTS', '3'))
BACKOFF_SECONDS = int(os.getenv('SERPAPI_BACKOFF_SECONDS', '15'))
ARTICLES_PER_PAGE = int(os.getenv('SERPAPI_ARTICLES_PER_PAGE', '100'))
MAX_ARTICLES = int(os.getenv('SERPAPI_MAX_ARTICLES', '500'))
SERPAPI_ENDPOINT = 'https://serpapi.com/search.json'
SERPAPI_TIMEOUT_SECONDS = int(os.getenv('SERPAPI_TIMEOUT_SECONDS', '40'))

os.makedirs('results', exist_ok=True)


def extract_author_pub_id(article: dict) -> str:
    citation_id = article.get('citation_id')
    if citation_id:
        return citation_id
    link = article.get('link', '')
    if not link:
        return ''
    query = parse_qs(urlparse(link).query)
    values = query.get('citation_for_view')
    return values[0] if values else ''


def fetch_author_page(author_id: str, api_key: str, start: int) -> dict:
    params = {
        'engine': 'google_scholar_author',
        'author_id': author_id,
        'hl': 'en',
        'num': ARTICLES_PER_PAGE,
        'start': start,
        'api_key': api_key,
    }
    response = requests.get(SERPAPI_ENDPOINT, params=params, timeout=SERPAPI_TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()
    if data.get('error'):
        raise RuntimeError(f"SerpAPI error: {data['error']}")
    return data


def fetch_author_data(author_id: str, api_key: str) -> dict:
    combined = None
    collected_articles = []
    start = 0
    while start < MAX_ARTICLES:
        page = fetch_author_page(author_id, api_key, start)
        if combined is None:
            combined = page
        articles = page.get('articles', [])
        if not articles:
            break
        collected_articles.extend(articles)
        if len(articles) < ARTICLES_PER_PAGE:
            break
        start += ARTICLES_PER_PAGE
    if combined is None:
        raise RuntimeError('No response from SerpAPI.')
    combined['articles'] = collected_articles
    return combined


author_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
api_key = os.environ.get('SERPAPI_API_KEY', '').strip()
if not author_id:
    print('GOOGLE_SCHOLAR_ID is empty. Skipping update.')
    raise SystemExit(0)
if not api_key:
    print('SERPAPI_API_KEY is empty. Skipping update.')
    raise SystemExit(0)

data = None
last_error = None
for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        data = fetch_author_data(author_id, api_key)
        break
    except Exception as exc:
        last_error = exc
        print(f"Attempt {attempt} failed: {type(exc).__name__}: {exc}")
        if attempt < MAX_ATTEMPTS:
            time.sleep(BACKOFF_SECONDS * attempt)

if data is None:
    print(f"Failed to fetch Google Scholar data after {MAX_ATTEMPTS} attempts. Skipping update.")
    if last_error is not None:
        print(f"Last error: {type(last_error).__name__}: {last_error}")
    raise SystemExit(0)

author = data.get('author', {})
cited_by = (
    data.get('cited_by', {})
    .get('table', [{}])[0]
    .get('citations', {})
    .get('all', 0)
)

publications = {}
for article in data.get('articles', []):
    author_pub_id = extract_author_pub_id(article)
    if not author_pub_id:
        continue
    num_citations = article.get('cited_by', {}).get('value', 0)
    publications[author_pub_id] = {
        'author_pub_id': author_pub_id,
        'title': article.get('title', ''),
        'num_citations': num_citations,
        'pub_year': article.get('year'),
    }

result = {
    'name': author.get('name', ''),
    'updated': str(datetime.now()),
    'citedby': cited_by,
    'publications': publications,
}
print(json.dumps(result, indent=2))
with open('results/gs_data.json', 'w') as outfile:
    json.dump(result, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{result['citedby']}",
}
with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
