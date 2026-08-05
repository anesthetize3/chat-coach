---
type: page
title: Release Notes for v1.8.1
listed: true
description: 
index_title: Release Notes for v1.8.1
hidden: false
keywords: 
tags: 
---

---

## Date: 14 July, 2023

{% callout type="warning" title="Warning" %}
This version is not suitable for a clean installation due to breaking changes introduced in Docker 25. Please **use version 1.9.2 or later** for clean installations!
{% /callout %}

Added:

- Compliance with CIS Level 1 OS hardening: [https://www.cisecurity.org/cis-benchmarks](https://www.cisecurity.org/cis-benchmarks)
- Detection for fast reverse proxy
- Detection for suspicious file extensions
- Detection for RCE in Office files (leveraged in CVE-2022-30190)
- Collector for identified packer statistics
- Indicator for malicious files with .scr extension
- Flagging for common words used as filename in phishing-delivered artifacts
- Increase brand coverage for phishing detection to support 300 brands
- Possibility to regenerate API key
- Buttons to download certificates and public key files

{% image url="https://uploads.developerhub.io/prod/XX2D/2xcxvu5tnqmqmq27iy4rjart56u866p74uqqwx4oy4cgazt4rl7ebrpej184yvz3.png" width=1000 /%}

Changed:

- Improved file type detection for more precise accuracy
- Improved VBA emulation to support additional features
- Improved emulation error handling to have a better success ratio
- Improved privacy and handling of personal information
- Improved verdict calculation
- Improved string analysis
- Improved detection and tagging of LOLBins
- Improved analysis of emulation indicators for dynamically allocated Windows APIs
- Improved analysis of URLs to detect commonly abused web services for Command and Control or exfiltration
- Improved logging and logging configuration
- Improved installation process (compatibility with hardened Ubuntu systems)
- Show if advanced scan options have been used

{% image url="https://uploads.developerhub.io/prod/XX2D/hpt4v3fdj0yrvxiqg4ph7v8pu0bkwz913nyjfu3f5cxyqm08gbo8rmca480afvpq.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/txia2ihlfi4dcge7zl1oan740ps6i6ppz8sypm1ryit685hjre05ocnqe45fa4kv.png" /%}

Fixed:

- Added version lock-in for some URL scanning container dependencies
- Fixed a crash that could occur when specific brands were detected (Coinbase, JCB)
- Bugs within YARA rule score parsing
- Issues and incorrect classification with identification and tagging of registry files
- Improved parsing for registry key paths
- Issues and misclassification of OSINT lookups for extracted hashes
- Improved report generator to be resilient against phishing detection failing in the URL scanning task
