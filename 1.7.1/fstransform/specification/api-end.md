---
type: page
title: System Info Endpoint
listed: true
description: 
index_title: System Info Endpoint
hidden: false
keywords: 
tags: 
---

This API endpoint allows retrieval of basic system stats, such as the version, name, queue size, disc usage and memory footprint.

#### Syntax

`GET https://<ip>:<port>/system-info`

#### Parameters

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Required?
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
serect
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Y
{% /cell %}
{% cell %}
Authentication secret
{% /cell %}
{% /row %}
{% /table %}

#### Example Response

{% code %}
```json
{
    "versionInfo":
    {
        "name": "fsTransform",
        "version": "1.0.0",
        "copyright": "Copyright 2020 Jan Miller, All Rights Reserved, www.filescan.io"
    },
    "queueInfo":
    {
        "activeCount": 0,
        "queueCount": 0,
        "completedCount": 0
    },
    "memoryStats":
    {
        "usedMemory": 556,
        "freeMemory": 1103,
        "totalMemory": 1660,
        "maxMemory": 3641
    },
    "freeDiscSpaceInMb":
    {
        "fsResources": 26970,
        "fsResults": 67967,
        "fsTasks": 26970
    },
    "activeThreads": 5,
    "systemEvents":
    {},
    "counters":
    {},
    "comments":
    []
}
```
{% /code %}
