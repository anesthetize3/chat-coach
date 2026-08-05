---
type: page
title: Maintenance
listed: true
description: 
index_title: Maintenance
hidden: false
keywords: 
tags: 
---

Here you will find the Maintenance settings inside the Configurations part.

**Admin Panel \> Setting \> Configurations \> Maintenance**

These configurations in MetaDefender Sandbox is to control functionalities related to blocking scanning and search features within the sandbox,  and used for maintenance purposes.

{% image url="https://uploads.developerhub.io/prod/XX2D/y30zdoi8uv0a1bx526wlsc1i8amp6xvf2llldait30pgigvcvkd1orqrsur37gaz.png" %}
Screenshot of Maintenance settings inside of Configurations on MetaDefender Sandbox webpage
{% /image %}

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
