---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I'm currently a Postdoctoral Research Fellow at [The Institute for Experiential AI (EAI)](https://ai.northeastern.edu/) at Northeastern Unversity. I do research on computer vision and machine learning with applications for healthcare, working closely with [Dr. Agata Lapedriza](https://s3.sunai.uoc.edu/web/agata/index.html), [Dr. Sarah Ostadabbas](https://coe.northeastern.edu/people/ostadabbas-sarah/), and [Dr. Eugene Tunik](https://bouve.northeastern.edu/directory/eugene-tunik/). Prior to joining to EAI, I received my Ph.D in Computer Science from [The State University of New York at Buffalo (UB)](http://www.buffalo.edu/), working on human activity analysis with [Dr. David Doermann](https://cse.buffalo.edu/~doermann/). Before joining UB, I obtained my MS and BS degrees (both with honors) from [Huazhong University of Science and Technology (HUST)](https://english.hust.edu.cn/), advised by [Dr. Zhiguo Cao](https://scholar.google.com/citations?user=396o2BAAAAAJ&hl=en). I enjoy hiking, skiing, playing ping-pong, and exploring towns with my camera.
<!-- [Dr. Zhiguo Cao](http://faculty.hust.edu.cn/caozhiguo1/zh_CN/index.htm). I have published papers on AI conferences and journals with <a href='https://scholar.google.com/citations?user=lTUM3B0AAAAJ'><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/yjzhux/yjzhux.github.io/google-scholar-stats/gs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>. -->

**Research Interests**: Human Action/Motion Analytics, Video Understanding, Human-Centric AI for Health; Multimodal Learning, Time Series Modeling, Sequence Generation

<!-- *<font color=red>I am on the job market for positions in Fall 2023.</font>* -->
<font color=red>
For NU students: feel free to send me an email if you are interested in working with me.</font>

<!-- https://github.com/yjzhux/yjzhux.github.io/blob/google-scholar-stats/gs_data_shieldsio.json -->
<!-- raw: https://raw.githubusercontent.com/yjzhux/yjzhux.github.io/google-scholar-stats/gs_data_shieldsio.json -->
<!-- raw_encode: https%3A%2F%2Fraw.githubusercontent.com%2Fyjzhux%2Fyjzhux.github.io%2Fgoogle-scholar-stats%2Fgs_data_shieldsio.json -->


# 🔥 News

<div style="width: 100%; height: 150px; overflow-y: auto; padding: 10px;" markdown="1">

- [2025.02] I was invited to serve as a mentor for the WACV 2025 Doctoral Consortium.
- [2024.12] Two papers on Human Motion Prediction and Affective Computing accepted by WACVW 2025.
- [2024.11] We are organizing [Elderly Action Recognition Challenge](https://voxel51.com/computer-vision-events/elderly-action-recognition-challenge-wacv-2025/) with Voxel51.
- [2024.10] We are organizing [CV4Smalls](https://cv4smalls2025.sites.northeastern.edu/) Workshop in WACV 2025.
- [2024.08] One paper on Human Attention Interruption Analysis accepted by *ICPR 2024*.
- [2024.05] One patent on Human Motion Prediction approved.
- [2023.09] One paper on defending against Data-Free Model Extraction (DFME) accepted by *NeurIPS 2023*.
- [2023.09] I joined [The Institute for Experiential AI (EAI)](https://ai.northeastern.edu/) at Northeastern Unversity as a Postdoctoral Research Fellow, working with [Dr. Agata Lapedriza](https://s3.sunai.uoc.edu/web/agata/index.html), [Dr. Sarah Ostadabbas](https://coe.northeastern.edu/people/ostadabbas-sarah/).
- [2023.08] I graduated from UB! 🎉🎉
- [2023.02] One paper on Continual Learning accepted by *CVPR 2023*.
- [2023.01] I successfully defended my dissertation proposal.
- [2022.07] One paper on Human Action Recognition accepted by *Neurocomputing*.
- [2022.06] One paper on Human Motion Prediction accepted by *IROS 2022* and *IEEE Robotics and Automation Letters*.
- [2022.02] I joined [XPENG Motors](https://heyxpeng.com/) as a Research Intern working with [Dr. Chen Bai](https://www.linkedin.com/in/chen-bai-a79743111/) and [Dr. Cheng Lu](https://www.linkedin.com/in/cheng-lu-5b24a739/).
- [2021.05] I joined [OPPO US Research Center](https://www.innopeaktech.com/) as a Research Intern working with [Dr. Zhong Li](https://sites.google.com/site/lizhong19900216) and [Dr. Yi Xu](https://www.linkedin.com/in/yi-xu-42654823/).
- [2021.01] One paper on Sign Language Recognition accepted by *IMWUT 2021*.
- [2020.10] One paper on Human Action Prediction accepted by *ICPR 2020*.
- [2020.04] One paper on Neural Architecture Search accepted by *IJCAI 2020*.
- [2019.05] I joined [Fuji Xerox Palo Alto Lab (FXPAL)](https://www.linkedin.com/company/fx-palo-alto-laboratory/about/) as a Research Intern working with [Dr. Yanxia Zhang](https://www.yanxiazhang.com/) and [Dr. Qiong Liu](https://www.linkedin.com/in/qiong-liu-8229446/?locale=zh_CN).
- [2018.10] One paper on Human Action Prediction accepted by *ICIP 2018*.
- [2018.08] I started my PhD in Computer Science at UB.

</div>

# Selected Publications 
<a href='https://scholar.google.com/citations?user=lTUM3B0AAAAJ'><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/yjzhux/yjzhux.github.io/google-scholar-stats/gs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WACVW 2025</div><img src='images/2025_UniMotion.png' alt="sym" width="100%"></div></div>
  <div class='paper-box-text' markdown="1">

  **UniMotion: Bridging 2D and 3D Representations for Human Motion Prediction**

  **Yanjun Zhu**, Chen Bai, Cheng Lu, David Doermann, and Agata Lapedriza

  *IEEE/CVF Winter Conference on Applications of Computer Vision Workshop (WACVW)*, 2025
  </div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICPR 2024</div><img src='images/2024_AdAttention.png' alt="sym" width="100%"></div></div>
  <div class='paper-box-text' markdown="1">

  **Multimodal Drivers of Attention Interruption to Baby Product Video Ads**

  Wen Xie, Lingfei Luan, **Yanjun Zhu**, Yakov Bart, and Sarah Ostadabbas

  *International Conference on Pattern Recognition (ICPR)*, 2024
  </div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2023</div><img src='images/2023_MeCo.png' alt="sym" width="100%"></div></div>
  <div class='paper-box-text' markdown="1">

  **Defending against Data-Free Model Extraction by Distributionally Robust Defensive Training**

  Zhenyi Wang, Li Shen, Tongliang Liu, Tiehang Duan, **Yanjun Zhu**, Donglin Zhan, David Doermann, Mingchen Gao

  *Annual Conference on Neural Information Processing Systems (NeurIPS)*, 2023
  </div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='images/2023_MetaMix.png' alt="sym" width="100%"></div></div>
  <div class='paper-box-text' markdown="1">

  **MetaMix: Towards Corruption-Robust Continual Learning with Temporally Self-Adaptive Data Transformation**

  Zhenyi Wang, Li Shen, Donglin Zhan, Qiuling Suo, **Yanjun Zhu**, Tiehang Duan, Mingchen Gao

  *Computer Vision and Pattern Recognition (CVPR)*, 2023
  </div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">RA-L</div><img src='images/2022_PIMNet.png' alt="sym" width="100%"></div></div>
  <div class='paper-box-text' markdown="1">

  **PIMNet: Physics-infused Neural Network for Human Motion Prediction**

  Zhibo Zhang\*, **Yanjun Zhu**\*, Rahul Rai, and David Doermann

  *IEEE Robotics and Automation Letters*, 7, No.4(2022): 8949-8955. *IROS*, 2022. (<font color=red>Oral</font>)

  (\* equal contribution)
  </div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neurocomputing</div><img src='images/2022_PB-GCN.png' alt="sym" width="100%"></div></div>
  <div class='paper-box-text' markdown="1">

  **PB-GCN: Progressive Binary Graph Convolutional Networks for Skeleton-based Action Recognition**

  Mengyi Zhao, Shuling Dai, **Yanjun Zhu**, Hao Tang, Pan Xie, Yue Li, Chunlei Liu, and Baochang Zhang

  *Neurocomputing* 501 (2022): 640-649.
  </div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IMWUT 2021</div><img src='images/2021_SonicASL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**SonicASL: An Acoustic-based Sign Language Gesture Recognizer using Earphones**

Yincheng Jin, Yang Gao, **Yanjun Zhu**, Wei Wang, Jiyang Li, Seokmin Choi, Zhangyu Li, Jagmohan Chauhan, Anind K. Dey, and Zhanpeng Jin

*ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT)* 5, no. 2 (2021): 1-30.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICPR 2020</div><img src='images/2020_JointPred.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**What and How? Jointly Forecasting Human Action and Pose**

**Yanjun Zhu**, Yanxia Zhang, Qiong Liu, Andreas Girgensohn, and David Doermann

*International Conference on Pattern Recognition (ICPR)*, 2020.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCAI 2020</div><img src='images/2020_CP-NAS.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CP-NAS: Child-Parent Neural Architecture Search for 1-bit CNNs**

Li'an Zhuo, Baochang Zhang, Hanlin Chen, Linlin Yang, Chen Chen, **Yanjun Zhu**, David Doermann

*International Joint Conference on Artificial Intelligence (IJCAI)*, 2020.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICIP 2018</div><img src='images/2018_KeyFrame.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Selecting Informative Frames for Action Recognition with Partial Observations**

**Yanjun Zhu**, Gang Yu, Junsong Yuan, and Kai-Kuang Ma 

*International Conference on Image Processing (ICIP)*, 2018. (<font color=red>Oral</font>)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TPAMI</div><img src='images/2017_BING++.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Sequential Optimization for Efficient High-Quality Object Proposal Generation**

Ziming Zhang, Yun Liu, Xi Chen, **Yanjun Zhu**. Ming-Ming Cheng, Venkatesh Saligrama, and Philip H.S. Torr

*IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)*, 40(5), pp.1209-1223, 2017.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Biosystems Engineering</div><img src='images/2016_Wheat.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**In-field automatic observation of wheat heading stage using computer vision**

**Yanjun Zhu**, Zhiguo Cao, Hao Lu, Yanan Li, and Yang Xiao

*Biosystems Engineering*, 143, pp.28-41, 2016. (<font color=red>Outstanding Paper Award</font>)
</div>
</div>

# Teaching

- [2023 Spring] Computer Vision and Image Processing
- [2022 Fall] Information Retrieval
- [2020 Fall] Blockchain Application Development
- [2020 Spring, 2019 Fall] Introduction to Machine Learning

# Honors and Awards

- [2021.09] Best Presentation Award, OPPO US Research Center
- [2018.07] European Society of Agricultural Engineers Outstanding Paper Award (1 per year)
- [2016.10] National Scholarship for Graduate Students (< 1%)
- [2014.12] Excellent Bachelor Thesis Award in Hubei Province, China (< 1%)

# Services

- **Workshop Chair**: [CV4Smalls](https://cv4smalls2025.sites.northeastern.edu/) with WACV 2025
- **Challenge Organizer**: [Elderly Action Recognition Challenge](https://voxel51.com/computer-vision-events/elderly-action-recognition-challenge-wacv-2025/) with Voxel51
- **Journal Guest Editor**: *Multimodal Tools and Applications (Special Issue, 2024)*
- **Journal Reviewer**: *Springer Plant Methods, IEEE TCSVT, Elsevier JVCIR, Multimodal Tools and Applications*
- **Conference Reviewer**: *ICIP, ICPR, ICCV, ECCV, CVPR, ACCV, WACV, NeurIPS, ICLR, ICML, ACM Multimedia, ICDAR, AAAI, MICCAI*

# &nbsp;

 