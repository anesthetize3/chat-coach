---
type: page
title: Jobs
listed: true
description: 
index_title: Jobs
hidden: true
keywords: 
tags: 
---

In the **Admin Panel \> Setting \> Configurations \> Jobs** settings, jobs can be parameterized, such as the number and timing of retries, or the maximum number of database queries running in parallel.

{% image url="https://uploads.developerhub.io/prod/XX2D/hnvhy1vl6xhpfuo759pyge0q1i9vaxce0us4uu7frwyxylixvrx1mj7x20b34dgt.png" /%}

Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[363] %}
Field
{% /cell %}
{% cell header=true colwidth=[197] %}
Description
{% /cell %}
{% cell header=true %}
Value
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`JOBS_PARALLEL_DB_QUERIES_LIMIT`
{% /cell %}
{% cell %}
The maximum number of database queries that can occur concurrently.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`JOB_MEMORY_LIMIT`
{% /cell %}
{% cell %}
Stop the job if it exceeds this memory limit.
{% /cell %}
{% cell %}
MB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`JOBS_QUERIES_INTERVAL`
{% /cell %}
{% cell %}
Defines the interval, in seconds, at which the system queries the jobs.
{% /cell %}
{% cell %}
sec (float)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MIN_SYSTEM_AVAILABLE_MEMORY_THRESHOLD`
{% /cell %}
{% cell %}
If system has less available memory left than this value, app will start stopping all jobs.
{% /cell %}
{% cell %}
MB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_BROKER_STUCK_RETRY_MAX_UPLOAD_SIZE`
{% /cell %}
{% cell %}
If the upload size exceeds this value, retries are not performed if the broker is stuck.
{% /cell %}
{% cell %}
MB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`QUEUED_SCAN_CHANGE_PRIORITY_TIMEOUT`
{% /cell %}
{% cell %}
The time before the priority of scans waiting in the queue is increased.
{% /cell %}
{% cell %}
sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`QUEUED_SCAN_CANCEL_TIMEOUT`
{% /cell %}
{% cell %}
The time before a scan waiting in the queue is canceled.
{% /cell %}
{% cell %}
sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`CREATE_SCANS_ABOVE_LIMIT_FACTOR`
{% /cell %}
{% cell %}
How many scans users are allowed to add above the queue limit, relative to this limit. (value is in %)
{% /cell %}
{% cell %}
from 0 to 1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`MOVE_SCAN_KEEP_FREE_RATIO`
{% /cell %}
{% cell %}
Determines the amount of free space that remains in the target queue when moving items between queues.  Set to 1 to disable changing scans priority.
{% /cell %}
{% cell %}
from 0 to 1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`QUICK_RETRY_MAX_COUNT`
{% /cell %}
{% cell %}
Max amount of quick retries due to failed report. Min of it or `TASKS_QUEUE_JOB_RETRY_LIMIT` (broker rescans) is used.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RESCAN_MAX_COUNT`
{% /cell %}
{% cell %}
Amount of delayed rescan attempts to make for failed reports. Set to 0 to disable rescans.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RESCAN_MIN_AGE_HOURS`
{% /cell %}
{% cell %}
The minimum age, in hours, before a rescan can be initiated for a report.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`REPORT_INTERRUPT_TIMEOUT`
{% /cell %}
{% cell %}
Defines the timeout period, in seconds, after which a report generation process will be interrupted if it takes too long to complete.
{% /cell %}
{% cell %}
sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_REQUEST_FAILED_RETRY_WAIT`
{% /cell %}
{% cell %}
Specifies the time, in seconds, to wait before retrying a failed scan request.
{% /cell %}
{% cell %}
sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_BROKER_STUCK_RETRY_WAIT_1`
{% /cell %}
{% cell %}
Defines the initial time, in seconds, to wait before retrying a scan request if the broker is stuck
{% /cell %}
{% cell %}
sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_BROKER_STUCK_RETRY_WAIT_2`
{% /cell %}
{% cell %}
Defines the time, in seconds, to wait before retrying a scan request if the broker is stuck after the second tries is failed.
{% /cell %}
{% cell %}
sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_BROKER_STUCK_RETRY_WAIT_3`
{% /cell %}
{% cell %}
Defines the time, in seconds, to wait before retrying a scan request if the broker is stuck after the third tries is failed.
{% /cell %}
{% cell %}
sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`RESCAN_QUOTA_FACTOR`
{% /cell %}
{% cell %}
Allow only certain part of queue to be occupied by rescans.
{% /cell %}
{% cell %}
from 0 to 1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_MAX_PRIORITY_JOBS_LIMIT`
{% /cell %}
{% cell %}
Specifies the maximum number of jobs allowed with the highest priority in the scan queue.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_MEDIUM_PRIORITY_JOBS_LIMIT`
{% /cell %}
{% cell %}
Specifies the maximum number of jobs allowed with medium priority in the scan queue.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_LOW_PRIORITY_JOBS_LIMIT`
{% /cell %}
{% cell %}
Specifies the maximum number of jobs allowed with low priority in the scan queue.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SCAN_LEAST_PRIORITY_JOBS_LIMIT`
{% /cell %}
{% cell %}
Specifies the minimum number of jobs allowed with the lowest priority in the scan queue.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`TASKS_QUEUE_JOB_TIMEOUT`
{% /cell %}
{% cell %}
Time limit for arq jobs from start till job is cancelled.
{% /cell %}
{% cell %}
sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
REPORT\_FORMAT\_STRINGS\_LIMIT
{% /cell %}
{% cell %}
Only include this amount of extracted strings into HTML/PDF report
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
REPORT\_FORMAT\_STRINGS\_MODE
{% /cell %}
{% cell %}
What strings to include into HTML/PDF report. `Prefer interesting`  means - include interesting strings first, and than other strings till limit is reached
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
REPORT\_FORMAT\_HISTORY\_CLEANUP\_TIMEOUT
{% /cell %}
{% cell %}
Interval to cleanup exporting reports history. Also affected by interval of launching cleanup job
{% /cell %}
{% cell %}
min
{% /cell %}
{% /row %}
{% /table %}
