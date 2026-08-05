---
type: page
title: API
listed: true
description: 
index_title: API
hidden: false
keywords: 
tags: 
---

Configure backend REST API server access.

{% callout title="Proxy usage" %}
See: [How to install Sandbox with Proxy support](https://docs.opswat.com/filescan/installation-with-proxy)
{% /callout %}

**Step #1 - Open** `/home/sandbox/sandbox/transform.cfg` **in a text editor**

**Step #2 - Modify the server configuration by adding or modifying the following properties:**

{% code %}
```bash {% title="transform.cfg" %}
# Secret
apiKey0.secret=

# Server
listenServerPort=22001

# Proxy
proxyHost=proxy.example.com
proxyPort=3128
proxyUser=optional_user
proxyPassword=optional_password
nonProxyHosts=localhost
proxyType=HTTP
```
{% /code %}

**Step #3 - Save the file and restart the** `sandbox` **service**

## Property Details

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property Name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
apiKey0.secret
{% /cell %}
{% cell %}
\<generated\>
{% /cell %}
{% cell %}
API key, used in HTTP Header: 'secret'.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
listenServerPort
{% /cell %}
{% cell %}
22001
{% /cell %}
{% cell %}
HTTP port
{% /cell %}
{% /row %}
{% row %}
{% cell %}
proxyHost
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Host of proxy server
{% /cell %}
{% /row %}
{% row %}
{% cell %}
proxyPort
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Port of proxy server
{% /cell %}
{% /row %}
{% row %}
{% cell %}
proxyUser
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Optional proxy basic auth user
{% /cell %}
{% /row %}
{% row %}
{% cell %}
proxyPassword
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Optional proxy basic auth password
{% /cell %}
{% /row %}
{% row %}
{% cell %}
nonProxyHosts
{% /cell %}
{% cell %}
localhost
{% /cell %}
{% cell %}
A list of hosts which should be reached directly
{% /cell %}
{% /row %}
{% row %}
{% cell %}
proxyType
{% /cell %}
{% cell %}
HTTP
{% /cell %}
{% cell %}
Proxy type, can be: *'HTTP', 'DIRECT', 'SOCKS'*
{% /cell %}
{% /row %}
{% /table %}
