---
type: page
title: VirusTotal API
listed: true
description: 
index_title: VirusTotal API
hidden: true
keywords: 
tags: 
---

## Set up in the configuration file

**Step #1 - Open** `FileScanIO/fsTransform/conf/transform.properties.custom` **in a text editor**

Add the following configuration variables, please use your own API key.

Optionally update the VirusTotal API usage limit: `virusTotalQueriesPerMinute`. Setting `0` means unlimited.

{% code %}
```bash {% title="Config" %}
enableVirusTotalLookups=true
virusTotalAPIKey=<your secret>
virusTotalQueriesPerMinute=3
```
{% /code %}

Please remember to **save the file.**

**Step #2 - Restart the** `fsio` **service**

{% code %}
```bash
sudo service fsio restart
```
{% /code %}

**Step #3 - Scan a file and verify if the VirusTotal API results are displayed in OSINT Lookup section**

It is recommended to test a file that is commonly known, e.g.: a Windows executable.
