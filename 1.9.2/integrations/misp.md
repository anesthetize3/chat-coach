---
type: page
title: MISP
listed: true
description: 
index_title: MISP
hidden: false
keywords: 
tags: 
---

The MISP is an open source software solution for collecting, storing, distributing and sharing cyber security indicators and threats about cyber security incidents analysis and malware analysis. You can find more information about MISP [here](https://www.misp-project.org).

{% callout type="warning" title="Note" %}
To integrate with MISP, it is necessary to have a pre-installed MISP instance.
{% /callout %}

## Integrating MetaDefender Sandbox with MISP

To create an integration, navigate to the Admin panel.

{% image url="https://uploads.developerhub.io/prod/XX2D/xl1tkmgaoj8w3fhsxnnjh8cu3j2v9rs3segcs9yqplfxhjt1yqo1p8149vpapzoo.png" /%}

Select "Settings" from the menu bar, and you'll find the MISP tab under Configuration.

{% image url="https://uploads.developerhub.io/prod/XX2D/jkdjews6ao26suoralso1g6cvjlvmvebapq69jj048cle6mfm0lpm5i19y13aosr.png" /%}

Enter your MISP API key and MISP API URL, check the "*MISP\_ENABLED*" checkbox, and then save the settings.

{% image url="https://uploads.developerhub.io/prod/XX2D/jdrvh6raul4xga2mk86wjiknzflf4dz4jpm20xedmgb9hnuehoead46bm4bt9cw1.png" /%}

{% callout type="warning" title="Note" %}
note that in order for Sandbox results to be added as events to MISP, the url format should be:

**\<MISP URL\>/events/add**
{% /callout %}

If everything is correct, click on the "Save" button.

{% image url="https://uploads.developerhub.io/prod/XX2D/mlrq4fepotsdwrp95quvnojvodg81y2p1faiwcbx9lm7f1xw02bbk45up2sq7z58.png" /%}

If MISP integration is enabled, then **Malicious** and **Likely Malicious** results will be published.

If all settings are correct, events will appear in the MISP instance. For example:

{% image url="https://uploads.developerhub.io/prod/XX2D/topmyks36w5jdyndzumczo84hqa2uenw9lwc9wfy0prc5l8tfrqes2qirfefko6z.png" /%}
