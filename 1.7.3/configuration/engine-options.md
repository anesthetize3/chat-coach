---
type: page
title: Engine Options
listed: true
description: 
index_title: Engine Options
hidden: true
keywords: 
tags: 
---

The following table outlines the most important configuration options:

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[209] %}
Option Name
{% /cell %}
{% cell header=true colwidth=[175] %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
listenServerPort
{% /cell %}
{% cell %}
22001
{% /cell %}
{% cell %}
This is the HTTP port on which the webservice will listen, if the transformer is launched in the listen mode (see "—listen")
{% /cell %}
{% /row %}
{% row %}
{% cell %}
storeResultsPath
{% /cell %}
{% cell %}
/tmp/fsResults
{% /cell %}
{% cell %}
This is where the reporting dataand samples are stored. It should have the longest retention period. The storage size can be reduced by enabling "discStorageCompression" and disabling "transformServerSaveJsonToDisc". *Note: if the transform server is used in conjunction with the broker and the broker has the transform server configured with the "callbackDeleteTaskAfterProcessing" attribute, the underlying results will be deleted after "runFileSystemCleanupRequiredAgeInSeconds" seconds automatically*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
tempStoragePath
{% /cell %}
{% cell %}
/tmp/fsTemp
{% /cell %}
{% cell %}
This is where temporary data is stored (e.g. when unpacking OOXML files). It should have a short retention period.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
taskStoragePath
{% /cell %}
{% cell %}
/tmp/fsTasks
{% /cell %}
{% cell %}
This is where temporary data is stored (e.g. when unpacking OOXML files). It should have a short retention period.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
resourceStoragePath
{% /cell %}
{% cell %}
/tmp/fsResources
{% /cell %}
{% cell %}
Stores resource data (e.g. the result of a file visualization)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
deleteArchivedTasksAndResources IfOlderThanXDays
{% /cell %}
{% cell %}
7
{% /cell %}
{% cell %}
This is the default retention period (in days) for archived tasks and resources. *Note: this does not apply to reporting data and samples stored in "storeResultsPath"*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ipStackAccessKey
{% /cell %}
{% cell %}
\<empty\>
{% /cell %}
{% cell %}
If "runIPStackLookupOnExectractedHosts" is enabled and a valid API access key is provided, the transform server will perform IP geolocation and meta-data lookup (LAT/LON, etc.) for extracted IP addresses.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
opswatReputationAPIKey
{% /cell %}
{% cell %}
\<empty\>
{% /cell %}
{% cell %}
Provide your OPSWAT MetaDefender Cloud API key here. You can only use OPSWAT reputation lookup until your daily quota has not been exceeded. *Note: If you don't have an OPSWAT account yet, please register a free account* [here](https://id.opswat.com/register?redirect=https%3A%2F%2Fmetadefender.opswat.com%2Flogin&app=appMDC0001)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
opswatReputationAPIURL
{% /cell %}
{% cell %}
[https://api.metadefender.com/v4/](https://api.metadefender.com/v4/)
{% /cell %}
{% cell %}
OPSWAT MetaDefender Cloud API url
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
Provide your OPSWAT MetaDefender Core API key here.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
metaDefenderAPIURL
{% /cell %}
{% cell %}
[https://api.metadefender.com/v4/](https://api.metadefender.com/v4/)
{% /cell %}
{% cell %}
Replace with the IP address of your OPSWAT MetaDefender Core instance. Make sure that the provided IP address can be reached from your subnet.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
proxyHost, proxyPort, proxyType, proxyScheme
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Configure your proxy server / port, if you want the transform server to perform outbound connections using a proxy server.
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
If enabled, OSINT lookups (currently: VirusTotal andClamAV, OPSWAT) will be performed in general (it is a global flag).
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
If enabled, OSINT lookups will be performed on extracted files. In order to reduce the total number of queries, it is recommended to disable this option. However, if an unlimited API key is available, it should be enabled for improved detection.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
virusTotalAPIKey
{% /cell %}
{% cell %}
\<empty\>
{% /cell %}
{% cell %}
Provide your VirusTotal API key here. If the transform server is running in the listener, the "virusTotalQueriesPerMinute" limit will be applied automatically in order to ensure even during peak processing underlying quota is not exceeded. This option needs to be adjusted based on the actual usage quota (or set to "0" to disable any limiting).
{% /cell %}
{% /row %}
{% row %}
{% cell %}
virusTotalQueriesPerMinute
{% /cell %}
{% cell %}
32
{% /cell %}
{% cell %}
This option specifies how many transform tasks will be executed in parallel. The value will be capped to the total number of CPUs based on the "transformServerLimitByAvailableProcessors" option. If the server receives a large amount of files and performance is an issue, it is recommended to increase the total number of available CPUs (e.g. by upgrading hardware) as well as adjust the pool size.
{% /cell %}
{% /row %}
{% /table %}
