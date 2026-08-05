---
type: page
title: Audit Logger
listed: true
description: 
index_title: Audit Logger
hidden: true
keywords: 
tags: 
---

At the **Admin Panel \> Setting \> Configurations \> Audit Logger** section, you can enable or disable the Audit Logger and adjust its TTL (Time-to-Live).

### Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[262] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`ADMIN_AUDIT_LOGGER_ENABLED`
{% /cell %}
{% cell %}
Enable or disable admin audit logging.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`ADMIN_AUDIT_LOGGER_TTL`
{% /cell %}
{% cell %}
Logging Time-to-Live (TTL) in seconds.
{% /cell %}
{% /row %}
{% /table %}
