---
type: page
title: Engine
listed: true
description: 
index_title: Engine
hidden: false
keywords: 
tags: 
---

Engine configurations is being described inside the Configurations part on this part of the page.

**Admin Panel \> Setting \> Configurations \> Engine**

These configurations together define how the MetaDefender Sandbox communicates with its embedded malware analysis engine, including the protocol, host, port, and authentication mechanism.

{% image url="https://uploads.developerhub.io/prod/XX2D/4x38usznoqrmqioxtqf1ve7fgsex01w4ocwgbl9vwm6egui0xo6v5tku0fri1lwg.png" %}
Screenshot of Engine settings inside Configuration part on MetaDefender Sandbox webpage
{% /image %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[283] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*ENGINE\_SCHEMA*
{% /cell %}
{% cell %}
Specifies the protocol or schema used for communication with embedded MetaDefender Sandbox. In this case, it's set to "https", indicating that HTTPS (HTTP Secure) protocol is used for secure communication.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*ENGINE\_HOST*
{% /cell %}
{% cell %}
Specifies the IP address or hostname of the server where the malware analysis engine is hosted. In this configuration, the IP address needs to be provided.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*ENGINE\_PORT*
{% /cell %}
{% cell %}
Specifies the port number used for communication with the malware analysis engine
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*ENGINE\_SECRET*
{% /cell %}
{% cell %}
This refers to an authentication or access token/key required to authenticate requests to the MetaDefender Sandbox. The value is masked for security reasons, but it would be a secret key or token that grants access to the engine's functionalities.
{% /cell %}
{% /row %}
{% /table %}
