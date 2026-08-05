---
type: page
title: Do you offer a pure offline deployment/upgrade process?
listed: true
description: 
index_title: Do you offer a pure offline deployment/upgrade process?
hidden: false
keywords: 
tags: 
---

Unfortunately, not (yet).

OPSWAT Filescan (Sandbox) comes with hundreds of dependencies and multiple Docker containers that require an internet connection to download all of the interdependencies, machine-learning training data, latest threat indicators, etc. Here's an excerpt of the host level dependencies: [https://docs.opswat.com/filescan/datasheet/installed-packages-by-filescan](https://docs.opswat.com/filescan/datasheet/installed-packages-by-filescan)

However, we do support operating OPSWAT Filescan in an air-gapped environment. See the "Important notes for air-gapped systems" section on the installation page: [https://docs.opswat.com/filescan/installation/quick-installation](https://docs.opswat.com/filescan/installation/quick-installation)

In general, we recommend operating OPSWAT Filescan (Sandbox) in a DMZ with enabled internet connectivity, as it comes with a variety of advantages:

- Our automated background update jobs will give you the latest YARA rules to detect emerging threats in near real-time
- The "URL analysis" features for phishing detection requires internet to render URLs in a browser and capture all GET/POST requests
- Downloading \& analysing second stage payloads from extracted URLs requires an internet connection
- You extract more IOCs overall
