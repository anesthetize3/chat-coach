---
type: page
title: Providers
listed: true
description: 
index_title: Providers
hidden: true
keywords: 
tags: 
---

At the **Admin Panel \> Setting \> Configurations \> Providers** settings, you can specify numerous configurations related to [MetaDefender Cloud](https://docs.opswat.com/mdcloud).

These include the following:

{% image url="https://uploads.developerhub.io/prod/XX2D/a1f7g8stwnv3pmndb9ovc26i9av1r0hhgr8tvqyvzkphjcihc97oaq9a3yukbibk.png" /%}

### Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[269] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MDCLOUD_API_URL`
{% /cell %}
{% cell %}
MetaDefender Cloud API URL address. E.g:  `https://api.metadefender.com`
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MDCLOUD_API_KEY`
{% /cell %}
{% cell %}
Your MetaDefender Cloud API key.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MDCLOUD_TTL_HOURS`
{% /cell %}
{% cell %}
The TTL (Time-to-Live) of the locally stored reputation table, in hours. The table contains reputations coming from MD Cloud.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MDCLOUD_REPUTATION_ENABLED`
{% /cell %}
{% cell %}
Enable or Disable MetaDefender Cloud reputation.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MDCLOUD_THREATINTEL_ENABLED`
{% /cell %}
{% cell %}
Enable or Disable MetaDefender Cloud ThreatIntel.
{% /cell %}
{% /row %}
{% /table %}
