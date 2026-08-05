---
type: page
title: Why can’t I find the log file collection zip?
listed: true
description: 
index_title: Why can’t I find the log file collection zip?
hidden: true
keywords: 
tags: 
---

Summary

When running `collect_logs.sh`, the script finishes but the logs archive (`logs-&lt;timestamp&gt;.zip`) is missing. The console output shows:

./collect\_logs.sh: line 97: 7za: command not found

{% image url="../../assets/e143ca1cf093d25ce67b1565bdf8920edfaf0e6f.png" /%}

The log-collection script uses the `7za` command (7-Zip) to create the archive. If 7-Zip is not installed, the script cannot build the zip file.

Cause

The 7-Zip command-line tool (`7za`) is not installed on the system, so the script cannot compress the collected logs into the final zip archive.

Even though this is mentioned in the installation steps of the Sandbox application, this might have been removed in the meantime.

Resolution

1. Install 7-Zip on the Sandbox host.

Ubuntu / Debian:

sudo apt update

sudo apt install p7zip-full

RHEL / Rocky :

sudo dnf install p7zip -y

2. Re-run the log collection script:

cd /home/sandbox/sandbox

sudo ./collect\_logs.sh

3. Verify the archive was created:

ls logs-\*.zip

{% callout title="Support: " %}
If Further Assistance is required, please proceed to log a [support case or chatting with our support engineer](https://my.opswat.com/support).
{% /callout %}
