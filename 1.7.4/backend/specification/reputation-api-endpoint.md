---
type: page
title: Reputation API Endpoint
listed: true
description: 
index_title: Reputation API Endpoint
hidden: true
keywords: 
tags: 
---

This API endpoint allows checking reputation data (currently, limited to whitelist information) for one or multiple hashes (MD5, SHA-1, SHA-256, SHA-512). Based on the underlying configuration, this will either be the internal whitelist or output from other services, such as NSRL.

#### Syntax

`POST https://<ip>:<port>/reputation`

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
sha256
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Y
{% /cell %}
{% cell %}
SHA256 digest as found in the response of /submit or extracted resource in the reporting
{% /cell %}
{% /row %}
{% row %}
{% cell %}
hashes\[\]
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Y
{% /cell %}
{% cell %}
This may be an array of one or multiple hashes, provided with the “hashes\[\]” key as part of a form-data body part.
{% /cell %}
{% /row %}
{% /table %}

#### Example Response

{% code %}
```json
{
    "processTime": 148,
    "reputationResults":
    {
        "INTERNAL":
        {
            "processTime": 0,
            "whitelistedHashes":
            [
                "fffe43b0ba0137f2592e26bb98bbeca9"
            ],
            "invalidHashes":
            [
                "123"
            ]
        },
        "NSRL":
        {
            "processTime": 132,
            "whitelistedHashes":
            [
                "13210020db7a3e34ced1fa7b114155bc"
            ],
            "invalidHashes":
            [
                "123"
            ]
        }
    }
}
```
{% /code %}
