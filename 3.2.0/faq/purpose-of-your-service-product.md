---
type: page
title: Why use MetaDefender Aether?
listed: true
description: 
index_title: Why use MetaDefender Aether?
hidden: false
keywords: 
tags: 
---

The primary focus of **MetaDefender Aether** (previously known as MetaDefender Sandbox) and its standalone edition is not only to detect malicious files, but also to extract potential "Indicators of Compromise" (IOCs) from compressed, obfuscated, and encrypted data in a short time and without full runtime analysis that requires a slow and resource-intensive virtual machine (VM). This process is performed using a set of proprietary emulation engines (including virtual file systems and partial OS emulation), at scale and with rapid speed compared to traditional VM-based runtime analysis.

{% image url="https://uploads.developerhub.io/prod/XX2D/ccw2ivtxrqnsr4jcm2m7cckzeuehuihc0lz82o9xhsijztyrwvlial4je10htkrv.png" /%}

For example, an email (msg/eml) with a maldoc attachment (typically containing a heavily obfuscated VBA macro) is fully analyzed within \~10-15 seconds including all relevant threat indicators. This includes inspection of download URLs, underlying files, as well as a recursive analysis of embedded artifacts.

In addition, all files are scanned for thousands of malicious threats and – when possible – mapped to the MITRE ATT\&CK framework for quicker assessment. Using generative AI, an easy digestable executive summary can be generate for your analysts.
