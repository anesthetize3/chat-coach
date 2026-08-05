---
type: page
title: General
listed: true
description: 
index_title: General
hidden: false
keywords: 
tags: 
---

Here you will find the General configurations inside the Configurations part.

**Admin Panel \> Setting \> Configurations \> General**

The following configurations are for controlling various aspects such as user interface elements, file upload limits, caching behaviour, and API version.

{% image url="../../../assets/0905e4fde503b7db7624a95ac697299bc7f3b6ca.png" /%}

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
{% cell colwidth=[303] %}
*APP\_TITLE*
{% /cell %}
{% cell %}
This configuration specifies the title of the application, which is "Filescan.IO" in this case. However, it can be configured to the user specific organization or needs.
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*APP\_DESC*
{% /cell %}
{% cell %}
This can describe the application briefly or display a slogan. In this case, it states MetaDefender Sandbox slogan, which is a "Next-Gen Malware Analysis Platform".
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*HOME\_THEME*
{% /cell %}
{% cell %}
Home page theme can be selected.
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*AD\_FREQUENCY*
{% /cell %}
{% cell %}
In the given % of the reports there will be an advertisement presented for community users on the report page pointing towards commercial version's page. There are no advertisements in the standalone product. {% inline-image url="asset:oib2lxjq96mf" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*MAX\_UPLOAD\_SIZE*
{% /cell %}
{% cell %}
Sets the maximum allowed size for file uploads, given in megabytes (MB). It shouldn't exceed 2000 MB, or 2 gigabytes (GB). In this case, it's set to 100 MB.
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*REPORT\_CACHE\_TTL\_MINUTES*
{% /cell %}
{% cell %}
Specifies the time-to-live (TTL) for cached reports, in minutes. Reports will be cached for 20 minutes in this configuration.
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*USE\_HUMAN\_FRIENDLY\_VERDICTS*
{% /cell %}
{% cell %}
If enabled, human friendly verdicts will be used. If disabled, risk score based verdicts will be used. More info: [Report Verdict](../../datasheet/layer-1---threat-reputationpm8/verdict.md)
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*AUTOMATIC\_REPORT\_FILES\_DOWNLOAD*
{% /cell %}
{% cell %}
If enabled, the Webservice will download extracted and embedded files that are associated with the scan report.

Note: The additional URL screenshot for [brand detection](https://www.opswat.com/docs/filescan/3.1.1/datasheet/detected-brands) (formerly phishing) is only available if enabled.
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*OFFLINE\_MODE*
{% /cell %}
{% cell %}
Use this option if you are using your application in an [air-gapped environment](https://www.opswat.com/docs/filescan/3.1.1/installation/notes-for-air-gapped-environments#important-notes-for-air-gappedoffline-systems).
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*TRUSTED\_NETWORK\_MODE*
{% /cell %}
{% cell %}
If enabled, only the following network communications are allowed:

- OSINT providers
- Whois lookups
- system updates
- email notifications
- certificate revocation lists
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*SHOW\_FOOTER*
{% /cell %}
{% cell %}
Likely a boolean flag indicating whether to display a footer on the application's interface.
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*SCAN\_FILES\_PER\_UPLOAD*
{% /cell %}
{% cell %}
Determines the number of files that can be scanned per upload. Set to 5 in this case.
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*API\_VERSION (read-only)*
{% /cell %}
{% cell %}
Specifies the version of the API being used, set to 1.0 here.
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*BASE\_DIR  (read-only)*
{% /cell %}
{% cell %}
Specifies the base directory for the application's source files, set to "/app/src"
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[303] %}
*DEBUG (read-only)*
{% /cell %}
{% cell %}
Likely a boolean flag indicating whether the application is in debug mode.
{% /cell %}
{% /row %}
{% /table %}
