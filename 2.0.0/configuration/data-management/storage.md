---
type: page
title: Storage
listed: true
description: 
index_title: Storage
hidden: false
keywords: 
tags: 
---

These configurations relate to storage settings, particularly for managing files and data within a system.

These configurations outline how files are managed and stored within the system, specifying an optional storage provider (Amazon S3), access credentials, cleanup criteria, and the specific location and container (bucket) where files are stored.

The location of the ***Storage*** settings are **Admin Panel \> Settings \> [Configurations](https://www.filescan.io/admin/settings/config) \> Storage.**

{% image url="https://uploads.developerhub.io/prod/XX2D/i5zc0qtrq5ewmzazwpgcw9zpk3hq4j4nve1mqywjyez2rpbhkq71c7r3m5m8bc44.png" %}
Screenshot of Configuration page of MetaDefender Sandbox
{% /image %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[299] %}
**Field**
{% /cell %}
{% cell header=true %}
**Description**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`DEFAULT_FILE_MANAGER`
{% /cell %}
{% cell %}
This setting specifies the default file manager used for storing and handling files.

The default file manager is "local". By default, any sample submitted to the webservice is stored locally at: `/srv/backend/src/storage/files/*`

If disk space is limited, it is recommended to configure the Sandbox webservice to use an AWS S3 Bucket (with an appropriate lifecycle policy). In this case, this value should be set to "s3".
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`STORAGE_CLEAN_AGE_IN_HOURS`
{% /cell %}
{% cell %}
It determines how long files are retained in storage before they are considered eligible for cleanup. In this instance, files older than 24 hours are flagged for potential removal, ensuring storage space is efficiently managed.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`S3_ACCESS_KEY_ID`
{% /cell %}
{% cell %}
Authentication mechanism for accessing the S3 service. It functions like a username, providing access to the specified S3 bucket.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`S3_SECRET_ACCESS_KEY`
{% /cell %}
{% cell %}
Similar to a password, this key is used in combination with the access key ID to authenticate access to the S3 service securely.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`S3_REGION`
{% /cell %}
{% cell %}
The geographical region where the S3 bucket is located. Each region represents a separate geographic area where Amazon's data centres are situated. In this case, it's set to "eu-central-1," indicating the European Union (Frankfurt) region.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`S3_BUCKET_NAME`
{% /cell %}
{% cell %}
Name of the specific S3 bucket where files are stored. In this example, the bucket name is "filescanio-community".
{% /cell %}
{% /row %}
{% /table %}
