---
type: page
title: API Quota
listed: true
description: 
index_title: API Quota
hidden: true
keywords: 
tags: 
---

Under the **Admin Panel \> Settings \> API Quota** menu, you can specify various restrictions related to API usage. These restrictions include setting limits for different time intervals, which can be tailored for specific endpoints or user groups.

{% image url="https://uploads.developerhub.io/prod/XX2D/ori2xvr614gbjpph3sn6xtbe70xcq6okkz5o5d906wc347enreiqnsb9v41jyxoy.png" /%}

To add some quota, click on the **"+ Add quota"** button.

{% image url="https://uploads.developerhub.io/prod/XX2D/ogr1lc15drxioytmzo6t5pexyblfn2m28dq1ooj97g3kpui87oqo0yuaq5r3urz2.png" /%}

In the popup window, the following settings can be configured:

{% callout type="warning" title="Note" %}
Please specify max. amount of requests per period of time. You do not need to specify values for all periods. Do not select any group to make settings default.
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[259] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Route
{% /cell %}
{% cell %}
Specify the endpoint to which the restriction applies. E.g.: /api/scan/file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Groups
{% /cell %}
{% cell %}
Specify the groups to which the restriction applies. E.g.: Guests
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Requests each **X** sec.
{% /cell %}
{% cell %}
Specify the limit for **X** seconds, where **X** is a customizable number as well.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Requests / min
{% /cell %}
{% cell %}
Specify the maximum number of requests per minute.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Requests / hour
{% /cell %}
{% cell %}
Specify the maximum number of requests per hour.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Requests / day
{% /cell %}
{% cell %}
Specify the maximum number of requests per day.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Requests / week
{% /cell %}
{% cell %}
Specify the maximum number of requests per day.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Requests / month
{% /cell %}
{% cell %}
Specify the maximum number of requests per month.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Credits per 1 request
{% /cell %}
{% cell %}
Specify the number of credits assigned to each request. (integer)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Total credits per month
{% /cell %}
{% cell %}
Specify how much credit value can be used to submit requests per month.
{% /cell %}
{% /row %}
{% /table %}

After clicking the save button, the new limit is set and appears on the interface:

{% image url="https://uploads.developerhub.io/prod/XX2D/poytrudy7a4s8tooh3l7g5vfl16f7swrbedhq4duultwlddhser0fnut5pmgrzdm.png" /%}
