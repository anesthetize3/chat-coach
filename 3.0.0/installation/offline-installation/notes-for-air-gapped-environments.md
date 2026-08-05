---
type: page
title: Air-gapped Systems
listed: true
description: 
index_title: Air-gapped Systems
hidden: false
keywords: 
tags: 
---

## Important notes for air-gapped/offline systems

- The normal installation process **requires an Internet connection** (moving the system into a DMZ is recommended)
- The offline installation process **does not require** any network connectivity: [Offline Installation](../offline-installation.md)
- Air-gapped systems will only receive updated features (like YARA) when installed and upgraded with an active Internet connection. We recommend moving the system into a DMZ during these windows.
- All third-party integrations (e.g. Reputation API, geolocation/WHOIS lookup) require an Internet connection.
- The "File download" feature is not available in air-gapped environments.

To run the sandbox in an offline environment without any errors, the  following setting must be applied (after completing the installation  process in an online environment).

{% callout title="Info" %}
The "offlineMode=true" setting is automatically added when an [Offline Installation](../offline-installation.md) is performed.

There is no need to apply any futher changes!
{% /callout %}

Please open `/home/sandbox/sandbox/transform.cfg` using a text editor and add the following line:

{% code %}
```java {% title="transform.cfg" %}
offlineMode=true
```
{% /code %}

Please remember to **save the configuration file** and restart the `sandbox` service:

{% code %}
```bash
sudo service sandbox restart
```
{% /code %}
