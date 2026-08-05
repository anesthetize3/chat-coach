---
type: page
title: Release Notes for v2.2.1
listed: true
description: 
index_title: Release Notes for v2.2.1
hidden: false
keywords: 
tags: 
---

## Date: 7 March, 2025

{% callout type="warning" title="Warning" %}
It is recommended for all users to upgrade to this release to benefit from the latest **security enhancements**!
{% /callout %}

**Improvements**

- **URL Length Limit**: Extended the maximum length of analyzed URLs from 1024 to 2048 characters to align with the URL length limit used by modern browsers.
- **Extended Certificate Issuer Whitelist**: We have substantially extended the built-in list of whitelisted certificate issuers, improving the scan verdict for files that are signed by reputable vendors.

**Bug Fixes**

- **Strengthened PowerShell Emulation**: Addressed a security issue where certain .NET DLLs could be loaded within the emulated PowerShell environment, bypassing instrumentation (execution remained contained within the hardened Docker container). This fix enhances detection and prevents the unauthorized DLL loading during PowerShell emulation.
- **Scan Profile Selection:** Resolved an issue with selecting scan profiles for some users. Basic scanning can be enabled for guest users in the Admin Panel, guest scan requests will use the default Analysis profile.
