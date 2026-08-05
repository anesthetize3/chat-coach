---
type: page
title: Providers
listed: true
description: 
index_title: Providers
hidden: false
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

MetaDefender Cloud also provides region-specific API endpoints that are listed here: [https://www.opswat.com/docs/mdcloud/compliance/locations](https://www.opswat.com/docs/mdcloud/compliance/locations)

*Disclaimer: By default, the region is selected automatically based on the user's geographic location. When performing reputation lookups, MetaDefender Cloud may also connect to external service providers that reside in different regions.*
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
