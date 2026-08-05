---
type: page
title: Failed upgrade to 3.0 from earlier versions
listed: true
description: 
index_title: Failed upgrade to 3.0 from earlier versions
hidden: false
keywords: 
tags: 
---

**Upgrading directly** from versions prior to 2.5.0 to 3.0.0 is **not supported**. Skipping version 2.5.x may result in a successful installation, but Sandbox will become inoperable. Consequences include:

- Scan tasks may fail with unexpected errors.
- Transform may fail to start due to a SQL error.

**Recommended Upgrade Path:** First upgrade to **2.5.1**, then proceed to **3.0.0**.

## How to troubleshoot

The recommended and safest solution is to **follow the supported upgrade path** and run the installers in the correct order.

**If version 2.5.x was skipped and the system is already in a broken state**, the issue can be mitigated by following the steps below.

#### 1. Stop the Sandbox service

Stop the Sandbox service before making any changes.

{% code %}
```bash {% title="Stop Sandbox" %}
sudo service sandbox stop
```
{% /code %}

---

#### 2. Remove old update files

Remove leftover update and database files that prevent Sandbox from starting correctly.

{% code %}
```bash {% title="Remove leftover files" %}
sudo rm -rf /data/db/sandbox/transform/sqlite 
sudo rm -rf /home/sandbox/sandbox/transform/storage/update
```
{% /code %}

---

#### 3. Re-run the 3.0.0 installer

After the cleanup is complete, run the **3.0.0 installer again** as you normally would.

Once the installation finishes, the Sandbox services should start correctly, and file scanning should be restored.
