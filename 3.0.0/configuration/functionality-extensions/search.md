---
type: page
title: Search
listed: true
description: 
index_title: Search
hidden: true
keywords: 
tags: 
---

In the **Admin Panel \> Settings \> Configuration \> Search** section, settings related to search can be specified. Restrictions related to the number of reports and their age can be set for different user levels.

{% image url="https://uploads.developerhub.io/prod/XX2D/c609vnvij3fac07yml6j1zeq5ihx8rak2t7z1g6q294isbjevzslfu5podmcznji.png" %}
Search settings under Configuration
{% /image %}

### Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[308] %}
Fields
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SEARCH_REPORTS_LIMIT`
{% /cell %}
{% cell %}
This field sets the maximum number of reports returned by the search (not limited if the value is 0)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SEARCH_REPORTS_LIMIT_PREVALENCE`
{% /cell %}
{% cell %}
Limits the maximum number of similar reports to search for related to the IOCs. (not limited if the value is 0)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SEARCH_MONTHS_LIMIT_GUEST`
{% /cell %}
{% cell %}
It can be configured to return results going back how many months for guest users. (not limited if the value is 0)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SEARCH_MONTHS_LIMIT_USER`
{% /cell %}
{% cell %}
It can be configured to return results going back how many months for normal users. (not limited if the value is 0)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SEARCH_MONTHS_LIMIT_ADMIN`
{% /cell %}
{% cell %}
It can be configured to return results going back how many months for Admin users. (not limited if the value is 0)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SEARCH_MONTHS_LIMIT_INTEL`
{% /cell %}
{% cell %}
It can be configured to return results going back how many months for Intel users. (not limited if the value is 0)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SEARCH_MONTHS_LIMIT_PREVALENCE`
{% /cell %}
{% cell %}
How many months back to search for similar reports. (not limited if the value is 0)
{% /cell %}
{% /row %}
{% /table %}
