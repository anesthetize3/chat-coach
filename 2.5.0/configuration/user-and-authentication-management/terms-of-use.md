---
type: page
title: Terms of Use
listed: true
description: 
index_title: Terms of Use
hidden: false
keywords: 
tags: 
---

These are the identifiers / keys related to a service's terms of use, privacy policy, cookie policy, and other legal documents.

The location of the ***Terms of Use*** is **Admin Panel \> Settings \>[ Configuration](https://www.filescan.io/admin/settings/config)\> Terms of Use .**

{% image url="https://uploads.developerhub.io/prod/XX2D/d73sbyxrc1iongei9xon600o7rnc39xo2loot7wshvcfmrp1gkz4zdfkbaxgxhzu.png" %}
Screenshot of Configuration page of MetaDefender Sandbox
{% /image %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[289] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`TERMLY_ACCOUNT_ID`
{% /cell %}
{% cell %}
Identifier for the account or entity associated with the terms of use.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`TERMLY_PRIVACY_POLICY_ID`
{% /cell %}
{% cell %}
Unique identifier for the privacy policy of the service.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`TERMLY_TERMS_ID`
{% /cell %}
{% cell %}
Unique identifier for the terms of use document.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`TERMLY_COOKIE_POLICY_ID`
{% /cell %}
{% cell %}
Unique identifier for the cookie policy of the service.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`TERMS_LOCAL_SOURCE`
{% /cell %}
{% cell %}
A flag indicating to show the source or location of the terms of use.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`ASK_TERMS_CONSENT`
{% /cell %}
{% cell %}
A flag indicating whether the service asks users to consent to the terms of use explicitly. Requesting users to consent happens per scan/upload. If it is deemed unnecessary, it is possible to turn it off here.
{% /cell %}
{% /row %}
{% /table %}

Identifiers are used in the service's backend to reference specific legal documents or settings related to terms of use, privacy, and cookies.
