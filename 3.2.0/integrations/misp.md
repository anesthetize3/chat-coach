---
type: page
title: MISP
listed: true
description: 
index_title: MISP
hidden: false
keywords: 
tags: 
---

The MISP is an open source software solution for collecting, storing, distributing and sharing cyber security indicators and threats about cyber security incidents analysis and malware analysis. You can find more information about MISP [here](https://www.misp-project.org).

{% callout type="warning" title="Note" %}
To integrate with MISP, it is necessary to have a pre-installed MISP instance.
{% /callout %}

## Integrating MetaDefender Sandbox with MISP

To create an integration, navigate to the **Admin Panel**.

{% image url="../../assets/b7caa0cf962998168d635cabe195d8266900edd3.png" /%}

Select "Settings" from the menu bar, and you'll find the MISP tab under Configuration.

{% image url="../../assets/fd1ecd3e22f2f50d9426c95b28e8d7694b5e97b5.png" /%}

Enter your MISP API key and MISP API URL, check the "*MISP\_ENABLED*" checkbox, and then save the settings.

{% image url="../../assets/67ed56bd70c93689c376e9ef66c12391d512d43f.png" /%}

### Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[198] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MISP_API_KEY`
{% /cell %}
{% cell %}
MISP server API-key
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MISP_API_URL`
{% /cell %}
{% cell %}
The address of the MISP server
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MISP_TIMEOUT`
{% /cell %}
{% cell %}
Timeout, value in seconds. The 0 value disables timeout check!
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MISP_ENABLED`
{% /cell %}
{% cell %}
Check-box to enable or disable MISP integration
{% /cell %}
{% /row %}
{% /table %}

{% callout type="warning" title="Note" %}
note that in order for Sandbox results to be added as events to MISP, the url format should be:

**\<MISP URL\>/events/add**
{% /callout %}

If everything is correct, click on the "Save" button.

{% image url="../../assets/9862984389a01cd78f3826778f6b12253258934e.png" /%}

If MISP integration is enabled, then **Confirmed Threat** and **High Risk** results will be published.

If all settings are correct, events will appear in the MISP instance. For example:

{% image url="https://uploads.developerhub.io/prod/XX2D/topmyks36w5jdyndzumczo84hqa2uenw9lwc9wfy0prc5l8tfrqes2qirfefko6z.png" /%}
