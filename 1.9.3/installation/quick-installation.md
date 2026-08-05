---
type: page
title: Installation
listed: true
description: 
index_title: Installation
hidden: true
keywords: 
tags: 
---

{% callout type="warning" title="Prepare your host system / VM" %}
Before starting the installation, please make sure that your target system meets the [Technical Requirements](technical-requirements.md) and the installation is performed by a person with basic Linux skills.
{% /callout %}

{% callout type="success" title="Pro Tip" %}
Before installing, please check out our [Proxy Usage](quick-installation/installation-with-proxy.md) or [Air-gapped Systems](quick-installation/notes-for-air-gapped-environments.md) pages if these requirements apply to you!
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

{% callout title="Info" %}
Please use the **password** that you received from your OPSWAT Sales Representative!

Please adjust the x.y.z **version numbers** to match the downloaded filename, and make sure to have no quotes or spaces between the "-p" directive and the password (i.e. "7z x -p123456 file.zip").
{% /callout %}

{% code %}
```bash
7z x -p"PASSWORD" MetaDefender_Sandbox_vx.y.z-Standalone.zip
7z x fsBootstrap.zip -ofsBootstrap
rm fsBootstrap.zip
```
{% /code %}

**Step #3 - Ensure that the embedded installation scripts are executable:**

{% code %}
```bash
cd fsBootstrap
chmod +x *.sh
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

**Step #8 - Access the Filescan web server ([https://localhost:443](https://localhost:443)) and setup the initial Admin user**

**Step #9 - Add your Activation Key**

The system will not be able to generate scan reports yet, as a **valid Activation Key is required.**

Please use the Activation Key that you received from your OPSWAT Sales Representative, and follow the instructions on the [License Activation](license-activation.md) page.

Simple steps for Online activation:

Navigate to the *Admin panel \> Settings \> Integrations \> License Management* tab, then click on *Activate All,* then **enter your license key**!

**Step #10 - Optional: start the transform and/or broker services, if not running already**

{% code %}
```bash
sudo service fsio start
sudo service fsiobroker start
```
{% /code %}

**Step #11 -** **Check the application logs to ensure that the initialization succeeded**

To initialize the newly created bash aliases, please run this command:

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

{% callout title="Best practices" %}
For a more comprehensive report, it's considered a best practice to enable the use of the MD Cloud Reputation API. For further details on this: [MetaDefender Cloud Reputation Service](../integrations/reputation-api-integration.md)

The sandbox API is documented here: [**MD Sandbox API**](https://docs.opswat.com/filescan/metadefender-sandbox-api-reference-v1)
{% /callout %}

## Important notes for air-gapped systems

Please see the [Air-gapped Systems](quick-installation/notes-for-air-gapped-environments.md) subpage.
