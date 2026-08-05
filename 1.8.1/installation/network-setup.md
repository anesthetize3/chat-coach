---
type: page
title: Network Setup
listed: false
description: 
index_title: Network Setup
hidden: true
keywords: 
tags: 
---

### High-Level Networking Setup

{% image url="https://uploads.developerhub.io/prod/XX2D/lfftjngsp6rxmwad4qq98wfxh5ji0wdpmbqxix3gjvz6xmzvmikbjbpdc147won1.png" /%}

It is strongly recommended to deploy the Filescan Sandbox server in a **segregated network** (e.g. DMZ, VLAN, VPC).

This segregated network can be connected to a corporate network through a firewall that only allows access to the Filescan Web interface and REST API over **HTTPS (port 443)**. This "management" connection might use a dedicated network card.

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

We also need to allow internal communication on the `docker0`  interface, otherwise the Filescan Webservice cannot send requests to fsBroker running on the host system.

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

# Allow outside access to the Filescan Webservice and REST API
iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT

# Allow Filescan Webservice to reach fsBroker on docker0 interface
iptables -A INPUT -d 172.17.0.1/16 -j ACCEPT

# (Optional) Allow SSH access
iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
```

#### Additional Hardening

It is also possible to block all outgoing traffic except for a short list of domains (that are required for essential features).

Disclaimer: With maximum hardening the analysis quality will decrease, as the purpose of the sandbox is to allow outbound traffic to download the second stage payloads and analyze them.

### Internal Communication Ports

All internal communication among Filescan components uses custom REST APIs.

The fsBroker HTTP server is listening on port 23001.

The fsTransform HTTP server is listening on port 22001.
