---
type: page
title: Storage
listed: true
description: 
index_title: Storage
hidden: true
keywords: 
tags: 
---

The backend Sandbox engine creates and temporarily stores files like scan results, input files. The retention policy can be adjusted to fit to the throughput and disc size.

To modify the retention policy:

**Step #1 - Open** `/home/sandbox/sandbox/transform.cfg` **in a text editor**

**Step #2 - Modify the configuration by adding or modifying the following properties:**

{% code %}
```bash {% title="transform.cfg" %}
runFileSystemCleanup=true
cleanupCompletedTasksOlderThanXSeconds=600
```
{% /code %}

**Step #3 - Save the file and restart the** `sandbox` **service**

## Property details

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[276] %}
Property Name
{% /cell %}
{% cell header=true colwidth=[113] %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runFileSystemCleanup
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Main switch to enable / disable file retention feature
{% /cell %}
{% /row %}
{% row %}
{% cell %}
cleanupCompletedTasksOlderThanXSeconds
{% /cell %}
{% cell %}
10 minutes
{% /cell %}
{% cell %}
Retention for specific Sandbox scans
{% /cell %}
{% /row %}
{% /table %}

{% callout title="Info" %}
All other files will be removed daily
{% /callout %}
