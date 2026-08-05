---
type: page
title: Database
listed: true
description: 
index_title: Database
hidden: true
keywords: 
tags: 
---

These configurations are related to database connections within the Sandbox webservice.

The location of the ***Database*** settings are **Admin Panel \> Settings \> [Configurations](https://www.filescan.io/admin/settings/config) \> Database.**

{% image url="https://uploads.developerhub.io/prod/XX2D/x2xtnc2gqfwm5end8w2o1vgnr8rb4i647s5awk0vo36wlybkv7ck3ji93v6vi18e.png" %}
Screenshot of Database configuration on MetaDefender Sandbox webpage
{% /image %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[258] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`DB_CONN_URL`
{% /cell %}
{% cell %}
It specifies the connection URL for the primary database used by Sandbox.  It should determine what is its primary database, what is the accessible hostname and on what port. Sandbox includes its own MongoDB container. The default setting should not be changed.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`GRAPH_DB_CONN_URL`
{% /cell %}
{% cell %}
It specifies the connection URL for a graph database used by Sandbox. Sandbox includes its own graph database container. The default setting should not be changed.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REDIS_CONN_URL`
{% /cell %}
{% cell %}
This configuration specifies the connection URL for a Redis database used by the application. Sandbox includes its own Redis container. The default setting should not be changed.
{% /cell %}
{% /row %}
{% /table %}
