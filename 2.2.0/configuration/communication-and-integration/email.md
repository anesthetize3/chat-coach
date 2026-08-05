---
type: page
title: SMTP / Email
listed: true
description: 
index_title: SMTP / Email
hidden: true
keywords: 
tags: 
---

This tab allows Admins to configure their STMP server which sends automatic emails to their users.

These configuration parameters are used in applications or scripts where sending emails programmatically is required, such as in web applications, automated notification systems, or email clients. By setting these parameters correctly, the application can connect to an SMTP server, authenticate, and send emails on behalf of a specified sender

### Email tab

***Admin Panel \> Settings \> Configuration \> Email***

The instances that are **sent automatically to user** via STMP emails can be due to:

- Sign-up confirmation email
- Resetting password

The [following tab](https://www.filescan.io/admin/settings/config) details the STMP server setup:

{% image url="https://uploads.developerhub.io/prod/XX2D/epvedup2jbl3hz99hildqlf5n7v0hxpju5ffh7chfm8dalvggmxx7l17ewmqtgm1.png" /%}

### Configuration options

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[280] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`EMAIL_SENDER_ADDRESS`
{% /cell %}
{% cell %}
Email address that the automatic emails are being sent from to the users
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`USE_SMTP`
{% /cell %}
{% cell %}
Whether the organization or the admin is using SMTP server or not. Simple Mail Transfer Protocol (SMTP) should be used for sending emails. SMTP is the standard protocol for sending emails across the Internet and it is preferred by OPSWAT as well. ***Library used for sending emails if SMTP server is not configured:*** ***sendmail***
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SMTP_HOST`
{% /cell %}
{% cell %}
This specifies the hostname or IP address of the SMTP (outgoing mail) server that will be used to send the emails.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SMTP_PORT`
{% /cell %}
{% cell %}
This specifies the port number on the SMTP server to connect to for sending emails. Common ports used for SMTP are 25, 587, or 465
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SMTP_USER`
{% /cell %}
{% cell %}
This is the username or account name used to authenticate with the SMTP server if authentication is required. This could be an email address or a specific username provided by the SMTP server.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SMTP_PASS`
{% /cell %}
{% cell %}
This is the password associated with the SMTP\_USER account. It is used for authentication when connecting to the SMTP server to send emails securely.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
`SMTP_SECURITY`
{% /cell %}
{% cell %}
This setting determines the type of security to use when connecting to the SMTP server. Possible values might include:

- `none`: No encryption or security.
- `ssl`: Use SSL/TLS encryption on a dedicated SSL port (e.g., port 465).
- `tls`: Use STARTTLS command to switch the connection to a TLS-encrypted one (usually on port 587).
{% /cell %}
{% /row %}
{% /table %}
