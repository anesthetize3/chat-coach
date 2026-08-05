---
type: page
title: Quick Installation
listed: true
description: 
index_title: Quick Installation
hidden: false
keywords: 
tags: 
---

Please walk through the following steps:

**Step #1 - Create a new user that will own all the release files and run the appliance**

{% code %}
```bash
sudo adduser filescanio
```
{% /code %}

**Step #2 - Download and unpack the release archive to a folder, e.g.: your home folder**

Install 7zip:

{% code %}
```bash
sudo apt-get update
sudo apt-get install p7zip-full -y
```
{% /code %}

Download the release archive from [https://my.opswat.com/portal/products](https://my.opswat.com/portal/products)

*Note that the release archive is password protected and needs to be unpacked.* *Please use the* ***password*** *that you received from your Customer Representative. Please adjust the x.y.z* ***version numbers*** *to match the downloaded file.*

{% code %}
```bash
7z x -p"PASSWORD" OPSWAT_FileScan_vx.y.z-Standalone.zip
7z x fsBootstrap.zip -ofsBootstrap
rm fsBootstrap.zip
```
{% /code %}

**Step #3 - Ensure that the embedded installation scripts are executable and have the unix format:**

{% code %}
```bash
cd fsBootstrap
chmod +x *.sh
sudo apt-get install dos2unix -y
dos2unix *
```
{% /code %}

#### **Step #4 - Configure bootstrap.cfg and carefully set all options**

**Step #5 - Move the FileScanIO.zip archive into the current folder (fsBootstrap)**

{% code %}
```bash
mv ../FileScanIO.zip .
```
{% /code %}

**Step #6 - Run the bootstrap shell script**

{% code %}
```bash
sudo ./bootstrap.sh
```
{% /code %}

**Step #7 - Configure the transform and broker components to your liking**

**Step #8 - Access the webserver (localhost, port 443) and setup the initial admin**

**Step #9 - Optional: run the transform and/or broker processes, if not running already**

{% code %}
```bash
sudo service fsio start
sudo service fsiobroker start
```
{% /code %}

**Step #10 -** **Check the output to ensure that initialization succeeded**:

{% code %}
```bash
fsiolog
fsiologbroker
```
{% /code %}

**Step #11 - Run the fsFingerprint.jar (distributed with the release archive)**

Run this fingerprinting tool on your host machine to generate a unique fingerprint of your deployment host environment.

{% code %}
```bash
cd .. 
java -jar fsFingerprint.jar
```
{% /code %}

Upload the fingerprint contents or binary file via [https://my.opswat.com](https://my.opswat.com), using 'Upload Large File' from the menu in the top right corner:

{% image url="https://uploads.developerhub.io/prod/XX2D/x37kxl62xhwzf9dxgy6w45vedxya63dant2b27r8t9unf844tcetatwcbgnf9357.png" /%}

You will receive a license key file shortly. The license key will be needed after the deployment.

**Step #12 - Put your license key (see Generate License Key) into the FileScanIO/fsTransform folder.**

It will be picked up and loaded automatically.

Example:

```
May 01 15:44:12 filescanio18 fsio[27171]: main 2020-05-01 15:44:12,652 INFO 234 [fsLogger] - <Trying to start server on localhost: 22001>

May 01 15:44:12 filescanio18 fsio[27171]: main 2020-05-01 15:44:12,663 INFO 236 [fsLogger] - <Server started successfully.>

May 01 15:44:12 filescanio18 fsio[27171]: main 2020-05-01 15:44:12,664 INFO 242 [fsLogger] - <Server maintenance thread started>
```

*Note: please refer to the API top level menu at the webservice to learn how files may be sent to the system for automated processing. For custom integrations (eg: email), please reach out to support.*

**Important notes to air-gapped systems**

- Air-gapped systems will only receive updated features (like YARA) when installed and upgraded with an active internet connection. We recommend moving the system into a DMZ during these windows.
- All third-party integrations (e.g. Reputation API, geolocation/WHOIS lookup) require an internet connection.
- The "File download" feature are disabled in air-gapped environments.
