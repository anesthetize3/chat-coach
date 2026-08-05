---
type: page
title: Adaptive Sandbox Full Report Overview
listed: true
description: 
index_title: Adaptive Sandbox Full Report Overview
hidden: true
keywords: 
tags: 
---

**This is an introduction to the MetaDefender Sandbox Full Report (Remote module).**

**Overview**

Provides an overview of recent analysis activities and user statistics.

Link to report: [Filescan.IO - Analysis Report for 9e7d694ed87ae95f9c25af5f3a5cea76188cd7c1c91ce49c92e25585f232d98e - Overview](https://www.filescan.io/uploads/6712504c7f0507a8d241e0a3/reports/16baffa5-8671-4f37-be5d-842d838a0382/overview)

{% image url="https://uploads.developerhub.io/prod/XX2D/hcl18qmre4h9znbw1z5sjrwpeodp14uf9p71maxa4yrbqxmm8pl2jtdc8memh8ju.png" /%}

**Overview includes the following**

Submission Info

- Including the Name: File Name
- Mediatype: Type or format of a file being analyzed
- Hash: The unique ID of the file hashing calculation
- Report ID: The unique ID for the Report
- Submission Date: The timestamp of the scan

Tags

- Tags are used to categorize or label files based on specific attributes, behaviors, or detected threats. These tags help users to highlight important information like file origin, vulnerability types, or known malware families.

ChatGPT

- To help get summary using the ChatGPT integration.

Analysis Overview

The analysis overview includes all malicious results the Sandbox detected, for all verdicts, please see: [https://docs.opswat.com/filescan/datasheet/verdict](https://docs.opswat.com/filescan/datasheet/verdict)

- Threat Indicators: They highlight potential malicious activities, suspicious behaviors or benign activities in files.
  - E.g. OSINT source detected malicious resource: Indicates a file or URL linked to a known malicious source based on Open Source Intelligence (OSINT).

{% image url="https://uploads.developerhub.io/prod/XX2D/jyeqdu61n5c018018w4w2wevsdviikjelekkx6mzhlzifxyzy0pvhv5z0wrrxpg5.png" /%}

Filters

With the help of the side panel, the user can filter down for verdict, tags, MITRE Techniques and Origin

- MITRE Techniques
- It allows users to identify and categorize specific techniques used by malware or attackers, as defined by the MITRE ATT\&CK framework

**File Details**

It is comprehensive information about a specific file, including its hash, file type, size, and origin. This may also include metadata like version information, or the software used to create it. This feature is useful for analyzing potentially malicious files and understanding their characteristics.

{% image url="https://uploads.developerhub.io/prod/XX2D/e5v7jx02yg07znhgwv7ytfnqo5o7dzie89o4r29ovv3bssf98vhdmac0bgr5dy6x.png" /%}

**Extended Details**

This section dives deeper into the file's characteristics, possibly including information about its compilation, digital signatures, and other technical details.

{% image url="https://uploads.developerhub.io/prod/XX2D/8769xrk7qf8dyszsiiv4zp248y8v9vujaze391gt4y36jswl213ih54b8r3ykc1w.png" /%}

- **Entropy: 7.1:** This suggests a moderate level of randomness in the file, which can indicate potential encryption or obfuscation. Higher entropy values often raise red flags as they might signal that the file is hiding something.
- **ForensicAnalysisRecommended: false:** This means that, based on the analysis, there’s no immediate need for a deeper forensic examination, which could imply that the file doesn't exhibit known signs of being malicious.

**Indicators of Compromise (IOCs)**

IOCs are extracted from the input binary or derived data (e.g. extracted files) of the analysis. Indicators that are highly likely to be an IOC are marked as interesting.

{% image url="https://uploads.developerhub.io/prod/XX2D/g8kyu2x6vaj53io2c1u750ff3lciirm2gg5es466olyi0z34o887sj8idz97tq6m.png" /%}

**Threat Intelligence**

Scan and analyze files with more than 300 features and match complex patterns in known malicious files to hunt threats and identify new and unknown malware. During the similarity search, files undergo a rigorous scanning procedure using the MetaDefender Sandbox static and file emulation technologies. This advanced technology extracts the most relevant and useful information from a given file.

{% image url="https://uploads.developerhub.io/prod/XX2D/o5khohda4ncf58psk171altudgiq4yp985r9wjy0ey8o64cciqt0enl18tgr01yo.png" /%}

Learn more about Threat Intelligence here: [https://docs.opswat.com/filescan/operationalguide/similarity-search](https://docs.opswat.com/filescan/operationalguide/similarity-search)

**Disassembly Section**

This can be particularly useful for reverse engineering, malware analysis, or debugging purposes. In this section, you can see how the code is structured, which instructions are executed, and how different components of the file interact with each other.

{% image url="https://uploads.developerhub.io/prod/XX2D/my0znt7zi9mbu0km71w659nconfevro100i88eon09yijshufzk5thbcivwdgtcu.png" /%}

Learn more about Disassembly here: [https://docs.opswat.com/filescan/datasheet/showcase-reports#6-finding-interesting-things-via-disassembly](https://docs.opswat.com/filescan/datasheet/showcase-reports#6-finding-interesting-things-via-disassembly)

**YARA Rules**

It is used for identifying and classifying malware or suspicious files based on specific patterns. YARA, which stands for "Yet Another Recursive Acronym," allows users to create rules that can match certain characteristics within files, such as strings or byte sequences.

{% image url="https://uploads.developerhub.io/prod/XX2D/sd2izhzt5moprc38x2tj4ggwp8c3c43ltx9iwy0101y35jv3kw1e1ej6tmo8np3o.png" /%}

**Extracted Strings**

Further information that can be extracted from the file meta data.

{% image url="https://uploads.developerhub.io/prod/XX2D/pyrxdpnzk8tlljzjfvjtfh7x1qvvjkm6pp1njgtdjpa69odiggsnayivlyz2fbqz.png" /%}

**Extracted files**

The list of files that have been extracted from a scanned archive or binary. This feature is useful for analyzing the contents of complex files, such as executables or compressed archives, where multiple files may be contained within.

{% image url="https://uploads.developerhub.io/prod/XX2D/dmrruac30kyxfyz4st3cnbzd3qzqyokhcbxlqokbsr2ynybx8pxofsohyok6nrjl.png" /%}

**OSINT Lookups**

OSINT utilizes the hash and other IOCs to check against the online reputation services to make sure that the file is safe, it also lists out the malicious components as tags for better awareness.

{% image url="https://uploads.developerhub.io/prod/XX2D/24bg5eswy1yagw77l77ubhyqpz7gnxl4w7il4qpnocsifwh5kynrgf8t2eyrgalr.png" /%}

**Geolocation**

The geolocation feature provides information about the geographical locations associated with a file, typically based on its network activity or the IP addresses it may communicate with.

{% image url="https://uploads.developerhub.io/prod/XX2D/izjwx5ffxtfe7pdo4t60853fpeky6qhy3oh9y1wnf26w4gw9rsgk72brzmuax6id.png" /%}

{% callout title="Support:" %}
If **Further Assistance** is required, please proceed to log a [**support case or chatting with our support engineer**](https://my.opswat.com/support).
{% /callout %}
