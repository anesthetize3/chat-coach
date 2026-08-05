---
type: page
title: How to disable a Threat Indicator?
listed: true
description: 
index_title: How to disable a Threat Indicator?
hidden: false
keywords: 
tags: 
---

In order to disable a Threat Indicator, the corresponding Python File must be removed. Future development will allow for this to be completed through the CLI.

## Steps to Disable the Threat Indicator

Outlined below are the steps that should be followed so that a Threat Indicator can be disabled. In this example, the aim is to disable the following Threat Indicator: "**Found a call for action (e.g. 'enable macros')**"

{% image url="https://uploads.developerhub.io/prod/XX2D/ohu1rg2thdfu7pddgdbvrfzpmcg88w48jsj7sbm2i4crodwpa98ho305t07otni0.png" /%}

### Find the ID of the Threat Indicator

Find the Threat Indicator ID within the *Hunting* page by searching for the Threat Indicator description.

In this case it is **S040**.

{% image url="https://uploads.developerhub.io/prod/XX2D/lljzwc1xr50lnhzx7hn1jzu5my35e2r6axisq9h3a0xqpp0ollel6hdxjnd6yhxy.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/cya83jb7i3g6mmpj72mm8ns4puylah4ljltl19rhgkpgnpvrop4o48jgjzu32oro.png" /%}

### Locate and Rename the Corresponding Python File

Search: *\<installation directory\>/transform/consumers*

Locate the consumer file. The File Name is similar, however it is not always the same as the Threat Indicator ID.

In relation to this Threat Indicator, it is **strings-040.py.** Ensure it is the correct consumer by checking the consumer ID in the python script:

{% code %}
```python
def identifier():
	return "S040"
```
{% /code %}

Example bash command to find the consumer file:

{% code %}
```bash {% title="bas" %}
~/sandbox/transform$ grep -rl 'return "S040"' ./consumers/
```
{% /code %}

### Rename the file

For this example, it is renamed to: **strings-040.py.disabled**

### Restart Sandbox

Restart the Sandbox service for the modification to take effect.

{% callout type="warning" title="Warning" %}
The consumer will be automatically restored by a reinstall or upgrade install.
{% /callout %}
