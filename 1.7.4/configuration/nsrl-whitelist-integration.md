---
type: page
title: NSRL Whitelist Integration
listed: true
description: 
index_title: NSRL Whitelist Integration
hidden: false
keywords: 
tags: 
---

In addition to local whitelists, it is possible to utilize a NSRL (National Software Reference Library) server, which is self-maintained and automatically updates itself with the latest hash sets. The NSRL whitelist integration is implemented at the broker, as it is effectively meant to be used as a pre-filter (see "skipWhitelistedFiles") to reduce the total number of analyses.

Please install a docker instance of cybagard/nsrllookup and configure the "Reputation settings" section of the broker. The successful configuration/setup can be tested by utilizing the /reputation endpoint of the broker (see "fsBroker API Documentation.pdf").

*Note: when using the logfile monitor service “Datadog” (dd-agent), a port conflict on port 5000/5001 may occur. In that case, change the “expvarport” and “cmd service datadog-agent restart).*
