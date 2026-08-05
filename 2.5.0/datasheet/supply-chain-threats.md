---
type: page
title: Supply Chain Threats
listed: true
description: 
index_title: Supply Chain Threats
hidden: false
keywords: 
tags: 
---

## #1 Supply Chain Attack

**Detection Spotlight:** {% badge text="deep static" /%}{% badge text="malware config" /%}

The *SolarWinds* supply chain attack exemplifies how minimal code changes in trusted software can enable massive breaches while bypassing traditional security defenses. Threat actors injected a stealthy backdoor into a legitimate DLL, embedding malicious logic while preserving original functionality. The payload ran silently in a parallel thread mimicking legitimate components. With a valid digital signature and seamless behavior, the DLL evaded detection and granted covert access to thousands of high-profile victims. The compromise of the build pipeline turned trusted updates into a vehicle for global intrusion.

While a 4,000-line backdoor might seem significant, in the context of a large enterprise source code, it’s easily overlooked. This is where MetaDefender Sandbox excels: it doesn’t just inspect the code, it observes what the software does. It flags deviations from normal behavior, guiding analysts to what really matters—cutting through the noise to spotlight threats that traditional reviews would likely miss.

{% callout title="URL for original DLL" %}
[https://www.filescan.io/uploads/6862920d7423ff017c370754/reports/8fa054eb-8341-4dba-8e64-c1bfc5ce6913/overview](https://www.filescan.io/uploads/6862920d7423ff017c370754/reports/8fa054eb-8341-4dba-8e64-c1bfc5ce6913/overview)
{% /callout %}

{% callout title="URL for trojanized DLL" %}
[https://www.filescan.io/uploads/68629132714e106cecb7c676/reports/da0f9ed6-7f46-4cd0-ad98-abaef0c3d8d7/overview](https://www.filescan.io/uploads/68629132714e106cecb7c676/reports/da0f9ed6-7f46-4cd0-ad98-abaef0c3d8d7/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/f4syyszsuph5spnotm5fo1j8sdtpxzebw98xds65upmqyhsn6m0ciwgoi88rrcxh.png" %}
On the left, we see the legitimate DLL file. On the right is the trojanized version responsible for the infamous SolarWinds incident.
{% /image %}

Let’s walk through the key findings as revealed by the sandbox analysis:

{% image url="https://uploads.developerhub.io/prod/XX2D/2bbcel4wmuop599sqyrqtsquz92bnb5qwi162x70279h174ocx2j0gk4wvgkw5j5.png" %}
String encryption: the code employs a typical obfuscation technique found in various malware: compression followed by base64 encoding.
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/6wn2c93vfckqv03azg0isq8bja9hft4tdsjrkmnjtskj2jr5pxt4v0gtg1zd0rav.png" %}
WMI queries commonly associated with system fingerprinting. In this case, the related strings were encrypted to avoid detection.
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/e1rqyc1s668c5jkp9jtsbnlsivxia32hos9axjskgitwdrssazbjx3pcrs9l5vrx.png" width=945 %}
Multiple indicators tied to privilege escalation, user identity spoofing, and access control tampering.
{% /image %}

---

## #2 Detect malicious Pickle within AI model

**Detection Spotlight:** {% badge text="deep static" /%}

AI is powering everything from chatbots to business tools. To move faster, companies often use pre-trained AI models shared online through open source platforms like Hugging face. These models are saved in complex formats such as Pickle and PyTorch.

While it is convenience, this usage opens a new risk. Attackers can hide malware inside AI models, especially in Pickle files. Because Pickle can store both data and executable code, it has become a common vehicle for supply chain attacks. A model downloaded from a public repository may look safe but could trigger hidden instructions the moment it is loaded.

A recent case showed how attackers abused the reputation of *Alibaba AI* brand as a lure to publish fake PyPI packages containing a malicious AI model. These packages seem legitimate but contained hidden code to steal user's data and send it to the attacker. Although the packages were available for less than 24 hours on May 19, they were downloaded about 1,600 times. This shows how quickly malicious software can spread through a supply chain attack.

MetaDefender Sandbox uncovers these threats through dedicated Pickle and PyTorch scanning capabilities.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/68bf95d91b52c70384b7da92/reports/f4cb90b4-279a-47a3-b9ff-69b5e8232bd1/overview](https://www.filescan.io/uploads/68bf95d91b52c70384b7da92/reports/f4cb90b4-279a-47a3-b9ff-69b5e8232bd1/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/6zvswpzio8qoulce2xegluxc8oi31q7l8ua6nm8ag8qq8pzr3y0pemyxtbrzvc0a.png" %}
Multiple Pickle scanning methods from Third-party tools to Deep Static Analysis
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/579yna6j7e6rkfy1eixn4uk41nk8wc4tg2gx9q4z2nnjoic57nn6t617qyvwwogm.png" %}
REDUCE may be abused for arbitrary code execution and to embed malware in Pickle
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/3rez01vmxcdk2ug06n5gfcdcq5g70n1vwee1tz3p1x2dyrnwhu4tvlkk8zscf3wz.png" %}
Uncovering encoded payload
{% /image %}

---

---
