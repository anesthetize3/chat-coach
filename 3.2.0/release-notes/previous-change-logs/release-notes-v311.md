---
type: page
title: Release Notes for v3.1.1
listed: true
description: 
index_title: Release Notes for v3.1.1
hidden: false
keywords: 
tags: 
---

### Date: 27th May 2026

{% callout type="warning" title="Warning" %}
**Upgrading directly** from versions prior to 2.5.1 to 3.1.1 is **not possible!**

**Recommended Upgrade Path:** First upgrade to **2.5.1**, then install **3.1.1**.
{% /callout %}

## MetaDefender Aether™ v3.1.1 (including MetaDefender Sandbox™ capabilities)

MetaDefender Aether v3.1.1 provides database package updates via proxy and several minor enhancements.

### What’s New

- **Database Package Updates via Proxy -** Database packages can also be downloaded if the system connects to the Internet via a proxy server: [Database package updates](../../adminguide/database-package-updates.md)

### Improvements

- **Suppressed AV Misdetections for Demo Report -** The release artifact contained a demo report in JSON format that was incorrectly detected by some AV engines. This report has been encoded to suppress these misdetections.

### Bug Fixes

- **Fixed CEF Syslog Summary -** The broker component could not generate the CEF Syslog summary due to a data conversion issue.
