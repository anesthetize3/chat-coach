---
type: page
title: Automated Data Deletion
listed: true
description: 
index_title: Automated Data Deletion
hidden: false
keywords: 
tags: 
---

## Configuration on the Admin panel

You can configure the retention under the Webservice Admin (UX) panel as well.

For that click on the user icon on the top right corner and select "**Admin**" panel:

{% image url="https://uploads.developerhub.io/prod/XX2D/2hb28t48iddjmoe4r2m0nz7h3uxttw9sf1hwbyrehw6f89g5pp9ftenro9k9bo3v.png" /%}

Then select "**Settings**" in the middle:

{% image url="https://uploads.developerhub.io/prod/XX2D/sc1o2mnicivrtczg6suecathaifb3i0ddlg1yf6jdq3puzfcvkubslgiaj1xvmpt.png" /%}

Select "**Configuration**":

{% image url="https://uploads.developerhub.io/prod/XX2D/xhi4ybb8sr3ci5l97zpauk51rh6ljplrqr65k9tefweklobh70y5eqqsy4nplpab.png" /%}

Under the "**Retention**" tab you can set retention policy:

{% image url="https://uploads.developerhub.io/prod/XX2D/dbzufoxxuf988r1gsqx1nno5duspuiac94ea86pvmo5g0t0qn5ko444hy6tqpikk.jpeg" /%}

By default, retention is enabled and set to 365 days.

## Backend configuration

By default, the backend services (broker and transform) are designed to clean up locally stored results/received samples and other temporary files after 1 day. These cleanup operations are performed continuously in a background process.

For more information about the specific configured, see [Retention Policy Configuration](../configuration/data-management/retention-policy-configuration.md)
