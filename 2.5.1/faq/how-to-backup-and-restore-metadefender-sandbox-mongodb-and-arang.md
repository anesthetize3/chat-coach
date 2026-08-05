---
type: page
title: How to Backup and Restore MetaDefender Sandbox MongoDB and ArangoDB?
listed: true
description: 
index_title: How to Backup and Restore MetaDefender Sandbox MongoDB and ArangoDB?
hidden: false
keywords: 
tags: 
---

{% callout title="Check Your Version:" %}
This article applies to all MetaDefender Sandbox releases.
{% /callout %}

## Overview

This article explains how to back up and restore the MetaDefender Sandbox MongoDB and ArangoDB database.

## **Backup procedure**

**Preferred method:** Create a full system snapshot.

**Alternative method:** Manually back up the `/data` folder, which contains both **MongoDB** and **ArangoDB** databases.

#### Steps:

1. **Stop the sandbox service:**

```
sudo service sandbox stop
```

2. **Back up the** `/data` **folder:**

```
sudo cp -R /data/* /YOUR/BACKUP/FOLDER
```

3. **Restart the sandbox service:**

```
sudo service sandbox start
```

{% callout type="warning" title="Note:" %}
It is strongly recommended to store the backup on a separate disk or network share to safeguard against potential disk failures.
{% /callout %}

## **Restore procedure**

1. **Stop the sandbox service:**

```
sudo service sandbox stop
```

2. **Remove existing database files:**

```
sudo rm -rf /data/db/fsio/*
sudo rm -rf /data/graphdb/fsio/*
```

3. **Restore the backup to** `/data`**:**

```
sudo cp -R /YOUR/BACKUP/FOLDER/* /data/
```

4. **Start the sandbox service:**

```
sudo service sandbox start
```

{% callout title="Support:" %}
If **Further Assistance** is required, please proceed to log a [support case or chatting with our support engineer](https://my.opswat.com/support).
{% /callout %}
