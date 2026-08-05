---
type: page
title: Upgrade
listed: true
description: 
index_title: Upgrade
hidden: false
keywords: 
tags: 
---

{% callout type="warning" title="Check System Requirements" %}
Before starting the installation, please make sure that your target system meets the [Technical Requirements](technical-requirements.md) and the installation is **performed by a person with basic Linux skills**.

If your target system is currently running **Ubuntu 20.04**, then please upgrade to **Ubuntu 22.04 LTS** following the [Operating System Upgrade](quick-upgrade/operating-system-upgrade.md) guide.
{% /callout %}

{% callout type="warning" title="Warning" %}
This page only refers to product installation with a **stable Internet connection**!

For **offline installations**, please follow the [Offline Installation](offline-installation.md) guide instead!
{% /callout %}

Please walk through the following steps:

**Step #1 -** **Download and copy the release archive**

Download the release archive from [https://my.opswat.com/portal/products](https://my.opswat.com/portal/products)

Copy the release archive to a folder on the Sandbox server, e.g. your home folder

**Step #2 - Unpack the release archive:**

{% callout title="Info" %}
Please use the **password** that you received from your OPSWAT Sales Representative!

Please adjust the x.y.z **version numbers** to match the downloaded filename.
{% /callout %}

{% code %}
```bash
7z x -aoa -p"PASSWORD" MetaDefender_Sandbox_vx.y.z-Standalone.zip
```
{% /code %}

**Step #3 - Move to the installation folder:**

{% code %}
```bash
cd sandbox-installer
```
{% /code %}

**Step #4 - (Optional) Configure** `install.cfg` **to specify a custom user name and installation path**

There is no need to modify `install.cfg`  if you used the default options during the original installation.

More details available in [Installation Options](quick-installation/installation-options.md).

{% callout type="warning" title="Warning" %}
If you configured **a custom user name and installation path** during your original installation, please configure the **same values**, otherwise the installer cannot find the existing installation!
{% /callout %}

{% callout title="Info" %}
If you use the default options, the existing **filescanio** user will be automatically renamed to **sandbox**.

If you have an existing installation at the default directory: **/home/filescanio/FileScanIO** then this directory will be moved \& renamed to **/home/sandbox/sandbox**.
{% /callout %}

**Step #5 - Run the install shell script**

Note that this operation can take up to 20-30 minutes (depending on available network bandwidth).

{% code %}
```bash
sudo ./install.sh
```
{% /code %}

All components should restart  automatically after the upgrade is completed.

**Step #6 - (Optional) Troubleshooting if the Sandbox service failed to** **restart**

Verify the status of the `sandbox` service and if the running docker container are healthy:

{% code %}
```bash
sudo service sandbox status
sudo docker ps
```
{% /code %}

The `sblog` bash command can be used to check the application logs for different system components.

This command is available to all users (but might require sudo privileges):

{% code %}
```bash
# Show logs from the transform component
sblog 
# Show logs from the broker component
sblog -b
```
{% /code %}
