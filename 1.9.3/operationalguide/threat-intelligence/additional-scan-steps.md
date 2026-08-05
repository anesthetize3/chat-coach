---
type: page
title: Similarity Search Settings (Additional Scan Steps)
listed: true
description: 
index_title: Similarity Search Settings (Additional Scan Steps)
hidden: false
keywords: 
tags: 
---

You will find the Similarity Search Settings in the Additional Scan Steps tab among Configurations **Admin Panel \> Settings \> [Configuration](https://www.filescan.io/admin/settings/config) \> Additional Scan Steps tab**

{% callout title="Info" %}
**Customers are not recommended to interact the following fields as these are mainly for the Admin**

**The Similarity Search is disabled by default.**

**If it is enabled, you may find the same values set by default for each field.**
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/8kbaznnd45ffqy853wvq349sczz2oii51z6ivjyvbvfvzc2jsoumobe204qywyh7.png" /%}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[320] %}
Field
{% /cell %}
{% cell header=true colwidth=[269] %}
Description
{% /cell %}
{% cell header=true %}
Values
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*REPORT\_SIMILARITY\_VERDICT\_OVERWRITE*
{% /cell %}
{% cell %}
After the report is completed, it tries to search for similar reports that has been already processed. It will look at the verdict and can modify it.

(e.g. If previous similar reports show `malicious`it will change the verdict to `malicious)`
{% /cell %}
{% cell %}
ON/OFF
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*REPORT\_SIMILARITY\_VERDICT\_THRESHOLD*
{% /cell %}
{% cell %}
Specifies a threshold value (ranging from 0 to 1) for similarity checks. If the similarity ratio exceeds this threshold, it triggers a specific action or verdict overwrite
{% /cell %}
{% cell %}
Percentage converted to decimal
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*REPORT\_SIMILARITY\_VERDICT\_FILTER*
{% /cell %}
{% cell %}
Determines the minimal level of similarity verdict that needs to be checked against other samples (e.g., only consider similarities categorized as suspicious or higher)
{% /cell %}
{% cell %}
- no threat
- informational
- suspicious
- likely malicious
- malicious
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*REPORT\_SIMILARITY\_MALICIOUS\_MATCH*
{% /cell %}
{% cell %}
If the ratio of identified malicious similarities exceeds this threshold (0 to 1), the overall verdict for the analyzed sample is changed to "malicious."
{% /cell %}
{% cell %}
Percentage converted to decimal
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*REPORT\_SIMILARITY\_LIKELY\_MALICIOUS\_MATCH*
{% /cell %}
{% cell %}
Similarly, if the ratio of likely malicious similarities surpasses this threshold (0 to 1), the verdict is adjusted to "likely malicious."
{% /cell %}
{% cell %}
Percentage converted to decimal
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*REPORT\_SIMILARITY\_SUSPICIOUS\_MATCH*
{% /cell %}
{% cell %}
If the ratio of suspicious similarities meets or exceeds this threshold (0 to 1), the verdict is altered to "suspicious."
{% /cell %}
{% cell %}
Percentage converted to decimal
{% /cell %}
{% /row %}
{% /table %}
