---
type: page
title: IMAP Integration
listed: true
description: 
index_title: IMAP Integration
hidden: true
keywords: 
tags: 
---

Another new web service feature is the **Scan Sources** capability accessible from the **Top Menu**. It allows configuring the web service to pull in files/URLs from a variety of sources.

To set up an **Email Scan Source** navigate to **Scan Sources -\> Config -\> Add Source.**

{% callout type="warning" title="Warning" %}
IMAP integration is currently supported only for Gmail accounts or Google Workspace accounts.
{% /callout %}

{% image url="../../assets/684233f563b85d88f8bfabc396f827175a9440cf.png" /%}

Currently, we support the configuration of IMAP accounts that are then regularly polled with a background (cron-like) job and ingested into the web service automatically. Here are a few examples:

{% image url="https://uploads.developerhub.io/prod/XX2D/v9l197d24eixe3smq6n0zar3l96w9p4ioms3yxzlt08rkdv0qrohme1wrvpa2blp.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/j5n7kzhnviwan6j6qk7m6h26dv7ox0ni2j4s613hmlevrkktmnchmjku7t3oufdq.png" /%}

You can edit a **Scan Source** by navigating to **Scan Source -\> Config** and clicking on the pencil icon.

{% image url="https://uploads.developerhub.io/prod/XX2D/n8gafr62s6gv1c3b5cq0iz2qx0jn3qm0xkp2n1s0688snpk4af4su4q0q9hl7gyz.png" /%}
