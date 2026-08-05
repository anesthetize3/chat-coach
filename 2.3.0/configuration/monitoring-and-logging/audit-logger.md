---
type: page
title: Audit Logging for Admin Settings and User Authentication
listed: true
description: 
index_title: Audit Logging for Admin Settings and User Authentication
hidden: false
keywords: 
tags: 
---

## Function

The Audit Logger is a logging system that logs events happening inside the system. These events include settings changes, logins and logouts etc. be them successful or failed. The Audit Logger logs the event, the user responsible for it, an error message in case of an error, and also the before and after states where it makes sense (ex. in case of settings changes).

{% callout title="Note" %}
**Audit Logger does not log events or errors that are not the result of user interactions.**
{% /callout %}

Each log is categorized into four levels:

- **info:** the successful events are on this level
- **warning:** - (this level is currently not used)
- **error:** those events got this level that resulted in an error
- **fatal:** when any of the Audit Loggers disabled it generates a log on this level

{% image url="https://uploads.developerhub.io/prod/XX2D/5m94rdfz80qwo7fk67ej6bapaby6hvll0zm2pjuqwe8o9tmwrkd32797vjmp25is.png" /%}

## Log Details

On the right side of each log there is a page icon with the title “View log details”.

{% image url="https://uploads.developerhub.io/prod/XX2D/xq4n3dxrrug662i2g5jxzudu5upu9cqf3jkqlt26040aen69qmhi2ncf4cjnwq9p.png" /%}

Clicking on this will open the raw log in JSON format that contains more details. For example in case of a setting change the original and the new state.

{% image url="https://uploads.developerhub.io/prod/XX2D/z7horbizd1tv0alxmlg2wnx133sbmyr9jrvbsl1mtjm7nl2tqae3tcqti6k8s5ku.png" /%}

## Types of Audit Logger

There are multiple types of Audit Logger, each logging events for a designated part of the system.

### Admin

The Admin Audit Logger logs any event happening on the Admin Panel including changing settings, creating, modifying or deleting users or groups etc..

### Authentication

The Authentication Audit Logger logs any logins and logouts.

{% image url="https://uploads.developerhub.io/prod/XX2D/h65pri8tdxag56m2ovntu97aesy76mo3xgzsa0uthjpkp2dszygdpxcouoezrp2f.png" /%}

## Settings

At the **Admin Panel \> Setting \> Configurations \> Audit Logger** section, you can enable or disable the Audit Logger and adjust its TTL (Time-to-Live).

{% image url="https://uploads.developerhub.io/prod/XX2D/cmbj5ihqrf24t9i5gw7guo2by4y6f884680osuepakgdd50epnh0h7otyi3xjscd.png" /%}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[262] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`*_AUDIT_LOGGER_ENABLED `
{% /cell %}
{% cell %}
Enable or disable admin audit logging.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`*_AUDIT_LOGGER_TTL`
{% /cell %}
{% cell %}
Logging Time-to-Live (TTL) in seconds.
{% /cell %}
{% /row %}
{% /table %}

Each Audit Logger can be enabled/disabled here separately and can be set how many days each Audit Logger should keep its logs.

{% callout title="Note" %}
**All Audit Logger is enabled by default. When an Audit Logger is disabled, it generates a fatal level log about it.**
{% /callout %}

{% callout title="Note" %}
**Audit Logger logs cannot be deleted manually, instead it automatically deletes logs older then the determined days (default 180 days)**
{% /callout %}
