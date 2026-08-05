---
type: page
title: Submit Result API Endpoint
listed: true
description: 
index_title: Submit Result API Endpoint
hidden: false
keywords: 
tags: 
---

This API endpoint allows querying the response data of the underlying processor node, to which the broker submitted the accepted file. It will contain the application server ID, HTTP status code, result as well as the position in queue, if not submitted yet. If the file was submitted to a processor node, the state will be SUCCESS. Possible state values are: QUEUED, FAILED, SUCCESS.

*Note: this API is very lightweight and can be used to quickly obtain the queue position and submission status. For retrieval of the actual reporting, the /task API should be used.*

#### Syntax

`GET https://<ip>:<port>/submit-result`

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
{% /table %}

#### Example Response

{% code %}
```json
{
    "processTime": 29,
    "fileSize": 298083,
    "mediaType":
    {
        "string": "text/plain",
        "slash": 4,
        "semicolon": 10,
        "parameters":
        {}
    },
    "digests":
    {
        "SHA-1": "89f1e80601aad4a29f6b0d9dac27dbbc8043911e",
        "SHA-256": "ded996a1b8ecb407d0e33d2177d50ade036cbe8d1680dda4329bbd878f433ac1",
        "SHA-512": "2f28c0e765d031bbf166223ab5b732a7c8308c6421233ae776414938066e2b082ae1f-0799b56e0feb7e5da430e315b1ff0b1a60f6b47d36c22548c56a2d2c00d",
        "MD5": "e82aded7b074aaa0110445219bdbc6a1"
    },
    "base64": "KjFkN0hQY1ljUE5O(..)"
}
```
{% /code %}
