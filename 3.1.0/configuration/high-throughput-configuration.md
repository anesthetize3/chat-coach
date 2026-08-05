---
type: page
title: High-Throughput Configuration
listed: true
description: 
index_title: High-Throughput Configuration
hidden: false
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
It is important to set any custom option values in the **transform.cfg** and **broker.cfg** files!
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
runHexillionOnExtractedDomains=false
runWhoisRecordLookups=false

# Disable expensive/unpredictable subtasks 
runFileDownloaders=false
runTesseractOCRForImages=false
runDe4DotForNetFiles=false
runFileVisualizer=false
```
{% /code %}

---

## Webservice Admin Settings

Log in to the sandbox using an admin user, and open the Admin Panel to change the following settings under the Configuration.

#### 1. Configure Reputation Providers (use your `MDCLOUD_API_KEY`):

{% image url="../../assets/0556ad9bca79bf442a8205f73f42ffc218a406c5.png" /%}

#### 2. Configure a short retention period for samples and scan reports (e.g. 3 days):

{% image url="../../assets/e7797ea29e4f16e8be491b57dba229c57f530983.png" /%}

#### 3. Disable Trends-related jobs that might lead to a database bottleneck (**Statistics** tab):

{% image url="../../assets/8fbe13bc3732f530f3e97f62569d6076321601da.png" /%}

#### 4. Disable other non-essential jobs (**Reports** tab):

{% image url="../../assets/506161fef3fe1bcec0cca24bb5f1a25acbc070c1.png" /%}

#### 5. Configure "Finalize finished reports with hanging subtasks" job to run "Every 2 minutes" (`Scan` tab):

{% image url="../../assets/d8c3e96aee958f28c3e6bd6802e3ff294765f22a.png" /%}
