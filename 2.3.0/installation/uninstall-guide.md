---
type: page
title: Uninstall Guide
listed: true
description: 
index_title: Uninstall Guide
hidden: false
keywords: 
tags: 
---

{% callout type="warning" title="Loss of data" %}
Please be aware that removing MetaDefender Sandbox will delete all configuration and data permanently! This cannot be undone!
{% /callout %}

{% callout title="Restart" %}
Please be aware that after the uninstall process finished the system must be restarted. This is mandatory for the cleanup.
{% /callout %}

Please walk through the following steps to remove MetaDefender Sandbox from your system / VM.

**Step #1 - Navigate to the installation folder**

{% code %}
```bash
cd /home/sandbox/sandbox
```
{% /code %}

**Step #2 -** **Ensure that the uninstall script is executable**

{% code %}
```bash
chmod +x uninstall.sh
```
{% /code %}

**Step #3 - Run the uninstall script as root**

{% code %}
```bash
sudo ./uninstall.sh
```
{% /code %}

**Step #4 - Manually confirm that you want to delete all Sandbox configuration and data**

{% callout title="Removing APT packages" %}
The uninstall process will not remove APT packages. They can be removed manually if not needed anymore.
{% /callout %}
