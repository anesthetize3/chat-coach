---
type: page
title: Requirements
listed: true
description: 
index_title: Requirements
hidden: false
keywords: 
tags: 
---

**Processing Power**

In general, we recommend at least 8 vCPUs and 32GB of RAM. Some stress tests have found the following EC2 instance types to be adequate:

- t3a.2xlarge for up to 5000 files/day and 1-5 users
- c4.4xlarge for up to 10000 files/day and 5-10 users
- c4.8xlarge for up to 25000 files/day and 10+ users

**Disc Storage**

The minimum SSD storage to get an instance up and running is 32 GB. However, while the system is in parts already configured to automatically delete local binaries (see “Retention Policy Configuration” in the User Guide), the hard disc will eventually run full. It is thus recommended to configure the webservice to use a S3 bucket and potentially move the database storage (/data/db and /data/graphdb) to an additional, external storage. Please refer to the “S3 Bucket Configuration” section of the “User Guide”.
