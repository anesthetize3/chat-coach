---
type: page
title: General
listed: true
description: 
index_title: General
hidden: true
keywords: 
tags: 
---

Here you will find the General configurations inside the Configurations part.

**Admin Panel \> Setting \> Configurations \> General**

The following configurations are for controlling various aspects such as user interface elements, file upload limits, caching behaviour, and API version.

{% image url="https://uploads.developerhub.io/prod/XX2D/krqgvsdy08apie88k0rhg530hrryvt5s1oh8y4p4y5lvoldqlevngbppbldgssmo.png" %}
Screenshot of MetaDefender Sandbox General settings
{% /image %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[303] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*APP\_TITLE*
{% /cell %}
{% cell %}
This configuration specifies the title of the application, which is "Filescan.IO" in this case. However, it can be configured to the user specific organization or needs.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*APP\_DESC*
{% /cell %}
{% cell %}
This can describe the application briefly or display a slogan. In this case, it states MetaDefender Sandbox slogan, which is a "Next-Gen Malware Analysis Platform".
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*AD\_FREQUENCY*
{% /cell %}
{% cell %}
In the given % of the reports there will be an advertisement presented for community users on the report page pointing towards commercial version's page. There are no advertisements in the standalone product. {% inline-image url="asset:9kvgauu3eyng" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*MAX\_UPLOAD\_SIZE*
{% /cell %}
{% cell %}
Sets the maximum allowed size for file uploads, given in megabytes (MB). It shouldn't exceed 2000 MB, or 2 gigabytes (GB). In this case, it's set to 100 MB.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*REPORT* CACHE *TTL\_MINUTES*
{% /cell %}
{% cell %}
Specifies the time-to-live (TTL) for cached reports, in minutes. Reports will be cached for 20 minutes in this configuration.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*SHOW\_FOOTER*
{% /cell %}
{% cell %}
Likely a boolean flag indicating whether to display a footer on the application's interface.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*SCAN* FILES *PER\_UPLOAD*
{% /cell %}
{% cell %}
Determines the number of files that can be scanned per upload. Set to 5 in this case.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*API\_VERSION (read-only)*
{% /cell %}
{% cell %}
Specifies the version of the API being used, set to 1.0 here.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*BASE\_DIR  (read-only)*
{% /cell %}
{% cell %}
Specifies the base directory for the application's source files, set to "/app/src"
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*DEBUG (read-only)*
{% /cell %}
{% cell %}
Likely a boolean flag indicating whether the application is in debug mode.
{% /cell %}
{% /row %}
{% /table %}
