---
type: page
title: MetaDefender Cloud Reputation Service
listed: true
description: 
index_title: MetaDefender Cloud Reputation Service
hidden: false
keywords: 
tags: 
---

MetaDefender Aether on-premise / standalone integrates with the MetaDefender Cloud Reputation Service:

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

For that select *Settings* on the top and select *Configurations* on the page. You will find the Providers under Communications and Integrations:

{% image url="../../assets/10b8a4ad9ed8b20147e7ec8b709d62fcebc793e9.png" /%}

**Step #3 - Set the MD Cloud Service - API options**

## Set up in the configuration file (optional)

{% callout type="warning" title="Warning" %}
Modifying the transform.cfg configuration file is only necessary for a multi-server deployment!

For single-server deployments, the configuration is automatically synced between components.
{% /callout %}

For more details, see the [OSINT Lookups](../configuration/scan/engine-config-osint-lookups.md) configuration page.

It is recommended to test a file that is commonly known, e.g.: a Windows executable.
