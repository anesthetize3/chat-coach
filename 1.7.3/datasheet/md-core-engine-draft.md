---
type: page
title: MD Core Engine Draft
listed: false
description: 
index_title: MD Core Engine Draft
hidden: true
keywords: 
tags: 
---

Filescan's adaptive threat analysis technology is available as part of an integration with [MD Core](https://docs.opswat.com/mdcore). The integration is available with two different engine types: embedded and remote engine (with full reporting). The integration is in addition with the current [engine features](https://docs.opswat.com/filescan/datasheet/engine-features).

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[255] %}
*Engine Type*
{% /cell %}
{% cell header=true %}
*Feature*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Remote**
{% /cell %}
{% cell %}
Static file analysis

Dynamic analysis

Reputation service

YARA signature matcher
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Embedded**
{% /cell %}
{% cell %}
Static file analysis

Dynamic analysis

Reputation service

YARA signature matcher
{% /cell %}
{% /row %}
{% /table %}

{% callout type="warning" title="Warning" %}
Embedded engine type may have limited to no feature compared to the remote engine type. We recommend the remote engine type as we work on enhancing the embedded engine type.
{% /callout %}

{% callout title="Embedded & Remote Workflows" %}
Embedded engine contains a "scanner" engine directly installed on the [MD Core](https://docs.opswat.com/mdcore) machine, similar to other MD Core engines (for example DLP or CDR).

Remote engine is connecting to a remote Filescan server based on the configurable url and apikey, this can be an on premise installation or [Filescan.io](https://www.filescan.io/scan) itself.
{% /callout %}
