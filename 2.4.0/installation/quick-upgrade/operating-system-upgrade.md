---
type: page
title: Operating System Upgrade
listed: true
description: 
index_title: Operating System Upgrade
hidden: true
keywords: 
tags: 
---

Upgrading MetaDefender Sandbox from version 1.x.x to 2.x.x **requires an operating system upgrade** from Ubuntu 20.04 to Ubuntu 22.04 LTS. This guide shows how to upgrade Ubuntu **before** MetaDefender Sandbox is installed.

{% callout type="warning" title="Backup your system" %}
Before starting the Ubuntu upgrade process, please create a backup of your system if possible!
{% /callout %}

**Step #1 - Unmonitor Sandbox services and delete monit service**

{% code %}
```bash
sudo monit unmonitor fsiobroker
sudo monit unmonitor fsio
sudo systemctl stop monit
sudo systemctl disable monit
sudo apt-get purge -y monit
```
{% /code %}

**Step #2 - Stop and disable Sandbox services**

Please be aware that the path `/home/filescanio/FileScanIO` can differ based on the configuration used for the installation.

{% code %}
```bash
sudo service fsioweb stop
sudo /home/filescanio/FileScanIO/shutdown_webservice.sh

sudo service fsiobroker stop
sudo service fsio stop

sudo systemctl disable fsioweb
sudo systemctl disable fsiobroker
sudo systemctl disable fsio
```
{% /code %}

**Step #3 - Uninstall docker and remove Tesseract PPA**

{% code %}
```bash
sudo apt-get purge -y --allow-change-held-packages docker-ce docker-ce-cli docker-ce-rootless-extras docker-buildx-plugin docker-compose-plugin containerd.io

sudo rm -f /etc/apt/sources.list.d/alex-p-ubuntu-tesseract-ocr-focal.list

sudo apt autoremove -y
```
{% /code %}

**Step #4 - Upgrade Ubuntu from 20.04 LTS to 22.04 LTS**

Please follow this guide to upgrade your operating system: [https://www.cyberciti.biz/faq/upgrade-ubuntu-20-04-lts-to-22-04-lts/](https://www.cyberciti.biz/faq/upgrade-ubuntu-20-04-lts-to-22-04-lts/)

**Step #4.1 - Sandbox related configuration files**

During the installation there could be questions about modified configuration files, e.g.`/etc/multitail.conf` .

Please choose: `Y or I : install the package maintainer's version`.

**Step #4.2 - Obsolete packages**

It is recommended to remove obsolete packages during the upgrade process.

**Step #4.3 - Enabling third party repositories or mirrors**

When enabling these repositories in `/etc/apt/sources.list.d` please double check to use the correct version (22.04) and codename (jammy) in the `.list`  files.

**Step #5 - Upgrade MetaDefender Sandbox** **to 2.x.x**

Please follow the guide on the [Upgrade](../quick-upgrade.md) page.
