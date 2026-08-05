---
type: page
title: Third Party
listed: true
description: 
index_title: Third Party
hidden: true
keywords: 
tags: 
---

These configurations are for integrating and configuring third-party services, particularly Google Analytics and Google Sitemap ping, within MetaDefender Sandbox.

The location of ***Third Party*** setting is under **Admin Panel \> Settings \> [Configuration ](https://www.filescan.io/admin/settings/config)\> Third Party** .

{% image url="https://uploads.developerhub.io/prod/XX2D/99yqxakeysumidk8neelp53wcdmk8shrphemunls5ecyzge62r9nlg6ixojxvpc3.png" %}
Screenshot of the Configuration page of MetaDefender Sandbox
{% /image %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[290] %}
**Field**
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`GOOGLE_ANALYTICS_ID`
{% /cell %}
{% cell %}
A placeholder for the Google Analytics tracking ID. Google Analytics is a web analytics service provided by Google that tracks and reports website traffic. This ID is unique to each Google Analytics property and is used to identify and collect data from the website.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`GOOGLE_ANALYTICS_ID_V3`
{% /cell %}
{% cell %}
A placeholder for a different version of the Google Analytics tracking ID. The service is being migrated to a newer version of Google Analytics.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`PING_GOOGLE_SITEMAP_HOSTNAME`
{% /cell %}
{% cell %}
It specifies the hostname to which Google should be pinged when a sitemap is updated. A sitemap is a file that lists the URLs of a website, allowing search engines like Google to crawl and index the site more effectively. When you ping Google with an updated sitemap, it tells Google that your website has changed and asks them to check it out again.
{% /cell %}
{% /row %}
{% /table %}
