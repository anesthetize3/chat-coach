---
type: page
title: Quick Upgrade
listed: true
description: 
index_title: Quick Upgrade
hidden: false
keywords: 
tags: 
---

Please walk through the following steps:

**Step #1 -** **Upload the new release archive** into the fsBootstrap folder created during installation

**Step #2 - Configure upgrade.cfg and carefully set all options.**

*Note: leave settings blank if you want to keep the values from your original installation. Please ensure that FileScanIOWebservice\_IsCommunityDeploy is disabled for the standalone edition*

**Step #3 - Run the upgrade shell script**

`sudo ./upgrade.sh`

All components should automatically restart after the upgrade completed, if they were running when the upgrade process started. If this was not the case, please start all services:

`sudo service fsiobroker start`

`sudo service fsio start`

`sudo service fsioweb start`
