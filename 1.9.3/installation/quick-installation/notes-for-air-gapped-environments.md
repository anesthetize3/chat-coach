---
type: page
title: Air-gapped Systems
listed: true
description: 
index_title: Air-gapped Systems
hidden: true
keywords: 
tags: 
---

## Important notes for air-gapped systems

- The installation process **requires an Internet connection** (moving the system into a DMZ is recommended)
- Air-gapped systems will only receive updated features (like YARA) when installed and upgraded with an active internet connection. We recommend moving the system into a DMZ during these windows.
- All third-party integrations (e.g. Reputation API, geolocation/WHOIS lookup) require an Internet connection.
- The "File download" feature is not available in air-gapped environments.

To run the sandbox in an offline environment without any errors, the  following settings must be changed (after completing the installation  process in an online environment).

Please open `/home/filescanio/FileScanIO/fsTransform/conf/transform.properties.custom` using a text editor and add the following lines:

{% code %}
```java {% title="transform.properties.custom" %}
downloadLatestPeStudioForDataEnrichment=false
runDomainResolver=false
runFileDownloaders=false
runIPStackLookupOnExectractedHosts=false
runIPStackOnDomainResolvedIPs=false
runHexillionOnExtractedDomains=false
runWhoisRecordLookups=false
ntpServer=127.0.0.1
ntpServerTimeout=1
ntpServerRefreshRateInSeconds=31536000
runSystemUpdateEvery=31536000
runYaraUpdateOnStartup=false
runPatchesOnStartup=false
runOSINTLookups=false
```
{% /code %}

Also open `/home/filescanio/FileScanIO/fsTransform/conf/reputation.properties.custom` using a text editor and add the following line:

{% code %}
```java {% title="reputation.properties.custom" %}
refreshReputationSources=false
```
{% /code %}

Please remember to **save both configuration files** and restart the `fsio` service:

{% code %}
```bash
sudo service fsio restart
```
{% /code %}
