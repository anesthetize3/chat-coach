---
type: page
title: Automatically Scan E-Mails
listed: true
description: 
index_title: Automatically Scan E-Mails
hidden: true
keywords: 
tags: 
---

As the **OPSWAT Filescan** engine has extensive E-Mail (msg, eml/rfc822) support, it is possible to automatically monitor and scan new E-Mails of any number of E-Mail inboxes. The basic idea is to setup fsBroker to scan a “mail directory” and auto-forward any newly found E-Mail to one or multiple application servers.

Steps to take:

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
