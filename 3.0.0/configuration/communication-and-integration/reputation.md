---
type: page
title: Reputation
listed: true
description: 
index_title: Reputation
hidden: true
keywords: 
tags: 
---

The Admin **Panel \> Setting \> Configurations \> Reputation** section allows for fine-tuning of the external reputation like MetaDefender Cloud or MetaDefender Sandbox Community.

### Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[427] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_MDCLOUD_THRESHOLD_MALICIOUS`
{% /cell %}
{% cell %}
The threshold at which we consider a result malicious for MD Cloud. For example, if this is 0.3, we consider something malicious if it's detected by 30% of the  MD Cloud engines.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_MDCLOUD_THRESHOLD_LIKELY_MALICIOUS`
{% /cell %}
{% cell %}
The threshold at which we consider a result likely malicious for MD Cloud.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_MDCLOUD_THRESHOLD_SUSPICIOUS`
{% /cell %}
{% cell %}
The threshold at which we consider a result suspicious for MD Cloud.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_MDCLOUD_THRESHOLD_DAYS_OLD`
{% /cell %}
{% cell %}
If the MD Cloud lookup result is very old, it might show false results. For example, a file previously labeled as Benign may later be identified as Malicious. This setting allows old results not to be taken into account. The value represents days.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_COMMUNITY_THRESHOLD_MALICIOUS`
{% /cell %}
{% cell %}
The threshold at which we consider a result malicious for Community votes.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_COMMUNITY_THRESHOLD_LIKELY_MALICIOUS`
{% /cell %}
{% cell %}
The threshold at which we consider a result likely malicious for Community votes.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_COMMUNITY_THRESHOLD_SUSPICIOUS`
{% /cell %}
{% cell %}
The threshold at which we consider a result suspicious for Community votes.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_COMMUNITY_THRESHOLD_VOTENUMBER`
{% /cell %}
{% cell %}
Threshold value for community votes. It is advisable to consider multiple votes.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPUTATION_BULK_LIMIT`
{% /cell %}
{% cell %}
Limit on how many hashes or IOCs you can search for at once in a bulk lookup scenario.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`IOC_REPORTS_REPUTATION_REPORTS_LIMIT`
{% /cell %}
{% cell %}
The report limit determines the maximum number of reports used to calculate the IOC's reputation verdict.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`IOC_REPORTS_REPUTATION_DAYS_LIMIT`
{% /cell %}
{% cell %}
The days limit specifies the maximum number of days of reports used to calculate the IOC's reputation verdict.
{% /cell %}
{% /row %}
{% /table %}
