---
type: page
title: Release Notes for v1.8.0
listed: true
description: 
index_title: Release Notes for v1.8.0
hidden: false
keywords: 
tags: 
---

---

## Date: 8 June, 2023

{% callout type="warning" title="Warning" %}
This version is not suitable for a clean installation due to breaking changes introduced in Docker 25. Please **use version 1.9.2 or later** for clean installations!
{% /callout %}

Added:

- A new **single source of truth** reputation lookup for Hashes, URLs, IPs, and Domains. Automatically integrated with [MDCloud](https://docs.opswat.com/mdcloud) look up. Always yielding a result, independent of whether a report was generated for the search query.

{% image url="https://uploads.developerhub.io/prod/XX2D/sxq4cwh240m4qm5yyb0r4ylxdtsz403sbnes2kcxer57gi5m7b46so26nbvclz1q.png" /%}

- Threat Intelligence Similarity Search feature for Portable Executable (PE) files

{% image url="https://uploads.developerhub.io/prod/XX2D/5cwr31a79mzoo60dddpga6710r1id2fssk9coc5sr2c8279xrnps3cx8mgleq4si.png" /%}

- Emulation metadata parsing from self-extracting archive files
- Detection of appended files in images with steganography
- Administrative feature to overrule scan report verdict
- Detection of file executions initiated by msiexec on remotely fetched MSI files

Changed:

- Extended certificate whitelisting with QT Framework signatures
- Extended Filescan Reputation API with support for IPs, domains and URLs
- Extended Filescan Fuzzy Hash blacklist hits with additional details
- Optimized JPG processing speed
- Fine -tuned YARA rule behaviors
- Fine-tuned fuzzy hash lookup verdict contribution
- Improved RTF emulation success rate
- Enhanced startup time with lighting fast speed and performance
- Improved verdict calculation

Fixed:

- Service stability issues
- Service availability issues via automated restart mechanism
- Backend disk usage issues
- Backend service error handling issues
- Phishing URL detection issues
- OSINT provider verdict standardization issues
