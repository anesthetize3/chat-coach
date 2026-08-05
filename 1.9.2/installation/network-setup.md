---
type: page
title: Network Setup
listed: true
description: 
index_title: Network Setup
hidden: true
keywords: 
tags: 
---

### High-Level Networking Setup

{% image url="https://uploads.developerhub.io/prod/XX2D/b0bfmva3w2fj2d2sqfdcmgvqrfr5j3kn4bknxondoahnsk6h08x4gakbjhzhnkzx.png" /%}

It is strongly recommended to deploy the **MetaDefender Sandbox** (previously known as Filescan) server in a **segregated network** (e.g. DMZ, VLAN, VPC).

This segregated network can be connected to a corporate network through a firewall that only allows access to the Sandbox Web interface and REST API over **HTTPS (port 443)**. This "management" connection might use a dedicated network card.

A secondary network card could be used for "sample analysis" purposes to allow outbound connections to the Internet. An important purpose of the Sandbox system is to download the second stage payloads and analyze them. This secondary network connection can also be used for updating system packages, downloading updated YARA rules and connecting to reputation services in the Cloud.

**An Internet connection is required during the product installation.** After a successful installation, the outbound connection might be disabled after considering the following limitations:

- Offline systems cannot receive updated features (like YARA rules) to improve detections for recent threats.
- All third-party integrations (e.g. Reputation API, geolocation/WHOIS lookup) require an Internet connection.
- The "File download" feature is not available in offline environments.
- The "URL rendering and phishing detection" features are not available in offline environments.

Note that the quality of the Sandbox analysis will deteriorate without these important features!

### Recommended iptables Configuration

The following `iptables` rules are recommended for a standard single-server deployment.

This setup will block all incoming connections except for HTTPS (port 443) and SSH (port 22) traffic.

We also need to allow internal communication on the `docker0`  interface, otherwise the Sandbox Webservice cannot send requests to fsBroker running on the host system.

Please fine-tune these rules to match your specific requirements:

```
# Set default policies 
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Accept traffic on localhost
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Allow established sessions to receive traffic
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow outside access to the Sandbox Webservice and REST API
iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT

# Allow Sandbox Webservice to reach fsBroker on docker0 interface
iptables -A INPUT -d 172.17.0.1/16 -j ACCEPT

# (Optional) Allow SSH access
iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
```

#### Additional Hardening

It is also possible to block all outgoing traffic except for a selected list of domains. Please refer to the list of [Domains Contacted During Installation](../datasheet/domains-contacted-during-installation.md) to identify the most important domains.

{% callout type="warning" title="Warning" %}
Disclaimer: With maximum hardening the analysis quality will decrease, as the purpose of the sandbox is to allow outbound traffic to download the second stage payloads and analyze them.
{% /callout %}

Note that `iptables` alone is not suitable for blocking/allowing connections on the domain level (iptables works with IP addresses instead).

In your custom firewall configuration, you can allow the following list of essential domains as a starting point:

{% code %}
```bash
opswat.com
ubuntu.com
docker.io
pypa.io
github.com
microsoft.com
filescan.com
```
{% /code %}

### Internal Communication Ports

All internal communication among Sandbox components uses custom REST APIs.

The `fsBroker`  HTTP server is listening on port 23001.

The `fsTransform`  HTTP server is listening on port 22001.
