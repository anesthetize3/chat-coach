---
type: page
title: Quick Upgrade
listed: true
description: 
index_title: Quick Upgrade
hidden: true
keywords: 
tags: 
---

Please walk through the following steps:

**Step #1 - Upload the new release archive into an empty directory.**

**Step #2 - Unzip the release archive and the fsBootstrap directory:**

*Please use the password that you received from your Customer Representative. Please adjust the x.y.z version numbers to match the downloaded file.*

{% code %}
```bash
7z x -p"PASSWORD" OPSWAT_Filescan_vx.y.z-Standalone.zip 
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

**Step #7 - Optional: Add new** **Activation Key (if you are upgrading from version 1.7.2 or earlier)**

If you are upgrading from version 1.7.2 or earlier, you need to deploy **a new Activation Key** to use Filescan.

Please use the Activation Key that you received from your OPSWAT Sales Representative, and follow the instructions on the [License Activation](license-activation.md) page.

If you used the default installation location, then you can create and copy the `licence.yml` file like this:

{% code %}
```bash
echo "ACTIVATION_KEY" > ~/license.yml
sudo cp ~/license.yml /home/filescanio/FileScanIO/fsTransform/license/
```
{% /code %}
