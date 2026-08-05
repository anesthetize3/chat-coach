---
type: page
title: MD Core Engine
listed: true
description: 
index_title: MD Core Engine
hidden: true
keywords: 
tags: 
---

Filescan's adaptive threat analysis technology is also available as part of an integration with MD Core. It is available as an embedded and remote engine (with full reporting). Please find a comparison chart of the different engine feature sets below.

See full list of features [here](https://docs.opswat.com/filescan/1.7.3/datasheet/engine-features).

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Feature
{% /cell %}
{% cell header=true %}
Subfeature
{% /cell %}
{% cell header=true %}
Remote
{% /cell %}
{% cell header=true %}
Embedded
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Dynamic analysis
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Partial" type="warning" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Microsoft Office file emulation
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Powershell script emulation
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
URL emulation, phishing detection
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Static file analysis
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Partial" type="warning" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
File parsers
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
File certificate validation
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Image text analysis (OCR) \*
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Reputation service
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Partial" type="warning" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Fuzzy hash lookup
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Google safe browsing
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
OPSWAT reputation lookup
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
YARA signature matcher
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% /table %}

{% callout type="warning" title="Note" %}
The embedded engine is a work in progress and we expect more feature parity shortly.
{% /callout %}
