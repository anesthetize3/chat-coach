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

#### Broker System Info Endpoint

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
secret
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
{% row %}
{% cell %}
appServers
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Indicates, whether or not a subset of the /system-info response of fsTransform application servers should be returned
{% /cell %}
{% /row %}
{% /table %}

#### Example Response

{% code %}
```json
{
    "versionInfo":
    {
        "name": "broker",
        "version": "1.0.0",
        "copyright": "Copyright 2024 OPSWAT Inc., All Rights Reserved,www.filescan.com"
    },
    "queueInfo":
    {
        "queueCount": 0
    },
    "memoryStats":
    {
        "usedMemory": 21,
        "freeMemory": 538,
        "totalMemory": 560,
        "maxMemory": 14492
    },
    "freeDiscSpaceInMb":
    {
        "Samples": 1833809,
        "fsBrokerQueue": 1833809,
        "fsBrokerResults": 1833809,
        "fsTemp": 79668
    }
}
```
{% /code %}

---

#### Transform System Info Endpoint

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
secret
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
        "name": "transform",
        "version": "1.0.0",
        "copyright": "Copyright 2024 OPSWAT Inc., All Rights Reserved, www.filescan.com"
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
