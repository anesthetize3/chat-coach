---
type: page
title: OSINT Lookups
listed: true
description: 
index_title: OSINT Lookups
hidden: true
keywords: 
tags: 
---

**Step #1 - Open** `/home/sandbox/sandbox/transform.cfg` **in a text editor**

**Step #2 - Modify the configuration by adding or modifying the properties on this page**

**Step #3 - Save the file and restart the** `sandbox` **service**

## Enable OSINT

To enable reputation lookups and external tools, use the following settings.

{% code %}
```bash {% title="transform.cfg" %}
runOSINTLookups=true
runExtendedOSINTLookups=false
runOSINTLookupsOnExtractedFiles=false
runOSINTLookupsDistributedTimeoutMs=60000
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true colwidth=[110] %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runOSINTLookups
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Main switch to enable reputation lookups and external tool integrations on the input sample
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runExtendedOSINTLookups
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Enable execution for extracted IOCs
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runOSINTLookupsOnExtractedFiles
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Enable execution for extracted files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runOSINTLookupsDistributedTimeoutMs
{% /cell %}
{% cell %}
1 minute
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}

## Enable OSINT lookups exclusively on the input file hash

To enable reputation lookups to exclusively only perform OSINT lookups on the input file hash, use the following settings.

{% code %}
```bash {% title="transform.cfg" %}
runOSINTLookups=true
runExtendedOSINTLookups=false
runOSINTLookupsOnExtractedFiles=false
runOSINTLookupsRestrictedResourceTypes=FILE_HASH_SHA256
enableFuzzyHashLookup=false
calculateFuzzyFsioHash=false
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true colwidth=[110] %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runOSINTLookups
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Main switch to enable reputation lookups and external tool integrations on the input sample
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runExtendedOSINTLookups
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Enable execution for extracted IOCs
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runOSINTLookupsOnExtractedFiles
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Enable execution for extracted files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runOSINTLookupsRestrictedResourceTypes
{% /cell %}
{% cell %}
FILE\_HASH\_ SHA256, URL, DOMAIN
{% /cell %}
{% cell %}
Type of resource is being looked up during an OSINT query
{% /cell %}
{% /row %}
{% row %}
{% cell %}
enableFuzzyHashLookup
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Enable to perform any lookups based on fuzzy hashing
{% /cell %}
{% /row %}
{% row %}
{% cell %}
calculateFuzzyFsioHash
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Enable the calculation of fuzzy hashes for files during its lookups
{% /cell %}
{% /row %}
{% /table %}

## OPSWAT Reputation

Enable [OPSWAT Reputation lookups](https://docs.opswat.com/mdcloud/reputation/reputation)

{% code %}
```bash {% title="transform.cfg" %}
enableOpswatReputationAPI=true
opswatReputationAPIURL=https://api.metadefender.com/
opswatReputationAPIKey=
```
{% /code %}

{% callout title="API key" %}
The API key can be configured by the user manually, or it can be part of the license file. A demo API key is used if not specified by the user or license.
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property Name
{% /cell %}
{% cell header=true %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
enableOpswatReputationAPI
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable OPSWAT Reputation lookups
{% /cell %}
{% /row %}
{% row %}
{% cell %}
opswatReputationAPIURL
{% /cell %}
{% cell %}
[https://api.metadefender.com/](https://api.metadefender.com/)
{% /cell %}
{% cell %}
API URL
{% /cell %}
{% /row %}
{% row %}
{% cell %}
opswatReputationAPIKey
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
API key
{% /cell %}
{% /row %}
{% /table %}

## OPSWAT MultiScanning

Enable OPSWAT MultiScanning with [MetaDefender Cloud](https://docs.opswat.com/mdcloud) or [MetaDefender Core](https://docs.opswat.com/mdcore)

{% code %}
```bash {% title="transform.cfg" %}
enableMetaDefenderAPI=false
metaDefenderUseCloudAPI=true
metaDefenderAPIURL=https://api.metadefender.com/
metaDefenderAPIKey=
metaDefenderScanRule=
metaDefenderScanTimeout=60
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property Name
{% /cell %}
{% cell header=true %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
enableMetaDefenderAPI
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Switch to enable / disable OPSWAT MultiScanning
{% /cell %}
{% /row %}
{% row %}
{% cell %}
metaDefenderUseCloudAPI
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
If set to true, multiscan requests will be sent to MetaDefender Cloud If set to false, multiscan requests will be sent to MetaDefender Core
{% /cell %}
{% /row %}
{% row %}
{% cell %}
metaDefenderAPIURL
{% /cell %}
{% cell %}
[https://api.metadefender.com/](https://api.metadefender.com/)
{% /cell %}
{% cell %}
API URL (could also point to local instance of MDCore, e.g.: [http://10.0.0.5:8008/](http://10.0.0.5:8008/) )
{% /cell %}
{% /row %}
{% row %}
{% cell %}
metaDefenderAPIKey
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
API key
{% /cell %}
{% /row %}
{% row %}
{% cell %}
metaDefenderScanRule
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Workflow rule to use
{% /cell %}
{% /row %}
{% row %}
{% cell %}
metaDefenderScanTimeout
{% /cell %}
{% cell %}
1 minute
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}

## OPSWAT Fuzzy Hash Lookup

Fuzzy hashes are basically a SHA-256 of a long string that is built using a streamlined order, containing very high-level, but specific attributes of an input file. It is a proprietary algorithm and format developed by OPSWAT to enable detection of clusters of files / unknown malware. **MetaDefender Sandbox** (previously known as OPSWAT Filescan Sandbox) calculates FSIO Fuzzy hash for each appropriate input sample and looks for this hash in a specifically defined list.

**Fuzzy hash lookup results are displayed in OSINT Lookup section**

Please note, that you may not see result for every scanned malicious data.

The feature is enabled by default. To turn it off do the following steps:

{% code %}
```bash {% title="transform.cfg" %}
enableFuzzyHashLookup=false
```
{% /code %}

## Offline URL Reputation

Enable offline URL reputation lookups based on .

{% callout type="warning" title="Warning" %}
This is an experimental feature, only enabled in offline mode by default.
{% /callout %}

{% code %}
```bash {% title="transform.cfg" %}
enableOfflineUrlReputation=false
```
{% /code %}

## Virus Total

Enable [Virus Total](https://www.virustotal.com/)  lookups

{% code %}
```bash {% title="transform.cfg" %}
enableVirusTotalLookups=false
virusTotalAPIKey=
virusTotalQueriesPerMinute=4
virusTotalDefaultMaliciousEngineCount=3
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[285] %}
Property Name
{% /cell %}
{% cell header=true colwidth=[115] %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
enableVirusTotalLookups
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Switch to enable / disable Virus Total lookups
{% /cell %}
{% /row %}
{% row %}
{% cell %}
virusTotalAPIKey
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
API key
{% /cell %}
{% /row %}
{% row %}
{% cell %}
virusTotalQueriesPerMinute
{% /cell %}
{% cell %}
4
{% /cell %}
{% cell %}
Rate limiter for Virus total API queries / second. Value '0' means no rate limit.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
virusTotalDefaultMaliciousEngineCount
{% /cell %}
{% cell %}
3
{% /cell %}
{% cell %}
Malicious lookup verdict if at least the configured number of providers detected the input as malicious
{% /cell %}
{% /row %}
{% /table %}

## Broadcom Threat Intel Insight

Enable [Broadcom Threat Intel Insights](https://apidocs.securitycloud.symantec.com/#/doc?id=insight_api) lookups

{% code %}
```bash {% title="transform.cfg" %}
enableBroadcomInsightAPI=false
broadcomInsightAPIURL=https://api.sep.eu.securitycloud.symantec.com/
broadcomInsightSecret=
broadcomNetworkConfidenceThreshold=80
broadcomNetworkMaliciousThreatLevel=9
broadcomSha256ConfidenceThreshold=80
broadcomInsightMaxRetry=2
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property Name
{% /cell %}
{% cell header=true %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
enableBroadcomInsightAPI
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Switch to enable / disable Broadcom Threat Intel Insight lookups
{% /cell %}
{% /row %}
{% row %}
{% cell %}
broadcomInsightAPIURL
{% /cell %}
{% cell %}
[https://api.sep.eu.securitycloud.symantec.com/](https://api.sep.eu.securitycloud.symantec.com/)
{% /cell %}
{% cell %}
API URL
{% /cell %}
{% /row %}
{% row %}
{% cell %}
broadcomInsightSecret
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
API key
{% /cell %}
{% /row %}
{% row %}
{% cell %}
broadcomNetworkConfidenceThreshold
{% /cell %}
{% cell %}
80
{% /cell %}
{% cell %}
Network related results are accepted when meeting the confidence threshold
{% /cell %}
{% /row %}
{% row %}
{% cell %}
broadcomNetworkMaliciousThreatLevel
{% /cell %}
{% cell %}
9
{% /cell %}
{% cell %}
Network related threat level threshold to meet for malicious or or likely malicious verdicts. In case confidence treshold is 80 or above the verdict is malicious, otherwise likely malicious.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
broadcomSha256ConfidenceThreshold
{% /cell %}
{% cell %}
80
{% /cell %}
{% cell %}
File (SHA-256) related results are accepted when meeting the confidence threshold
{% /cell %}
{% /row %}
{% row %}
{% cell %}
broadcomInsightMaxRetry
{% /cell %}
{% cell %}
2
{% /cell %}
{% cell %}
Maximum number of retries for API requests
{% /cell %}
{% /row %}
{% /table %}

## Google Safe Browsing

Enable [Google Safe Browsing](https://developers.google.com/safe-browsing/)  lookups

{% code %}
```bash {% title="transform.cfg" %}
enableSafebrowsingLookups=false
safebrowsingAPI=
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property Name
{% /cell %}
{% cell header=true %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
enableSafebrowsingLookups
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Switch to enable / disable Safe Browsing lookups
{% /cell %}
{% /row %}
{% row %}
{% cell %}
safebrowsingAPI
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
API key
{% /cell %}
{% /row %}
{% /table %}
