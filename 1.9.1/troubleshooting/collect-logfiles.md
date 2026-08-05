---
type: page
title: Collect logfiles
listed: true
description: 
index_title: Collect logfiles
hidden: false
keywords: 
tags: 
---

If you have some issue with your system, logs can help to find out what went wrong. You can collect `webservice` , `fsBroker`  and `fsTransform`  logs automatically using a helper script.

Navigate to the `fsBootstrap`  folder where you installed the product and locate the `collect_logs.sh`  script. Make sure you have the correct rights to run the script.

{% callout type="warning" title="Warning" %}
If you are facing an ongoing issue and you would like to restart the webservice, it is highly recommended to run `collect_logs.sh` **before restarting the webservice!**

Otherwise the logs from the currently running Docker containers would be lost.
{% /callout %}

{% code %}
```bash
cd ~/fsBootstrap
chmod +x collect_logs.sh
sudo ./collect_logs.sh
```
{% /code %}

The script might take a few minutes to complete and it will output some information about the collected log files, for example:

{% code %}
```bash
Collecting OPSWAT Filescan log files...
        - Collected 40 log files from fsBroker
        - Collected 44 log files from fsTransform
        - Collected 2 log files from nginx
        - Collected 1 log files from autorestart service
        - Collected 14 log files from Docker containers
Success! Logs archived in /home/opswat/fsBootstrap/fslogs-230623_134130.zip
Exit...
```
{% /code %}

The output shows the path to the ZIP file that contains the collected logs. Note that the file can be large (a few hundred megabytes).

{% callout type="warning" title="Important!" %}
This is only available from version 1.8.0
{% /callout %}
