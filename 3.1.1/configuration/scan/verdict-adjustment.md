---
type: page
title: Verdict Adjustment
listed: true
description: 
index_title: Verdict Adjustment
hidden: false
keywords: 
tags: 
---

**Step #1 - Open** `/home/sandbox/sandbox/transform.cfg` **in a text editor**

**Step #2 - Modify the configuration by adding or modifying the properties on this page**

**Step #3 - Save the file and restart the** `sandbox` **service**

## **Disable Threat indicators**

One or more Threat indicators can be disabled, so those will not be evaluated during the verdict calculation process.

{% code %}
```bash {% title="transform.cfg" %}
ignoreVerdictForMatchingConsumerIDs=A000,AIT001
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ignoreVerdictForMatchingConsumerIDs
{% /cell %}
{% cell %}
- {% p /%}
{% /cell %}
{% cell %}
IDs to disable, separated by comma
{% /cell %}
{% /row %}
{% /table %}

## **Escalate Threat indicators**

One or more Threat indicators can be escalated, so those will be evaluated as Malicious during the verdict calculation process.

{% code %}
```bash {% title="transform.cfg" %}
escalateVerdictToMaliciousForMatchingConsumerIDs=A000,AIT001
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
escalateVerdictToMaliciousForMatchingConsumerIDs
{% /cell %}
{% cell %}
- {% p /%}
{% /cell %}
{% cell %}
IDs to escalate, separated by comma
{% /cell %}
{% /row %}
{% /table %}
