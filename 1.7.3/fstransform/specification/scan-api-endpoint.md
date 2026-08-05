---
type: page
title: Scan API Endpoint
listed: true
description: 
index_title: Scan API Endpoint
hidden: true
keywords: 
tags: 
---

This API endpoint allows users to submit a file that will get converted into one task. The call is asynchronous and will return immediately. Using the task ID, the execution status and results can be retrieved later via the /task endpoint.

#### Syntax

`POST https://<ip>:<port>/scan`

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
password
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Archive password
{% /cell %}
{% /row %}
{% row %}
{% cell %}
priority
{% /cell %}
{% cell %}
Integer
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Processing priority (0 = default, 100 = highest)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
transformOpt.\[option\]
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
See fsBroker API Documentation foravailable options
{% /cell %}
{% /row %}
{% row %}
{% cell %}
$\_FILE
{% /cell %}
{% cell %}
Octet-Stream
{% /cell %}
{% cell %}
Y
{% /cell %}
{% cell %}
File/Archive as form-data body
{% /cell %}
{% /row %}
{% /table %}

#### Example Response

{% code %}
```json
{
    "processTime": 899,
    "scanTasks":
    [
        {
            "taskReference":
            {
                "name": "transform-file",
                "additionalInfo":
                {
                    "submitName": "file",
                    "digests":
                    {
                        "SHA-256": "99f8505240fff0831382ddf692f83750844887047ef90f59034d34d857271608"
                    },
                    "callbackDeleteAfter": false
                },
                "ID": "1fd6d36c-5909-498e-9351-ba8080e5c530",
                "state": "IN_PROGRESS",
                "opcount": 0,
                "processTime": 0
            },
            "opcount": 0,
            "processTime": 0,
            "taskWarnings":
            [],
            "allTags":
            [],
            "allSignalGroups":
            [],
            "resources":
            {}
        }
    ]
}
```
{% /code %}
