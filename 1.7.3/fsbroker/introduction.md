---
type: page
title: Introduction
listed: true
description: 
index_title: Introduction
hidden: false
keywords: 
tags: 
---

## What is fsBroker?

The OPSWAT Filescan Broker ("fsBroker") receives and redistributes files for processing by one or multiple underlying application processor nodes (referred to as "fsTransform"). The broker processes files either via the exposed API or from configurable file system pathways. Please refer to the user guide for more information on the setup and configuration. The following diagram gives an idea of where the broker is situated within the overall system architecture:

{% image url="https://uploads.developerhub.io/prod/XX2D/59hj7egsxss0fouatl6qgw8bboagnvst8oceox7frq9ivdf58ryxuye098pocojt.png" %}
System Architecture
{% /image %}

*Note: the API presented in this document is the same as used by the Web Backend of the community webservice. Thus, it can also be used programmatically by other implementations.*

## What is the fsBroker API?

The fsBroker API is a simple HTTP based programmatic interface that allows submission of files and archives, which will be processed and redistributed to a group of processor nodes ("fsTransform", see above). Under the hood, the broker uses a file system-based priority queue and stores all received binary files in a central binary storage, which are also available via the API. All API requests require authentication via a configurable secret and authorization levels. In the following, the most important API endpoints are presented.
