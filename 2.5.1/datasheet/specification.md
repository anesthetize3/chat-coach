---
type: page
title: Specification
listed: false
description: 
index_title: Specification
hidden: true
keywords: 
tags: 
---

## API workflow

The following diagram outlines a typical API workflow / use case for submitting a file / archive and retrieving the reporting and/or extracted binary files.

{% image url="https://uploads.developerhub.io/prod/XX2D/aejbx8i0kgl1i0jqo5fgkh7kkhlwedf1h1wyj1kzdb1g34zk29vuw9y1qjah8nx1.png" %}
Typical API Workflow
{% /image %}

## HTTP Default Configuration

For the API to become available, the broker needs to be launched with "listenMode" enabled. The HTTP port at which the API will become available is configurable via the "listenServerPort" option. The default port is **23001**.

## HTTP Response Codes

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Code
{% /cell %}
{% cell header=true %}
Definition
{% /cell %}
{% /row %}
{% row %}
{% cell %}
200
{% /cell %}
{% cell %}
Successful
{% /cell %}
{% /row %}
{% row %}
{% cell %}
204
{% /cell %}
{% cell %}
Successful, but no content
{% /cell %}
{% /row %}
{% row %}
{% cell %}
400
{% /cell %}
{% cell %}
Bad Request
{% /cell %}
{% /row %}
{% row %}
{% cell %}
404
{% /cell %}
{% cell %}
File Not Found
{% /cell %}
{% /row %}
{% row %}
{% cell %}
500
{% /cell %}
{% cell %}
Internal Server Error
{% /cell %}
{% /row %}
{% /table %}
