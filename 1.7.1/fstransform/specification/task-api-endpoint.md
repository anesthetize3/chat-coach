---
type: page
title: Task API Endpoint
listed: true
description: 
index_title: Task API Endpoint
hidden: false
keywords: 
tags: 
---

This API endpoint allows querying the reporting data for a previously submitted task. Based on an optional “all” parameter, a high-level or complete report can be retrieved.

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
{% row %}
{% cell %}
taskID
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Y
{% /cell %}
{% cell %}
Must be provided in combination with "appServerID", if "submitID" is not provided
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
Return all reporting data or just a high-level version
{% /cell %}
{% /row %}
{% /table %}

#### Example response

{% code %}
```json
{
    "processTime": 535,
    "result":
    {...}
}
```
{% /code %}
