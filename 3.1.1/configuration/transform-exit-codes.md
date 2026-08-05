---
type: page
title: Sandbox Engine Exit Codes
listed: true
description: 
index_title: Sandbox Engine Exit Codes
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
5
{% /cell %}
{% cell %}
YARA update failed (transform only)
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
11
{% /cell %}
{% cell %}
Licence error (transform only)
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
