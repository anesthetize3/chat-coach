---
type: page
title: Task API Endpoint
listed: false
description: 
index_title: Task API Endpoint
hidden: false
keywords: 
tags: 
---

This API endpoint allows querying the reporting data returned by the underlying processor node. Based on an optional "all" parameter, a high-level or complete report can be retrieved. The "nocache" parameter is optional and determines whether cached reporting data (if available) may be returned or if the underlying processor node is to be re-queried.

#### Syntax

`GET https://<ip>:<port>/task`

#### Parameters

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true colwidth=[100] %}
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
submitID
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Y
{% /cell %}
{% cell %}
Submit ID as returned by /submit
{% /cell %}
{% /row %}
{% row %}
{% cell %}
all
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Reject submitted files, if their hash (MD5/SHA-256) is on an internal or external whitelist
{% /cell %}
{% /row %}
{% row %}
{% cell %}
nocache
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Disallow returning cached reporting data (if available). It is not recommended to set this flag, as the underlying processor nodes may clean up expired tasks triggering a 404 response code.
{% /cell %}
{% /row %}
{% /table %}

#### Example Response

{% code %}
```json
{
    "processTime": 535,
    "result":
    {...}
}
```
{% /code %}
