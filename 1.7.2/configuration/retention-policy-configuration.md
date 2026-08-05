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
