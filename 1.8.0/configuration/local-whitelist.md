---
type: page
title: Local Whitelist
listed: true
description: 
index_title: Local Whitelist
hidden: true
keywords: 
tags: 
---

The local whitelists are stored in the fsTransform/external folder, specifically:

- `whitelist_certificate_owners.txt`
- `whitelist_hashes.txt`
- `whitelist_iocs.txt`
- `whitelist_generated_hashes.txt`

The generated hashes file contains MD5, SHA-1, SHA-256, SHA-512 hashes which are used to reduce noise from false positive IOC detections. If you would like to add your own whitelist files (one hash per line), please add additional filenames to the filename list of the **whitelistHashesFiles** option and add that to transform.properties.custom.

*Note: it is important to set any custom option values in the .custom properties file, so that the upgrade process will not "reset" any configuration file changes (as would be the case when editing the default files), as the .custom property files remain untouched.*
