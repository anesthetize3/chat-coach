---
type: page
title: MetaDefender Multiscanning
listed: true
description: 
index_title: MetaDefender Multiscanning
hidden: true
keywords: 
tags: 
---

The OPSWAT Filescan Sandbox platform can integrate MetaDefender Core API to perform AV engine scans on input/extracted files.

- [https://docs.opswat.com/mdcore/metadefender-core/ref#file-analysis-process](https://docs.opswat.com/mdcore/metadefender-core/ref#file-analysis-process)

To enable this integration, please walk through the following steps:

**Step #1 - Copy your MetaDefender Core API key**

If you already have a MetaDefender Core API key, skip to **Step #2.**

Log in to your MetaDefender Core:

- Go to User Management menu
- Find and select your user under Users and Groups tab
- At the API key section, click on Generate and copy your API key

**Step #2 - Open** `FileScanIO/fsTransform/conf/transform.properties.custom` **in a text editor**

Add the following configuration variables, please use your own API key:

{% code %}
```bash
enableMetaDefenderAPI=true
metaDefenderUseCloudAPI=false
metaDefenderAPIURL=MY_MDCORE_URL   # E.g.: http://10.0.0.5:8008/ 
metaDefenderAPIKey=MY_API_KEY
```
{% /code %}

{% callout type="warning" title="Warning" %}
Please make sure to include the final / for the `metaDefenderAPIURL` parameter! E.g.: [http://10.0.0.5:8008/](http://10.0.0.5:8008/)
{% /callout %}

Please remember to **save the file.**

**Step #3 - Restart the** `fsio` **service**

{% code %}
```bash
sudo service fsio restart
```
{% /code %}

**Step #4 - Scan a file and verify if the OPSWAT MetaDefender Multiscanning results are displayed in the OSINT Lookup section**

It is recommended to test a file that is commonly known, e.g.: a Windows executable.
