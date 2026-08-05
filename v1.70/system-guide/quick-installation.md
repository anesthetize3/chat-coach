---
type: page
title: Quick Installation
listed: false
description: 
index_title: Quick Installation
hidden: false
keywords: 
tags: 
---

Please walk through the following steps:

**Step #1 - Create a new user that will own all the release files and run the appliance**

sudo adduser filescanio

**Step #2 - Unpack the fsBootstrap archive to a folder, eg: your home folder**

`sudo apt-get update`

`sudo apt-get install p7zip-full -y`

`7z x -p<password> fsBootstrap.zip -ofsBootstrap`

`rm fsBootstrap.zip`

*Note: as all archives use AES encryption, 7zip is required to unzip. Please use the password as provided as part of your release notes*

**Step #3 - Ensure that the embedded installation scripts are executable and have the unix format:**

`cd fsBootstrap`

`chmod +x *.sh`

`sudo apt-get install dos2unix -y`

`dos2unix`\*

**Step #4 - Configure bootstrap.cfg and carefully set all options**

**Step #5 - Move the FileScanIO.zip archive into the current folder (fsBootstrap)**

`mv ../FileScanIO.zip .`

**Step #6 - Run the bootstrap shell script**

`sudo ./bootstrap.sh`

**Step #7 - Configure the transform and broker components to your liking**

**Step #8 - Access the webserver (localhost, port 443) and setup the initial admin**

**Step #9 - Optional: run the transform and/or broker processes, if not running already**

`sudo service fsio start`

`sudo service fsiobroker star`

**Step #10 -** Check the output to ensure that initialization succeeded:

`fsiolog`

`fsiologbroker`

**Step #11 - Run the fsFingerprint.jar (distributed with the release archive)**

Run this fingerprinting tool on your host machine to generate a unique fingerprint of your deployment host environment. Send the fingerprint contents or binary file to **!!!support@filescan.io!!!** and you will receive a license key file shortly. The license key will be needed after the deployment.

`java -jar fsFingerprint.jar`

**Step #12 - Put your license key (see Generate License Key) into the FileScanIO/fsTransform folder.**

It will be picked up and loaded automatically.

Example:

`May 01 15:44:12 filescanio18 fsio[27171]: main 2020-05-01 15:44:12,652 INFO 234 [fsLogger] - <Trying to start server on localhost: 22001>`

`May 01 15:44:12 filescanio18 fsio[27171]: main 2020-05-01 15:44:12,663 INFO 236 [fsLogger] - <Server started successfully.>`

`May 01 15:44:12 filescanio18 fsio[27171]: main 2020-05-01 15:44:12,664 INFO 242 [fsLogger] - <Server maintenance thread started>`

*Note: please refer to the API top level menu at the webservice to learn how files may be sent to the system for automated processing. For custom integrations (eg: email), please reach out to support.*
