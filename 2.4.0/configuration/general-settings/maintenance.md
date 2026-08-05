---
type: page
title: Maintenance
listed: true
description: 
index_title: Maintenance
hidden: true
keywords: 
tags: 
---

Here you will find the Maintenance settings inside the Settings section part.

**Admin Panel \> Settings \> Configurations \> Functionality Extensions \> Maintenance**

These sections are useful for managing user experience during periods of system maintenance, troubleshooting, or updates. They provide a way to inform users about feature unavailability while also offering clarity regarding the reason for the issue.

{% image url="https://uploads.developerhub.io/prod/XX2D/h69gtchrd49o2hssy4uj1qwfb5z9rzzukrpbiuhei26bmitzfk728x5hqhydaz3k.png" /%}

These configurations allow ***Admins*** to temporarily disable scanning and search functionalities within MetaDefender Sandbox, for maintenance tasks or updates, and provide users with informative notifications about the unavailability of these features during such periods.

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[235] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*BLOCK\_SCAN*
{% /cell %}
{% cell %}
This configuration enables or disables the scanning functionality. When the box is ticked, it indicates that scanning is blocked or disabled.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*BLOCK\_SCAN\_NOTIFICATION*
{% /cell %}
{% cell %}
Specifies the message or notification displayed to users when scanning functionality is blocked or disabled. In this case, the message is *"Scanning is temporarily unavailable due to maintenance."*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*BLOCK\_SEARCH*
{% /cell %}
{% cell %}
This configuration  enables or disables the search functionality. When the box is ticked, it indicates that searching is blocked or disabled. In this case, the message is
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*BLOCK\_SEARCH\_NOTIFICATION*
{% /cell %}
{% cell %}
Specifies the message or notification displayed to users when search functionality is blocked or disabled. In this case, the message is *"Search is temporarily unavailable due to maintenance."*
{% /cell %}
{% /row %}
{% /table %}
