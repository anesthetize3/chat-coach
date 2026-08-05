---
type: page
title: File API Endpoint
listed: true
description: 
index_title: File API Endpoint
hidden: false
keywords: 
tags: 
---

This API endpoint allows downloading any processed or extracted (e.g. image embedded in a document) binary file. In order to retrieve a file, the SHA256 digest needs to be known. The reporting data as returned by /task will contain a variety of digests. The retrieved binary data is contained within the JSON response as a Base64 string. The decoded string is an inflated gzipped version.

*Note: the "mediaType" returned is the media type of the underlying file.*

#### Syntax

`GET https://<ip>:<port>/file`

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
    "compressedBase64": "KjFkN0hQY1ljUE5O(..)"
}
```
{% /code %}
