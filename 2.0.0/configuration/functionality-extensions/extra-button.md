---
type: page
title: Extra Button
listed: true
description: 
index_title: Extra Button
hidden: true
keywords: 
tags: 
---

The admin can create a programmable button on the interface. Its settings can be parameterized in the **Admin Panel \> Setting \> Configurations \> Extra Button** section.

{% image url="https://uploads.developerhub.io/prod/XX2D/ztx1b0czaplkq95hj5qwb7sk9tralroaal2g9ulk1y14fnpsrhbyfaeohjht3b8i.png" /%}

After configuration, the extra button appears on the homepage, to the left of the profile icon:

{% image url="https://uploads.developerhub.io/prod/XX2D/adjljizpi02hbdnfx91130gxm9ceqtpx1ht4awuxozbhowtiwwlnpbf4akyzjho0.png" /%}

### Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[227] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`EXTRA_BUTTON_TEXT`
{% /cell %}
{% cell %}
The text of the button.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`EXTRA_BUTTON_LINK`
{% /cell %}
{% cell %}
The link where the button goes to.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`EXTRA_BUTTON_ACTIVE`
{% /cell %}
{% cell %}
Enable or disable the extra button.
{% /cell %}
{% /row %}
{% /table %}
