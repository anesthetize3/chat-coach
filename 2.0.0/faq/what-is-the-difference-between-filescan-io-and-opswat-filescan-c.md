---
type: page
title: What is the difference between Filescan.io and MetaDefender Sandbox commercial offerings?
listed: true
description: 
index_title: What is the difference between Filescan.io and MetaDefender Sandbox commercial offerings?
hidden: false
keywords: 
tags: 
---

{% table layout="auto" %}
{% row %}
{% cell header=true %}
**Feature**
{% /cell %}
{% cell header=true %}
**Filescan.IO (Community)**
{% /cell %}
{% cell header=true colwidth=[243] %}
Adaptive Sandbox (Embedded MetaDefender Core Module)
{% /cell %}
{% cell header=true %}
**MetaDefender Sandbox** **(Platform)**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Use Case
{% /cell %}
{% cell %}
Free Triage with public reports, limited configurability
{% /cell %}
{% cell %}
Detection, Triage Alerts
{% /cell %}
{% cell %}
Full Malware Analysis, Triage Alerts, Threat Hunting
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Private Reports
{% /cell %}
{% cell %}
No
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
Full Report
{% /cell %}
{% cell %}
Partially
{% /cell %}
{% cell %}
Partially (only with remote engine that utilizes the platform)
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Access all uploaded samples
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
File size limit
{% /cell %}
{% cell %}
100MB
{% /cell %}
{% cell %}
2000MB
{% /cell %}
{% cell %}
2000MB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
API Limits
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
No (MD Core API)
{% /cell %}
{% cell %}
No (FileScan.IO API)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Priority Processing
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
User Management
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
Within MD Core
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ACL / Backend Access
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Configurable Engine
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
Partially
{% /cell %}
{% cell %}
Fully
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Configurable YARA rules
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Advanced Search / Threat Hunting Capability
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Integration with SOAR
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Integration with SIEM
{% /cell %}
{% cell %}
No
{% /cell %}
{% cell %}
Yes, via CEF syslog
{% /cell %}
{% cell %}
Yes, via CEF syslog
{% /cell %}
{% /row %}
{% /table %}
