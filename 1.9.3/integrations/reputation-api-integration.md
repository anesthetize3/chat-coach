---
type: page
title: MetaDefender Cloud Reputation Service
listed: true
description: 
index_title: MetaDefender Cloud Reputation Service
hidden: true
keywords: 
tags: 
---

MetaDefender Sandbox on-premise / standalone integrates with the MetaDefender Cloud Reputation Service:

- [https://docs.opswat.com/mdcloud/metadefender-cloud-api-v4/ref#tag-hash-lookups](https://docs.opswat.com/mdcloud/metadefender-cloud-api-v4/ref#tag-hash-lookups)
- [https://docs.opswat.com/mdcloud/metadefender-cloud-api-v4/ref#tag-reputation-service](https://docs.opswat.com/mdcloud/metadefender-cloud-api-v4/ref#tag-reputation-service)

To enable this integration, please walk through the following steps:

{% callout type="warning" title="Warning" %}
MetaDefender Cloud API key is necessary for the integration. It has to be set **both** on the webservice and in the sandbox engine.
{% /callout %}

**Copy your MetaDefender Cloud API key**

If you already have a MetaDefender Cloud API key, skip to **Set up from the admin panel** or **Set up in the configuration file**.

Log in to  MetaDefender Cloud:

- If you don't have an OPSWAT account yet, please register a free account [here](https://id.opswat.com/register?redirect=https%3A%2F%2Fmetadefender.opswat.com%2Flogin&app=appMDC0001)
- If you already created an OPSWAT account, please [log in to MetaDefender Cloud](https://metadefender.opswat.com/) using your credentials

Navigate to the Account Information page: [https://metadefender.opswat.com/account](https://metadefender.opswat.com/account) and copy your API key.

After you retrieve the MetaDefender Cloud API key, there are two ways to set up the integration:

1. Set up from the admin panel,
2. Set up in the configuration file.

## Set up from the admin panel

**Step #1 - Go to the Admin panel**

Go to the user (top right) and click on the Admin panel menu item.

**Step #2 - Go to the providers**

For that select *Settings* on the top and select *Providers* on the Configuration page:

{% image url="https://uploads.developerhub.io/prod/XX2D/u28yh2g6862l0wmybocmz7ouc7znmtngd7mv3ie7ocm2k6oubic8no63b3cl9bly.png" /%}

**Step #3 - Set the MD Cloud Service - API options**

## Set up in the configuration file

**Step #1 - Open** `FileScanIO/fsTransform/conf/transform.properties.custom` **in a text editor**

Add the following configuration variables, please use your own API key:

{% code %}
```bash {% title="Config" %}
enableOpswatReputationAPI=true
opswatReputationAPIKey=MYAPIKEY

runOSINTLookupsOnExtractedFiles=true
extractedFileProviders=OPSWAT_REPUTATION
```
{% /code %}

Please remember to **save the file.**

**Step #2 - Restart the** `fsio` **service**

{% code %}
```bash
sudo service fsio restart
```
{% /code %}

**Step #3 - Scan a file and verify if the MetaDefender Cloud Reputation Service API results are displayed in OSINT Lookup section**

It is recommended to test a file that is commonly known, e.g.: a Windows executable.
