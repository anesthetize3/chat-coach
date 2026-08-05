---
type: page
title: Retention Policy Configuration
listed: true
description: 
index_title: Retention Policy Configuration
hidden: false
keywords: 
tags: 
---

## Configuration on the Admin panel

You can configure the retention under the Webservice Admin (UX) panel as well.

For that click on the user icon on the top right corner and select "**Admin**" panel:

{% image url="https://uploads.developerhub.io/prod/XX2D/2hb28t48iddjmoe4r2m0nz7h3uxttw9sf1hwbyrehw6f89g5pp9ftenro9k9bo3v.png" /%}

Then select "**Settings**" in the middle:

{% image url="https://uploads.developerhub.io/prod/XX2D/sc1o2mnicivrtczg6suecathaifb3i0ddlg1yf6jdq3puzfcvkubslgiaj1xvmpt.png" /%}

Select "**Configuration**":

{% image url="https://uploads.developerhub.io/prod/XX2D/xhi4ybb8sr3ci5l97zpauk51rh6ljplrqr65k9tefweklobh70y5eqqsy4nplpab.png" /%}

Under the "**Retention**" tab you can set retention policy:

{% image url="https://uploads.developerhub.io/prod/XX2D/dbzufoxxuf988r1gsqx1nno5duspuiac94ea86pvmo5g0t0qn5ko444hy6tqpikk.jpeg" /%}

By default, retention is enabled and set to 365 days.

### [Configuration options](https://docs.opswat.com/filescan/configuration/ocm#configuration-options)

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[287] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RETENTION_ENABLED`
{% /cell %}
{% cell %}
Enable or disable data retention
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RETENTION_DELETE_REPORT`
{% /cell %}
{% cell %}
Enable or disable deleting retention report
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RETENTION_PERIOD_MALICIOUS`
{% /cell %}
{% cell %}
Set retention period for malicious files  (the value is in days, set to 0 for indefinite storage)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RETENTION_PERIOD_SUSPICIOUS`
{% /cell %}
{% cell %}
Set retention period for suspicious files  (the value is in days, set to 0 for indefinite storage)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RETENTION_PERIOD_INFORMATIONAL`
{% /cell %}
{% cell %}
Set retention period for informational files  (the value is in days, set to 0 for indefinite storage)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RETENTION_PERIOD_UNKNOWN`
{% /cell %}
{% cell %}
Set retention period for unknown files  (the value is in days, set to 0 for indefinite storage)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RETENTION_PERIOD_BENIGN`
{% /cell %}
{% cell %}
Set retention period for benign files  (the value is in days, set to 0 for indefinite storage)
{% /cell %}
{% /row %}
{% /table %}

## Backend configuration

By default, the system is designed to clean up locally stored results/received samples and other temporary files. These cleanup operations are performed either upon starting up the service (single-pass) or on continuous short-cycle intervals in a background process. To enable regular cleanup during the server mode, make sure the following options are enabled:

{% table layout="auto" %}
{% row %}
{% cell header=true %}
File
{% /cell %}
{% cell header=true %}
Option Name
{% /cell %}
{% /row %}
{% row %}
{% cell %}
broker.cfg
{% /cell %}
{% cell %}
runFileSystemCleanup
{% /cell %}
{% /row %}
{% row %}
{% cell %}
transform.cfg
{% /cell %}
{% cell %}
runFileSystemCleanup
{% /cell %}
{% /row %}
{% /table %}

---

By default, the following retention period is applied (see “Retention Policy” sections in both broker.cfg and transform.cfg  files):

{% table layout="auto" %}
{% row %}
{% cell header=true %}
File
{% /cell %}
{% cell header=true %}
Option Name
{% /cell %}
{% cell header=true %}
Retention Period in minutes (days)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Analysis Results
{% /cell %}
{% cell %}
deleteResultsPathArtifactsOlderThanXMinutes
{% /cell %}
{% cell %}
1440 (1 day)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sample Files
{% /cell %}
{% cell %}
deleteStoredSamplesOlderThanXMinutes
{% /cell %}
{% cell %}
1440 (1 day)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Temp Files
{% /cell %}
{% cell %}
deleteTempFilesOlderThanXMinutes
{% /cell %}
{% cell %}
1440 (1 day)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Queued Files
{% /cell %}
{% cell %}
deleteQueueFilesIfOlderThanXMinutes
{% /cell %}
{% cell %}
1440 (1 day)
{% /cell %}
{% /row %}
{% /table %}

*Note: the queued files are only cleaned up if automatic re-queue is disabled (by default). To change this behavior, configure the requeuePendingTasksFromPreviousTermination option.*
