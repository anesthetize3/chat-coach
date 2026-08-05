---
type: page
title: SSL Certificates
listed: true
description: 
index_title: SSL Certificates
hidden: true
keywords: 
tags: 
---

Filescan uses the **NGINX** web server and its configuration is defined in `/srv/backend/nginx/conf/production/default.conf`

{% callout type="warning" title="Warning" %}
Any modifications to `/srv/backend/nginx/conf/production/default.conf` will be **overwritten if you upgrade** your Filescan installation!

Always **create a backup** of this file if you modify it!

Alternatively, choose a solution below that does not require modifications to this file!
{% /callout %}

The following self-signed certificate and key files are used by default:

```
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
```

It is possible to modify the configuration to point to your certificate and key files, but it is **recommended to overwrite** the self-signed certificate and key with your own files instead! If you do that, you can upgrade Filescan without losing these settings.

Please create a backup of the self-signed certificate and key files first:

{% code %}
```bash
sudo mv /etc/ssl/certs/nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned-BACKUP.crt
sudo mv /etc/ssl/private/nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned-BACKUP.key
```
{% /code %}

Then overwrite these files with your **full certificate chain and private key files in PEM format** (the original file extension does not matter). For example, if your custom files are located in `~/my.domain.com` :

{% code %}
```bash
sudo cp ~/my.domain.com/fullchain.pem /etc/ssl/certs/nginx-selfsigned.crt
sudo cp ~/my.domain.com/privkey.pem /etc/ssl/private/nginx-selfsigned.key
```
{% /code %}

Make sure that the certificate is readable by all users and the private key is owned by your `filescanio` user:

{% code %}
```bash
sudo chmod a+r /etc/ssl/certs/nginx-selfsigned.crt
sudo chown filescanio:filescanio /etc/ssl/private/nginx-selfsigned.key
```
{% /code %}

After these preparations, please restart the Filescan webservice (this should only take a minute):

{% code %}
```bash
/home/filescanio/FileScanIO/shutdown_webservice.sh
/home/filescanio/FileScanIO/launch_webservice.sh
```
{% /code %}

At this point, you should be able to reach your Filescan instance at `https://my.domain.com` on port 443.

---

#### Special considerations for private key files with a passphrase

NGINX also supports PEM private key files that require a passphrase to use.

In this case, the `ssl_password_file` option should be added in `/srv/backend/nginx/conf/production/default.conf` as described in the [NGINX documentation](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_password_file)

For example:

{% code %}
```bash
ssl_password_file /etc/keys/global.pass;
```
{% /code %}

As the `default.conf` file must be changed for this, it is strongly encouraged to create a **backup** of this file **before you upgrade Filescan**!
