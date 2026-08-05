---
type: page
title: Proxy Usage
listed: true
description: 
index_title: Proxy Usage
hidden: false
keywords: 
tags: 
---

{% callout type="success" title="Pro Tip" %}
We recommend using a **transparent proxy**! A transparent proxy can hide its settings, hence it is safer and requires no additional configuration on the target machine.
{% /callout %}

{% callout title="Info" %}
This feature is available from Sandbox version 1.9.3
{% /callout %}

## Proxy server configuration

The following URLs are recommended to bypass on the proxy server:

- [https://api.metadefender.com/](https://api.metadefender.com/v4/) (For OPSWAT Reputation lookup)
- [https://activation.dl.opswat.com/](https://activation.dl.opswat.com/) (To reach the OPSWAT license server)

## Sandbox server configuration

The following configuration is necessary for the installer and the product to work properly behind a **non-transparent HTTP proxy**.

### Before Sandbox installation

Set the following configuration settings before installation.

#### System-wide proxy configuration

Update the `/etc/environment` config, copy the proxy variables to the end of the file as described below. This will be used by tools like WGET, CURL, APT.

{% callout type="warning" title="Warning" %}
Always set the `NO_PROXY` variable to **precisely** **match** the example below. The IP address ranges: `172.16.0.0/12` and `192.168.0.0/16` are used by Docker, do not reuse them for other purposes.

Use your own proxy URLs instead of the example *proxy.example.com:3128.*
{% /callout %}

{% callout title="Info" %}
The proxy format is `<protocol>://<user>:<password>@<domain or IP address>:<port>` where \<user\> and \<password\> are URL encoded strings.
{% /callout %}

```plaintext {% title="/etc/environment" %}
http_proxy=http://proxy.example.com:3128
https_proxy=https://proxy.example.com:3128
HTTP_PROXY=http://proxy.example.com:3128
HTTPS_PROXY=https://proxy.example.com:3128
NO_PROXY=localhost,172.16.0.0/12,192.168.0.0/16,fsio,broker,transform,reverse_proxy
```

Once the file is updated log out and log in again for these changes to take effect:

{% code %}
```bash
exit
```
{% /code %}

#### Docker proxy configuration

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
Environment="NO_PROXY=localhost,172.16.0.0/12,192.168.0.0/16,fsio,broker,transform,reverse_proxy"
```

Optionally, if the docker daemon is already installed on your system, restart it:

{% code %}
```bash
sudo systemctl daemon-reload
sudo service docker restart
```
{% /code %}

Install Sandbox as described on the [Installation](../quick-installation.md) page.

{% callout type="warning" title="Warning" %}
**Online** license activation is not working when a proxy is used!

Please follow the "**Offline license activation**" section of the [License Activation](../license-activation.md) page.
{% /callout %}

### After Sandbox installation (optional)

{% callout title="Info" %}
Sandbox will use the system proxy settings from `HTTP_PROXY` and `NO_PROXY` environment variables if available and no other proxy settings are defined.
{% /callout %}

**Optionally**, you can override the system-wide proxy configuration if you modify the `transform.cfg`  property file as described in [proxy settings](https://docs.opswat.com/filescan/configuration/engine-config-api). These changes only affect the transform component.

For other Docker containers, it is possible to change the proxy configuration without reinstalling Sandbox if you modify `/home/sandbox/.docker/config.json` (the path may differ if you installed Sandbox under a different user):

{% code %}
```json {% title="/home/sandbox/.docker/config.json" %}
{
    "proxies": {
        "default": {
            "httpProxy": "http://proxy.example.com:3128",
            "httpsProxy": "https://proxy.example.com:3128",
            "noProxy": "localhost,172.16.0.0/12,192.168.0.0/16,fsio,broker,transform,reverse_proxy"
        }
    }
}
```
{% /code %}

Then please restart the sandbox service to remove and restart all Docker containers:

{% code %}
```bash
sudo service sandbox restart
```
{% /code %}

You can check the currently used proxy configuration for a given Docker container, e.g. for transform:

{% code %}
```bash
docker inspect --format='{{range .Config.Env}}{{println .}}{{end}}' transform
```
{% /code %}

This is the expected output:

{% code %}
```bash
HTTP_PROXY=http://proxy.example.com:3128
http_proxy=http://proxy.example.com:3128
HTTPS_PROXY=https://proxy.example.com:3128
https_proxy=https://proxy.example.com:3128
NO_PROXY=localhost,172.16.0.0/12,192.168.0.0/16,fsio,broker,transform,reverse_proxy
no_proxy=localhost,172.16.0.0/12,192.168.0.0/16,fsio,broker,transform,reverse_proxy
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
UNAME=sandbox
```
{% /code %}
