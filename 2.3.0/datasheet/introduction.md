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

## What components are part of the reporting engine?

The reporting engine consists of two components: a broker and the actual report generator engine (transform). The broker takes care of some internal load balancing, calculates the final verdict and handles multi-file submissions via archives (as each embedded archive file creates its own report).

## What is Broker?

The MetaDefender Sandbox backend broker receives and redistributes files for processing by one or multiple underlying application processor nodes (referred to as "transform"). The broker processes files either via the exposed API or from configurable file system pathways. Please refer to the user guide for more information on the setup and configuration. The following diagram gives an idea of where the broker is situated within the overall system architecture:

{% image url="https://uploads.developerhub.io/prod/XX2D/iq32hjwx29pj3q3w2z7fkr4xghap01oqpu5ta8krvxispymqvzw04u2si6fu2ph2.png" /%}

*Note: the API presented in this document is the same as used by the Web Backend of the community webservice. Thus, it can also be used programmatically by other implementations.*

## What is the broker API?

The broker API is a simple HTTP based programmatic interface that allows submission of files and archives, which will be processed and redistributed to a group of processor nodes ("transform", see above). Under the hood, the broker uses a file system-based priority queue and stores all received binary files in a central binary storage, which are also available via the API. All API requests require authentication via a configurable secret and authorization levels. In the following, the most important API endpoints are presented.

## What is transform?

The MetaDefender Sandbox engine ("transform") can process a single file (for archive support, see "broker") specified either via the exposed API or from the file system as specified per the command line. Please refer to the user guide for more information on the setup and configuration. The following diagram gives an idea of where the transform processor node(s) are situated within the overall system architecture:

{% image url="https://uploads.developerhub.io/prod/XX2D/5f679msf2zpxn2k3d7mc97t8tf9wmwazzcf7ifo2zzn30rdato9cll39x9ainkyv.png" /%}

## What is the transform API?

The transform API is a simple HTTP based programmatic interface that allows submission of files, which will undertake deep static analysis and transformed into a reporting. All API requests require authentication via a configurable secret and authorization levels. In the following, the most important API endpoints are presented.
