---
type: page
title: Whitelist Configuration
listed: true
description: 
index_title: Whitelist Configuration
hidden: false
keywords: 
tags: 
---

If "skipWhitelistedFiles" is enabled in the broker (see broker.properties), any submitted file is first reputation checked against local and remote whitelists. All whitelist data/integrations are implemented at the analysis node. If preferred, whitelisted files may be analyzed, which will yield the same detailed information as for a regular analysis, except that the verdict will default to BENIGN (i.e. a file containing a lot of "potentially malicious" artifacts will still received the BENIGN verdict, as it is known to be non-malicious).
