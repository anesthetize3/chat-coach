---
type: page
title: Scan files from input sources
listed: true
description: 
index_title: Scan files from input sources
hidden: false
keywords: 
tags: 
---

As the **OPSWAT Filescan Sandbox** platform has the ability to automatically monitor and scan files (e.g. E-Mail files on disc) from configurable input sources (network share, file on disc). For example: you could setup fsBroker to scan a “mail directory” and auto-forward any newly found E-Mail to one or multiple application servers.

{% callout type="warning" title="Warning" %}
**This integration currently only works in combination with the [CEF Syslog Feedback](https://app.developerhub.io/opswat-filescan-sandbox/1.9.0/configuration/cef-syslog-feedback), as generated reports will not appear in the webservice.**
{% /callout %}

Example: reading mail files from disc:

- Setup a postfix server on Ubuntu ([https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-20-04)). Make sure to use the “maildir” format, so that each E-Mail is stored in its own rfc822 file.
- Create an automatic BCC to your central “Scan Mailbox” (e.g. [scan@yourdomain.com](mailto:scan@yourdomain.com))
- Create an input source in broker, which points to the “Scan Mailbox” and hard deletes any processed files:

```
in1.path.Unix=/home/user/Maildir/new
in1.path.Windows=
in1.pollFrequency=5
in1.priority=100
in1.hardDeleteInputFiles=true
```

- Configure the "E-Mail Notification settings" section for automated notification
