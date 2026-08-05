---
type: page
title: Release Notes for v1.8.1
listed: true
description: 
index_title: Release Notes for v1.8.1
hidden: true
keywords: 
tags: 
---

Date: 14 July, 2023

{% callout type="warning" title="Warning" %}
This version is not suitable for a clean installation due to breaking changes introduced in Docker 25. Please **use version 1.9.2 or later** for clean installations!
{% /callout %}

Added:

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
- Improved installation process (compatibility with CIS Level 1 OS hardening)
- Show if advanced scan options have been used

{% image url="https://uploads.developerhub.io/prod/XX2D/l1asvs2whqqcsupn5z5saqcoc2sm82x3y9txg8a73yue8ccpo627qik0plxfbd0s.png" width=1000 /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/klsqmiz0fi4v0yjn03tr8s0om80y5de3kvf3s8rxfgpg4em52ooxo5qau9g7dnbi.png" width=1000 /%}

Fixed:

- Added version lock-in for some URL scanning container dependencies
- Fixed a crash that could occur when specific brands were detected (Coinbase, JCB)
- Bugs within YARA rule score parsing
- Issues and incorrect classification with identification and tagging of registry files
- Improved parsing for registry key paths
- Issues and misclassification of OSINT lookups for extracted hashes
- Improved report generator to be resilient against phishing detection failing in the URL scanning task
