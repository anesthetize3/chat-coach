---
type: page
title: Automated Data Deletion
listed: false
description: 
index_title: Automated Data Deletion
hidden: true
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
broker.properties
{% /cell %}
{% cell %}
runFileSystemCleanup
{% /cell %}
{% /row %}
{% row %}
{% cell %}
transform.properties
{% /cell %}
{% cell %}
runFileSystemCleanup
{% /cell %}
{% /row %}
{% /table %}

---

By default, the following retention period is applied (see “Retention Policy” sections in both the broker and transform server properties files):

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
deleteResultsPathArtifactsOlderThanXMinutes
{% /cell %}
{% cell %}
10080 (7 days)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Temp Files
{% /cell %}
{% cell %}
deleteResultsPathArtifactsOlderThanXMinutes
{% /cell %}
{% cell %}
2880 (2 days)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Queued Files
{% /cell %}
{% cell %}
deleteResultsPathArtifactsOlderThanXMinutes
{% /cell %}
{% cell %}
1440 (1 day)
{% /cell %}
{% /row %}
{% /table %}

*Note: the queued files are only cleaned up if automatic re-queue is disabled (not by default). The automatic re-queue feature is designed to allow a downtime of the broker without losing previously submitted files from being processed. To change this behavior, configure the requeuePendingTasksFromPreviousTermination option.*
