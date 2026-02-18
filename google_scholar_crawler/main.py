from scholarly import scholarly
from scholarly._proxy_generator import MaxTriesExceededException
import jsonpickle
import json
from datetime import datetime
import os
import time

MAX_ATTEMPTS = int(os.getenv('SCHOLARLY_MAX_ATTEMPTS', '3'))
BACKOFF_SECONDS = int(os.getenv('SCHOLARLY_BACKOFF_SECONDS', '15'))

os.makedirs('results', exist_ok=True)


def fetch_author() -> dict:
    return scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])


author = None
last_error = None
for attempt in range(1, MAX_ATTEMPTS + 1):
    try:
        author = fetch_author()
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        break
    except (MaxTriesExceededException, AttributeError) as exc:
        last_error = exc
        print(f"Attempt {attempt} failed: {exc}")
        if attempt < MAX_ATTEMPTS:
            time.sleep(BACKOFF_SECONDS * attempt)

if author is None:
    print(f"Failed to fetch Google Scholar data after {MAX_ATTEMPTS} attempts. Skipping update.")
    raise SystemExit(0)

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
