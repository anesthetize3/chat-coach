---
type: page
title: Introduction
listed: true
description: 
index_title: Introduction
hidden: true
keywords: 
tags: 
---

## What is fsTransform?

The  OPSWAT Filescan Transformer ("fsTransform") can  process  a  single  file  (for  archive  support,  see  "fsBroker") specified either via the exposed API or from the file system as specified per the command line. Please refer to the user guide for more information on the setup and configuration. The following diagram gives an idea of where the transform processor node(s) are situated within the overall system architecture:

{% image url="https://uploads.developerhub.io/prod/XX2D/bz6nzd8clpz8y1tow1yymkbgtfzs4bcbcghmf6g1x9w3jyebpempjbe3mqrmzl2h.png" %}
System Architecture
{% /image %}

## What is the fsTransform API?

The fsTransform  API  is  a  simple  HTTP  based  programmatic  interface  that  allows  submission  of  files,  which  will  undertake  deep  static  analysis  and  transformed  into  a  reporting.  All  API  requests  require  authentication via a configurable secret and authorization levels. In the following, the most important API endpoints are presented.
