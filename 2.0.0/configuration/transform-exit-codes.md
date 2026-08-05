---
type: page
title: Sandbox Engine Exit Codes
listed: true
description: 
index_title: Sandbox Engine Exit Codes
hidden: true
keywords: 
tags: 
---

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Code
{% /cell %}
{% cell header=true %}
Definition
{% /cell %}
{% /row %}
{% row %}
{% cell %}
0
{% /cell %}
{% cell %}
Successful
{% /cell %}
{% /row %}
{% row %}
{% cell %}
1
{% /cell %}
{% cell %}
Configuration self-test failed
{% /cell %}
{% /row %}
{% row %}
{% cell %}
2
{% /cell %}
{% cell %}
pidfile indicates instance running already
{% /cell %}
{% /row %}
{% row %}
{% cell %}
3
{% /cell %}
{% cell %}
Webservice initialization failed
{% /cell %}
{% /row %}
{% row %}
{% cell %}
5
{% /cell %}
{% cell %}
YARA update failed (transform only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
6
{% /cell %}
{% cell %}
IP based geolocation failed (transform only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
7
{% /cell %}
{% cell %}
Failed to get VirusTotal scan report (transform only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
8
{% /cell %}
{% cell %}
Email test failed
{% /cell %}
{% /row %}
{% row %}
{% cell %}
9
{% /cell %}
{% cell %}
Application servers could not be verified (broker only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
10
{% /cell %}
{% cell %}
Webservice health check failures caused graceful exit
{% /cell %}
{% /row %}
{% row %}
{% cell %}
11
{% /cell %}
{% cell %}
Licence error (transform only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
12
{% /cell %}
{% cell %}
Archive unpack test failed (broker only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
13
{% /cell %}
{% cell %}
No valid input sources available (broker only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
100
{% /cell %}
{% cell %}
Unexpected error
{% /cell %}
{% /row %}
{% /table %}
