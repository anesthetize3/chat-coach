---
type: page
title: Proxy Usage
listed: true
description: 
index_title: Proxy Usage
hidden: true
keywords: 
tags: 
---

{% callout type="success" title="Pro Tip" %}
We recommend using a **transparent proxy**! A transparent proxy can hide its settings, hence it is safer and requires no additional configuration on the target machine.
{% /callout %}

{% callout title="Info" %}
This feature is available from Sandbox version 1.9.3
{% /callout %}

{% callout type="warning" title="Warning" %}
For now only offline license activation is available with non-transparent proxy
{% /callout %}

## Proxy server configuration

The following URLs are recommended to bypass:

- https://api.metadefender.com/v4/ (For OPSWAT Reputation lookup)
- https://activation.dl.opswat.com/ (To reach the OPSWAT license server)

## Sandbox server configuration

The following configuration is necessary for the installer and the product to work properly behind a **non-transparent HTTP proxy**.

### Before Sandbox installation

Set the following configuration settings before installation.

#### System-wide proxy configuration

Update the `/etc/environment` config, copy the proxy variables to the end of the file as described below. This will be used by tools like WGET, CURL, APT.

{% callout type="warning" title="Warning" %}
Set the `NO_PROXY` variable based on the example below. `172.16.0.0/12` and `192.168.0.0/16` are used by Docker, do not reuse them for other purposes.

Use your own proxy URLs instead of the example *proxy.example.com:3128.*
{% /callout %}

{% callout title="Info" %}
The proxy format is `<protocol>://<user>:<password>@<domain or IP address>:<port>` where \<user\> and \<password\> are URL encoded strings.
{% /callout %}

Once the file is updated log out and log in again for these changes to take effect:

{% code %}
```bash
exit
```
{% /code %}

```plaintext {% title="/etc/environment" %}
http_proxy=http://proxy.example.com:3128
https_proxy=https://proxy.example.com:3128
HTTP_PROXY=http://proxy.example.com:3128
HTTPS_PROXY=https://proxy.example.com:3128
NO_PROXY=localhost,172.16.0.0/12,192.168.0.0/16,fsio
```

Docker proxy configuration

#### Docker Daemon

Create the docker daemon proxy configuration file.

{% code %}
```bash {% title="http-proxy.conf" %}
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo touch /etc/systemd/system/docker.service.d/http-proxy.conf
```
{% /code %}

Update the proxy settings similarly to the system-wide proxy configuration:

```plaintext {% title="http-proxy.conf" %}
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:3128"
Environment="HTTPS_PROXY=https://proxy.example.com:3128"
Environment="NO_PROXY=localhost,172.16.0.0/12,192.168.0.0/16,fsio"
```

Optionally, if the docker daemon is already installed on your system, restart it:

{% code %}
```bash
sudo systemctl daemon-reload
sudo service docker restart
```
{% /code %}

Install Sandbox as described on the [Installation](../quick-installation.md) page.

## After Sandbox installation (optional)

{% callout title="Info" %}
Sandbox will use the system proxy settings from `HTTP_PROXY` and `NO_PROXY` environment variables if available and no other proxy settings are defined.
{% /callout %}

**Optionally**, add the proxy configuration to the fsTransform property file to override system  proxy settings:

```plaintext {% title="<install_dir>/fsTransform/conf/transform.properties.custom" %}
proxyHost=proxy.example.com
proxyPort=3128
proxyUser=optional_user
proxyPassword=optional_password
proxyType=HTTP
```
