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
4
{% /cell %}
{% cell %}
URL scanner initialization failed (fsTransform only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
9
{% /cell %}
{% cell %}
Application servers could not be verified (fsBroker only)
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
Licence error (fsTransform only)
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
