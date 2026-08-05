---
type: page
title: MD Core Sandbox Engine Features
listed: true
description: 
index_title: Sandbox Engine Features
hidden: true
keywords: 
tags: 
---

MetaDefender Sandbox technology is available as part of an integration with [MD Core](https://docs.opswat.com/mdcore). The integration is available with two different engine types: embedded and remote sandbox engine (with full reporting). The embedded engine is deployed with MD Core, similar to other engines (CDR/DLP). The remote engine requires a side-by-side installation of the full standalone sandbox platform.

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Feature
{% /cell %}
{% cell header=true colwidth=[319] %}
Embedded Engine
{% /cell %}
{% cell header=true %}
Remote Engine
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Installation OS
{% /cell %}
{% cell %}
Windows, Linux
{% /cell %}
{% cell %}
Ubuntu (Linux)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Archive handling
{% /cell %}
{% cell %}
**No**  \*
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
File parsers
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
File certificate validation
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Image text analysis (OCR)
{% /cell %}
{% cell %}
**No**
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Microsoft Office file emulation
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Powershell script emulation
{% /cell %}
{% cell %}
**No**
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
URL emulation (ML based phishing detection)
{% /cell %}
{% cell %}
**No**
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Fuzzy hash lookup
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Google safe browsing
{% /cell %}
{% cell %}
**No**
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
OPSWAT reputation lookup
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
YARA pattern matching
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% /table %}

Note: for a full list of engine features of the MetaDefender Sandbox standalone product, then visit [here](https://docs.opswat.com/filescan/datasheet/engine-features).

\*: The embedded engine doesn't support archive types itself, but the MetaDefender Core archive engine is able extract the files and send them to the sandbox for analysis
