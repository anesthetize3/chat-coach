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
Before starting the installation, please make sure that your target system meets the [Technical Requirements](technical-requirements.md) and the installation is **performed by a person with basic Linux skills**.
{% /callout %}

{% callout type="warning" title="Warning" %}
This page only refers to product installation with a **stable Internet connection**!

For **offline installations**, please follow the [Offline Installation](offline-installation.md) guide instead!
{% /callout %}

{% callout type="success" title="Pro Tip" %}
Before installing, please check out our [Proxy Usage](quick-installation/installation-with-proxy.md) or [Air-gapped Systems](quick-installation/notes-for-air-gapped-environments.md) pages if these requirements apply to you!
{% /callout %}

Please walk through the following steps. If you encounter any issues during installation, refer to our [Troubleshooting Guide.](https://docs.opswat.com/filescan/troubleshooting)

## Preparation

### Ubuntu 22.04

**Step #1 - (Optional) Create a new user that will own all the installed files and run the Sandbox services**

{% code %}
```bash
sudo adduser --disabled-password --gecos "" sandbox
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

### RedHat 9.5

{% callout title="EPEL repositories" %}
Some packages require the EPEL repositories. Ensure they are available in your package manager.
{% /callout %}

**Step #1 - (Optional) Install EPEL repositories if they are not yet available**

{% code %}
```bash
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm -y
```
{% /code %}

**Step #2 - (Optional) Create a new user that will own all the installed files and run the Sandbox services**

{% code %}
```bash
sudo useradd --create-home sandbox
sudo passwd -l sandbox
```
{% /code %}

**Step #3 - Download and unpack the release archive to a folder, e.g.: your home folder**

Install 7zip:

{% code %}
```bash
sudo dnf update -y
sudo dnf install p7zip -y
```
{% /code %}

## Installation

**Step #1 - Download the product:**

Download the release archive from [https://my.opswat.com/portal/products](https://my.opswat.com/portal/products)

Note that the release archive is password protected and needs to be unpacked.

{% callout title="Info" %}
Please use the **password** that you received from OPSWAT support!

Please adjust the x.y.z **version numbers** to match the downloaded filename.
{% /callout %}

{% code %}
```bash
7za x -aoa -p"PASSWORD" MetaDefender_Sandbox_vx.y.z-Standalone.zip
```
{% /code %}

**Step #2 - Move to the installation folder:**

{% code %}
```bash
cd sandbox-installer
```
{% /code %}

**Step #3 - (Optional) Edit install.cfg to specify a custom user name and installation path**

*Note: The default settings work fine for standard deploys and all features can be configured post installation.*

More details are available in [Installation Options](quick-installation/installation-options.md).

**Step #4 - Run the install shell script**

Note that this operation can take up to 20-30 minutes (depending on available network bandwidth).

{% code %}
```bash
sudo ./install.sh
```
{% /code %}

The first step of the installation process is accepting the product EULA, you need to **press Y** to start the installation.

**Step #5 - Access the Sandbox web server ([https://localhost:443](https://localhost:443)) and setup the initial Admin user**

**Step #6- Add your Activation Key**

The system will not be able to generate scan reports yet, as a **valid Activation Key is required.**

Please use the Activation Key that you received from your OPSWAT Sales Representative, and follow the instructions on the [License Activation](license-activation.md) page.

Simple steps for Online activation:

Navigate to the *Admin panel \> Settings \> Integrations \> License Management* tab, then click on *Activate All,* then **enter your license key**!

**Step #7 - Scan your preferred test file to check if the Sandbox system functions properly**

**Step #8 - (Optional) Troubleshooting if the Sandbox service failed to** **initialize**

Verify the status of the `sandbox`  service and if the running docker container are healthy:

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

{% callout title="Best practices" %}
For a more comprehensive report, it is considered a best practice to enable the use of the MD Cloud Reputation API. For further details on this: [MetaDefender Cloud Reputation Service](../integrations/reputation-api-integration.md)

The sandbox API is documented here: [**MD Sandbox API**](https://docs.opswat.com/filescan/metadefender-sandbox-api-reference-v1)
{% /callout %}

## Important notes for air-gapped systems

Please see the [Air-gapped Systems](quick-installation/notes-for-air-gapped-environments.md) subpage.
