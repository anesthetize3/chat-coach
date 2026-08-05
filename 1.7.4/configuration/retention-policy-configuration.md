---
type: page
title: Retention Policy Configuration
listed: true
description: 
index_title: Retention Policy Configuration
hidden: true
keywords: 
tags: 
---

## Configuration on the Admin panel

You can configure the retention under the Webservice Admin (UX) panel as well.

For that click on the user icon on the top right corner:

{% image url="https://uploads.developerhub.io/prod/XX2D/91zv2lj62a8me0848mgcmampuqf04kgiogs609rn05apa0p2e4cw61ndvc779ctj.png" /%}

Select "Admin panel", then select "Settings" on the top left:

{% image url="https://uploads.developerhub.io/prod/XX2D/qfnpg7gkomukutsw28u52rd2rjwn4hzbonw01napr8sfblhuaan8ya3wslgb9qw5.png" /%}

Select configuration:

{% image url="https://uploads.developerhub.io/prod/XX2D/eed31hf5mikceex133c05q71t0rcswpdr2zd4inf29slpe54a6ir7w0lust3gzqr.png" /%}

Under the Retention tab you can set retention policy:

{% image url="https://uploads.developerhub.io/prod/XX2D/rrq9fk8ffk8iqdym517khi6cpj7izha69290pvr1jxcghg66j9gq5nu34irfjclt.png" /%}

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
