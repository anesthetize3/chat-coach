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

{% callout type="warning" title="Warning" %}
Before starting the installation, please make sure that your target system meets the [Technical Requirements](technical-requirements.md) and the installation is performed by a person with basic Linux skills (mainly with Ubuntu experience).
{% /callout %}

Please walk through the following steps. If you encounter any issues during installation, refer to our [Troubleshooting Guide.](https://docs.opswat.com/filescan/troubleshooting)

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

Note that the release archive is password protected and needs to be unpacked.

{% callout type="warning" title="Warning" %}
Please use the **password** that you received from your OPSWAT Sales Representative! Please adjust the x.y.z **version numbers** to match the downloaded filename!
{% /callout %}

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
sudo apt-get install dos2unix -y
dos2unix *
```
{% /code %}

**Step #4 - Edit bootstrap.cfg to enable optional features (e.g. S3 bucket storage, E-Mail).**

*Note: Default settings work fine for standard deploys and all features can be configured post installation.*

**Step #5 - Move the FileScanIO.zip archive into the current folder (fsBootstrap)**

{% code %}
```bash
mv ../FileScanIO.zip .
```
{% /code %}

**Step #6 - Run the bootstrap shell script**

Note that this operation can take up to 20-30 minutes (depending on available network bandwidth).

{% code %}
```bash
sudo ./bootstrap.sh
```
{% /code %}

The first step of the installation process is accepting the product EULA, you need to **press Y** to start the installation.

**Step #7 -** **Optimize your transform and broker components if needed. More information: [Sandbox Engine Options](../configuration/engine-options.md).**

**Step #8 - Access the web server (localhost, port 443) and setup the initial admin user**

**Step #9 - Add your Activation Key**

The system will not be able to generate reports yet (and eventually gracefully exit), as a **valid Activation Key is required.**

Please use the Activation Key that you received from your OPSWAT Sales Representative, and follow the instructions on the [License Activation](license-activation.md) page.

If you use the default installation location, then you can create and copy the`licence.yml`file like this:

{% code %}
```bash
echo "ACTIVATION_KEY" > ~/license.yml
sudo cp ~/license.yml /home/filescanio/FileScanIO/fsTransform/license/
```
{% /code %}

**Step #10 - Optional: start the transform and/or broker services, if not running already**

{% code %}
```bash
sudo service fsio start
sudo service fsiobroker start
```
{% /code %}

**Step #11 -** **Check the application logs to ensure that the initialization succeeded**

To initialize the newly created bash aliases please run this command:

{% code %}
```bash
exec bash
```
{% /code %}

After this, the following command aliases will be available to the `filescanio` user (see `bootstrap.cfg`) and the user who performed the installation:

{% code %}
```bash
fsiolog
fsiologbroker
```
{% /code %}

{% callout type="warning" title="Note" %}
Please refer to the API top level menu at the webservice to learn how files may be sent to the system for automated processing. For custom integrations (e.g.: email), please reach out to support.
{% /callout %}

{% callout title="Best practices" %}
For a more comprehensive report, it's considered a best practice to enable the use of the MD Cloud Reputation API. For further details on this: [MD Cloud Reputation API](../integrations/reputation-api-integration.md)
{% /callout %}

**Important notes for air-gapped systems**

- The installation process **requires an Internet connection** (moving the system into a DMZ is recommended)
- Air-gapped systems will only receive updated features (like YARA) when installed and upgraded with an active internet connection. We recommend moving the system into a DMZ during these windows.
- All third-party integrations (e.g. Reputation API, geolocation/WHOIS lookup) require an Internet connection.
- The "File download" feature is not available in air-gapped environments.

To run Filescan in an offline environment without any errors, the following settings must be changed (after completing the installation process in an online environment).

Please open  `/home/filescanio/FileScanIO/fsTransform/conf/transform.properties.custom` using a text editor and add the following lines:

{% code %}
```java
downloadLatestPeStudioForDataEnrichment=false
runDomainResolver=false
runFileDownloaders=false
runIPStackLookupOnExectractedHosts=false
runIPStackOnDomainResolvedIPs=false
runHexillionOnExtractedDomains=false
runWhoisRecordLookups=false
ntpServer=127.0.0.1
ntpServerTimeout=1
ntpServerRefreshRateInSeconds=31536000
runSystemUpdateEvery=31536000
runYaraUpdateOnStartup=false
runPatchesOnStartup=false
runOSINTLookups=false
```
{% /code %}

Also open  `/home/filescanio/FileScanIO/fsTransform/conf/reputation.properties.custom` using a text editor and add the following line:

{% code %}
```java
refreshReputationSources=false
```
{% /code %}

Please remember to **save both configuration files** and restart the `fsio`  service:

{% code %}
```bash
sudo service fsio restart
```
{% /code %}
