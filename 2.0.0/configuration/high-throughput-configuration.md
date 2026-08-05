---
type: page
title: High-Throughput Configuration
listed: true
description: 
index_title: High-Throughput Configuration
hidden: true
keywords: 
tags: 
---

To achieve the maximum possible throughput on a single server, make sure to deploy **MetaDefender Sandbox** (previously known as OPSWAT Filescan Sandbox) on a powerful instance:

- 32 vCPUs (preferably 64 vCPUs)
- 128 GB RAM (preferably 256 GB)
- 500 GB SSD (preferably 1 TB)

*The overall throughput of such a server may eclipse the default maximum limit of 25000 scans/day, and it primarily depends on the sample set. The processing time for individual samples can range from 5 seconds to 2 minutes (depending on the complexity of the sample).*

The following special settings can be used to optimize the throughput when the main objective is **quickly obtaining an accurate verdict** for a sample, but deeper analysis is **not required**.

{% callout type="warning" title="Warning" %}
It is important to set any custom option values in the **.custom properties file** for `transform` and `broker`!

If you make any changes in the default properties file, then the upgrade process will "reset" those changes. But the .custom property files remain untouched during the upgrade process!
{% /callout %}

---

## Transform Configuration

Please add the following settings in `/home/sandbox/sandbox/transform.cfg`:

{% code %}
```bash
# Disable archiving files
archiveTasksAndResourcesIfOlderThanXMinutes=0
deleteArchivedTasksAndResourcesIfOlderThanXMinutes=0

# Delete files older than 60 minutes
deleteTasksAndResourcesIfOlderThanXMinutes=60
deleteResultsPathArtifactsOlderThanXMinutes=60
deleteEmptyDirectoriesIfOlderThanXMinutes=60
deleteTempFilesOlderThanXMinutes=60

# OSINT settings
runOSINTLookups=true
runExtendedOSINTLookups=true
runOSINTLookupsOnExtractedFiles=true
runOSINTLookupsRequireMinProcessingPriority=0
enableOpswatReputationAPI=true
opswatReputationAPIKey=<YOUR MDCLOUD APIKEY>

enableVirusTotalLookups=false
enableClamscanLookup=false
runIPStackLookupOnExectractedHosts=false
runIPStackOnDomainResolvedIPs=false
runHexillionOnExtractedDomains=false
runWhoisRecordLookups=false

# Disable expensive/unpredictable subtasks 
runFileDownloaders=false
runTesseractOCRForImages=false
runDe4DotForNetFiles=false
runFileVisualizer=false

requeuePendingTasksFromPreviousTermination=false
```
{% /code %}

---

## Broker Configuration

Please add the following settings in `/home/sandbox/sandbox/broker.cfg`:

{% code %}
```bash
# Disable download of missing resources
downloadMissingIdentifiers=false
```
{% /code %}

---

## Webservice Admin Settings

Log in to the sandbox using an admin user, and open the Admin Panel to change the following settings.

#### 1. Configure Reputation Providers (use your `MDCLOUD_API_KEY`):

{% image url="https://uploads.developerhub.io/prod/XX2D/5rab3toaszcuygv7k8daer1i1cgeot7lblaaxwmz966wqamjdnxujk50ucizeb96.png" /%}

#### 2. Configure a short retention period for samples and scan reports (e.g. 3 days):

{% image url="https://uploads.developerhub.io/prod/XX2D/jmijqqgyr9vc07ai01taamqc0eohleg2sg087b9l627lflvr0fs4skusbgceir1i.png" /%}

#### 3. Disable Trends-related jobs that might lead to a database bottleneck (**Statistics** tab):

{% image url="https://uploads.developerhub.io/prod/XX2D/kd62i06h5glagoxtmsvorik4rm6wm8kav0lgw1yf6i800vf3rijr54rw3fpmp40t.png" /%}

#### 4. Disable other non-essential jobs (**Reports** tab):

{% image url="https://uploads.developerhub.io/prod/XX2D/gr3t2ajf1wdo1bshj9z64gs2zgcqzhyjclziyd3fiip2vd51943xt93im84vj0cr.png" /%}

#### 5. Configure "Finalize finished reports with hanging subtasks" job to run "Every 2 minutes" (`Scan` tab):

{% image url="https://uploads.developerhub.io/prod/XX2D/4isf8mia70xem3dd4qyu0h74p5bon724oy56bo1xb9uly4tq1r7o8wa998zyskpw.png" /%}
