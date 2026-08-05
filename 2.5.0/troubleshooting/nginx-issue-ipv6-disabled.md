---
type: page
title: NGINX startup issue when IPv6 is disabled
listed: true
description: 
index_title: NGINX startup issue when IPv6 is disabled
hidden: true
keywords: 
tags: 
---

On hardened systems where **IPv6 is fully disabled**, the nginx server in MetaDefender Sandbox might fail to start.

In this situation, `docker ps`  shows that the `reverse_proxy` (nginx) container is **restarting continuously** every few seconds and other Sandbox containers can become `unhealthy` because of the failing `reverse_proxy`.

It is recommended to check the last few lines of the nginx `error.log`  using this command:

{% code %}
```bash
$ sudo tail /home/sandbox/sandbox/webservice/nginx/logs/error.log
...
[emerg] socket() [::]:443 failed (97: Address family not supported by protocol)
```
{% /code %}

If you see the `Address family not supported by protocol`  error, the underlying issue can be addressed by enabling IPv6 on the system or by modifying the nginx `default.conf` file in `/home/sandbox/sandbox/webservice/nginx/conf/production` (the path might differ if you installed Sandbox to a different target directory).

If enabling IPv6 is not feasible, please open the nginx `default.conf` file using a text editor (e.g. nano, vi) and scroll down to locate the following section in the file:

{% code %}
```bash
$ sudo nano /home/sandbox/sandbox/webservice/nginx/conf/production/default.conf
...

server {
    listen 443 http2 ssl;
    listen [::]:443 http2 ssl;

    ssl_certificate /app/nginx/certs/nginx-selfsigned.crt;
    ssl_certificate_key /app/nginx/certs/nginx-selfsigned.key;
    ssl_dhparam /app/nginx/certs/dhparam.pem;
```
{% /code %}

Please **add a # sign** in front of the **second listen directive** to comment out that line and disable listening on IPv6.

The updated section should look like:

```plaintext {% title="default.conf" %}
server {
    listen 443 http2 ssl;
    #listen [::]:443 http2 ssl;

    ssl_certificate /app/nginx/certs/nginx-selfsigned.crt;
    ssl_certificate_key /app/nginx/certs/nginx-selfsigned.key;
    ssl_dhparam /app/nginx/certs/dhparam.pem;
```

Please **save the file** (Ctrl+O in nano) and exit the text editor.

Restart the sandbox service:

{% code %}
```bash
sudo service sandbox restart
```
{% /code %}

After this change, nginx should start without issues and the Sandbox `webservice` can function properly.
