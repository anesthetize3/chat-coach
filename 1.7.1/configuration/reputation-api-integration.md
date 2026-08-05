---
type: page
title: Reputation API Integration
listed: true
description: 
index_title: Reputation API Integration
hidden: true
keywords: 
tags: 
---

FileScan integrates with the MetaDefender Cloud Reputation API:

- [https://docs.opswat.com/mdcloud/metadefender-cloud-api-v4/ref#tag-hash-lookups](https://docs.opswat.com/mdcloud/metadefender-cloud-api-v4/ref#tag-hash-lookups)
- [https://docs.opswat.com/mdcloud/metadefender-cloud-api-v4/ref#tag-reputation-service](https://docs.opswat.com/mdcloud/metadefender-cloud-api-v4/ref#tag-reputation-service)

To enable this integration, please walk through the following steps:

**Step #1 - Copy your MetaDefender Cloud API key**

If you already have a MetaDefender Cloud API key, skip to **Step #2.**

Log in to  MetaDefender Cloud:

- If you don't have an OPSWAT account yet, please register a free account [here](https://id.opswat.com/register?redirect=https%3A%2F%2Fmetadefender.opswat.com%2Flogin&app=appMDC0001)
- If you already created an OPSWAT account, please [log in to MetaDefender Cloud](https://metadefender.opswat.com/) using your credentials

Navigate to the Account Information page: [https://metadefender.opswat.com/account](https://metadefender.opswat.com/account) and copy your API key.

**Step #2 - Open** `FileScanIO/fsTransform/conf/transform.properties.custom` **in a text editor**

Add the following configuration variables, please use your own API key:

{% code %}
```bash
enableOpswatReputationAPI=true
opswatReputationAPIKey=MYAPIKEY
```
{% /code %}

Please remember to **save the file.**

**Step #3 - Restart the** `fsio` **service**

{% code %}
```bash
sudo service fsio restart
```
{% /code %}

**Step #4 - Scan a file and verify if the OPSWAT Reputation API results are displayed in OSINT Lookup section**

It is recommended to test a file that is commonly known, e.g.: a Windows executable.
