---
type: page
title: Static Analysis
listed: true
description: 
index_title: Static Analysis
hidden: false
keywords: 
tags: 
---

**Step #1 - Open** `/home/sandbox/sandbox/transform.cfg` **in a text editor**

**Step #2 - Modify the configuration by adding or modifying the properties on this page**

**Step #3 - Save the file and restart the** `sandbox` **service**

## URLs

Enable domain resolver, [IP stack](https://ipstack.com/) Geolocation and [Hexillion WHOIS](https://hexillion.com/) domain lookups

{% callout title="Info" %}
[IP Geolocation lookup](https://docs.opswat.com/filescan/configuration/ip-geolocation) will be executed on resolved domains
{% /callout %}

{% code %}
```bash {% title="transform.cfg" %}
runDomainResolver=true
domainResolveMaxResolves=20
runIPStackOnDomainResolvedIPs=true
runIPStackOnDomainResolvedIPsMaxLookups=20
runDomainResolveDistributedTimeoutMs=60000
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runDomainResolver
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable domain resolving
{% /cell %}
{% /row %}
{% row %}
{% cell %}
domainResolveMaxResolves
{% /cell %}
{% cell %}
20
{% /cell %}
{% cell %}
Domain resolver limit, '0' means no limit
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runIPStackOnDomainResolvedIPs
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Execute Geolocation on resolved IPs
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runIPStackOnDomainResolvedIPsMaxLookups
{% /cell %}
{% cell %}
20
{% /cell %}
{% cell %}
Geolocation limit on resolved IPs, '0' means no limit
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runDomainResolveDistributedTimeoutMs
{% /cell %}
{% cell %}
1 minute
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}

{% code %}
```bash {% title="transform.cfg" %}
runIPStackLookupOnExectractedHosts=true
runIPStackLookupMaxLookups=30
runIPStackLookupTimeoutMs=30000
ipStackAccessKey=
ipStackUrl=https://api.ipstack.com/$ip?access_key=$accessKey
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
unIPStackLookupOnExectractedHosts
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable domain resolving and geolocation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runIPStackLookupMaxLookups
{% /cell %}
{% cell %}
30
{% /cell %}
{% cell %}
Lookup limit, '0' means no limit
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runIPStackLookupTimeoutMs
{% /cell %}
{% cell %}
30 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ipStackAccessKey
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
ipStackUrl
{% /cell %}
{% cell %}
[https://api.ipstack.com/$ip?access\_key=$accessKey](https://api.ipstack.com/$ip?access_key=$accessKey)
{% /cell %}
{% cell %}
API URL
{% /cell %}
{% /row %}
{% /table %}

{% code %}
```bash {% title="transform.cfg" %}
runWhoisRecordLookups=true
runHexillionLookupTimeoutMs=30000
runHexillionLookupMaxLookups=30
hexillionUrl=https://hexillion.com/rf/xml/1.0/whois/?query=$domain
hexillionUsername=
hexillionPassword=
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
runWhoisRecordLookups
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable WHOIS lookups
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runHexillionLookupTimeoutMs
{% /cell %}
{% cell %}
30 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runHexillionLookupMaxLookups
{% /cell %}
{% cell %}
30
{% /cell %}
{% cell %}
Lookup limit, '0' means no limit
{% /cell %}
{% /row %}
{% row %}
{% cell %}
hexillionUrl
{% /cell %}
{% cell %}
[https://hexillion.com/rf/xml/1.0/whois/?query=$domain](https://hexillion.com/rf/xml/1.0/whois/?query=$domain)
{% /cell %}
{% cell %}
API URL
{% /cell %}
{% /row %}
{% row %}
{% cell %}
hexillionUsername
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
API username
{% /cell %}
{% /row %}
{% row %}
{% cell %}
hexillionPassword
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
API password
{% /cell %}
{% /row %}
{% /table %}

## Office Documents

Enable static analysis for Microsoft Office documents

{% code %}
```bash {% title="transform.cfg" %}
runContentParser=true
runContentParserDirectTimeoutMs=10000
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runContentParser
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable Office document static analysis
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runContentParserDirectTimeoutMs
{% /cell %}
{% cell %}
10 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}

## OLE Files

Enable parsing OLE files

{% code %}
```bash {% title="transform.cfg" %}
runOledumpOnOLEFiles=true
runOledumpBiffOnXLSFiles=true
oledumpExecutionTimeout=30
oledumpMaxFileSizeInKb=1024
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runOledumpOnOLEFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable OLE parsing
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runOledumpBiffOnXLSFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Enable or disable parsing of BIFF records
{% /cell %}
{% /row %}
{% row %}
{% cell %}
oledumpExecutionTimeout
{% /cell %}
{% cell %}
30 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
oledumpMaxFileSizeInKb
{% /cell %}
{% cell %}
1 MB
{% /cell %}
{% cell %}
File size limit
{% /cell %}
{% /row %}
{% /table %}

## PE Files

Enable executable file parsing, unpacking and disassembly

{% code %}
```bash {% title="transform.cfg" %}
# UPX unpacking
runUpxUnpacker=true

# Unipacker
runUnipackerOnPEFiles=true
unipackerExecutionTimeout=50
unipackerIgnorePackers=delphi,nullsoft
unipackerMaxFileSizeInKb=2048

# AutoIt unpacking
runAutoItRipper=true

# Python unpacking
runPythonUnpacker=true
pythonUnpackerTimeout=30

# Disassembly
extractDisassemblySections=true
extractDisassemblySectionsLimit=200
extractDisassemblySectionsInstructionLimit=10000

# .NET unpacking
runDe4DotForNetFiles=true
de4dotExecutionTimeout=30

# Detect it easy
enableDetectItEasy=true
enableDetectItEasyForExtractedFiles=true
detectItEasyTimeout=3
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[355] %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runUpxUnpacker
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable UPX unpacking
{% /cell %}
{% /row %}
{% /table %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[347] %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runUnipackerOnPEFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable unpacking
{% /cell %}
{% /row %}
{% row %}
{% cell %}
unipackerExecutionTimeout
{% /cell %}
{% cell %}
50 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
unipackerIgnorePackers
{% /cell %}
{% cell %}
delphi,nullsoft
{% /cell %}
{% cell %}
Comma separated list of ignored unpackers
{% /cell %}
{% /row %}
{% row %}
{% cell %}
unipackerMaxFileSizeInKb
{% /cell %}
{% cell %}
2 MB
{% /cell %}
{% cell %}
File size limit
{% /cell %}
{% /row %}
{% /table %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[344] %}
Property name
{% /cell %}
{% cell header=true colwidth=[115] %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runAutoItRipper
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable AutoItRipper, extraction of compiled AutoIt scripts
{% /cell %}
{% /row %}
{% /table %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[337] %}
Property name
{% /cell %}
{% cell header=true colwidth=[115] %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runPythonUnpacker
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable Python unpacking
{% /cell %}
{% /row %}
{% row %}
{% cell %}
pythonUnpackerTimeout
{% /cell %}
{% cell %}
30 seconds
{% /cell %}
{% cell %}
Switch to enable / disable Python unpacking, extraction of compiled Python scripts
{% /cell %}
{% /row %}
{% /table %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
extractDisassemblySections
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable disassembly
{% /cell %}
{% /row %}
{% row %}
{% cell %}
extractDisassemblySectionsLimit
{% /cell %}
{% cell %}
200
{% /cell %}
{% cell %}
Limit: the number of disassembled sections
{% /cell %}
{% /row %}
{% row %}
{% cell %}
extractDisassemblySectionsInstructionLimit
{% /cell %}
{% cell %}
10000
{% /cell %}
{% cell %}
Limit: the number of disassembled instructions
{% /cell %}
{% /row %}
{% /table %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[333] %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runDe4DotForNetFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable .NET unpacking
{% /cell %}
{% /row %}
{% row %}
{% cell %}
de4dotExecutionTimeout
{% /cell %}
{% cell %}
30 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[336] %}
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
enableDetectItEasy
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable DetectItEasy, file type and attribute detection
{% /cell %}
{% /row %}
{% row %}
{% cell %}
enableDetectItEasyForExtractedFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Enable DetectItEasy on extracted files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
detectItEasyTimeout
{% /cell %}
{% cell %}
3 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}

## Android Files

Enable Android APK parsing

{% code %}
```bash {% title="transform.cfg" %}
runAPKToolForAndroidFiles=true
apkToolExecutionTimeout=60
apkToolParseMaxFolderDepth=10
apkToolCheckMaxFiles=10000
apkToolParseMaxFiles=1000
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runAPKToolForAndroidFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable APK parsing
{% /cell %}
{% /row %}
{% row %}
{% cell %}
apkToolExecutionTimeout
{% /cell %}
{% cell %}
60 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
apkToolParseMaxFolderDepth
{% /cell %}
{% cell %}
10
{% /cell %}
{% cell %}
Limit: APK archive folder dept
{% /cell %}
{% /row %}
{% row %}
{% cell %}
apkToolCheckMaxFiles
{% /cell %}
{% cell %}
10000
{% /cell %}
{% cell %}
Limit: APK archive file count
{% /cell %}
{% /row %}
{% row %}
{% cell %}
apkToolParseMaxFiles
{% /cell %}
{% cell %}
1000
{% /cell %}
{% cell %}
Limit: Smali file count
{% /cell %}
{% /row %}
{% /table %}

## Java Files

Enable Java decompilation

{% code %}
```bash {% title="transform.cfg" %}
runCFRForJavaFiles=true
cfrExecutionTimeout=30
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runCFRForJavaFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable Java decompilation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
cfrExecutionTimeout
{% /cell %}
{% cell %}
30 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}
