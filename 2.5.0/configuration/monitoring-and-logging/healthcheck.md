---
type: page
title: Healthcheck
listed: true
description: 
index_title: Healthcheck
hidden: false
keywords: 
tags: 
---

At the **Admin Panel \> Setting \> Configurations \> Healthcheck** settings, various settings related to monitoring can be configured.

Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[346] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`HCS_PERIOD_MIN`
{% /cell %}
{% cell %}
The minimum time interval, in **minutes**, between health check operations.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`HCS_RETENTION_DAYS`
{% /cell %}
{% cell %}
The number of **days** for which health check records are retained in the system.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`HCS_PROXY_HOST`
{% /cell %}
{% cell %}
The hostname or IP address of the proxy server used for health checks.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`HCS_FSIO_URI`
{% /cell %}
{% cell %}
The Sandbox URI specifying the endpoint for health check operations.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_QUEUE_LONG_CHECK_TIME_INTERVAL`  ¹
{% /cell %}
{% cell %}
Seconds between pings of long running check. Max of it or `KEEP_JOB_RESULT_SECONDS` is used
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_QUEUE_QUICK_CHECK_STEPS_INTERVAL`¹
{% /cell %}
{% cell %}
Scan iterations between quick checks. Result time is calculated to be bigger then `KEEP_JOB_RESULT_SECONDS`
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_QUEUE_ALLOWED_CHECKS_MISSED`  ¹
{% /cell %}
{% cell %}
Allowed checks amount missed to still consider queue healthy
{% /cell %}
{% /row %}
{% /table %}

¹Healthcheck of scan queues. Final values are calculated to be bigger then `KEEP_JOB_RESULT_SECONDS` = 10
