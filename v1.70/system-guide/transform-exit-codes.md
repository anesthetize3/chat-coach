---
type: page
title: Transform Exit Codes
listed: true
description: 
index_title: Transform Exit Codes
hidden: false
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
pidfileindicates instance running already
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
Application servers could not be verified (broker only)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
10
{% /cell %}
{% cell %}
Webservice health check failures caused g raceful exit
{% /cell %}
{% /row %}
{% /table %}
