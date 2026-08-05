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

Please walk through the following steps:

**Step #1 - Upload the new release archive into an empty directory.**

**Step #2 - Unzip the release archive and the fsBootstrap directory:**

*Please use the password that you received from your Customer Representative. Please adjust the x.y.z version numbers to match the downloaded file.*

{% code %}
```bash
7z x -p"PASSWORD" MetaDefender_Sandbox_vx.y.z-Standalone.zip 
7z x fsBootstrap.zip -ofsBootstrap 
rm fsBootstrap.zip
```
{% /code %}

**Step #3 - Ensure that the embedded installation scripts are executable and have the unix format:**

{% code %}
```bash
cd fsBootstrap 
chmod +x *.sh 
dos2unix *
```
{% /code %}

**Step #4 - Configure upgrade.cfg and carefully set all options.**

*Note: leave settings blank if you want to keep the values from your original installation.*

**Step #5 - Move the FileScanIO.zip archive into the current folder (fsBootstrap)**

{% code %}
```bash
mv ../FileScanIO.zip .
```
{% /code %}

**Step #6 - Run the upgrade shell script**

{% code %}
```bash
sudo ./upgrade.sh
```
{% /code %}

All components should automatically restart after the upgrade completed, if they were running when the upgrade process started. If this was not the case, please start all services:

{% code %}
```bash
sudo service fsiobroker start 
sudo service fsio start 
sudo service fsioweb start
```
{% /code %}
