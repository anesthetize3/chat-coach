---
type: page
title: Can I change MetaDefender Aether Web UI’s port?
listed: true
description: 
index_title: Can I change MetaDefender Aether Web UI’s port?
hidden: false
keywords: 
tags: 
---

Yes, the port used by the MetaDefender Aether Web Interface can be modified.

The port mapping is defined in the following configuration file:

/home/sandbox/sandbox/webservice/docker-compose.nginx.yml

{% image url="https://uploads.developerhub.io/prod/XX2D/jkklh8eflyxks59hx362faj84mbtf4dmqqke5g2y9e7lbotrpwo46rbhs1801lea.png" /%}

In this file, the port mapping follows the format:

**\<external\_port\>:\<internal\_container\_port\>**

To change the external port accessed by users, simply modify the left-hand (external) port value. For example:

{% image url="https://uploads.developerhub.io/prod/XX2D/vfbuqhh54aywqn5o5vb6qh6chs6biwjobezxenxo5l0kvmza8t98doled8yizvau.png" /%}

After updating the configuration, apply the changes by restarting the Sandbox application using the following script:

**/home/sandbox/sandbox/restart\_sandbox.sh**

Once restarted, the MetaDefender Sandbox Web UI will be accessible at:

**https://\<sandbox\_ip\>:12345**

{% image url="https://uploads.developerhub.io/prod/XX2D/5gg5u2h1lqn56gcp1nwnjkiotmlozl2whv5l1f8mt1lisuc2kvdgqdqlopn0qm9i.png" /%}

This allows you to customize the web interface port to meet your network or security requirements.

{% callout title="Support:" %}
If further assistance is required, please proceed to log a support case or chatting with one of our support engineers.
{% /callout %}
