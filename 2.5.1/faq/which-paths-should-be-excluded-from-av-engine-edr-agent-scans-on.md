---
type: page
title: Which paths should be excluded from AV engine/EDR agent scans on the Sandbox server?
listed: true
description: 
index_title: Which paths should be excluded from AV engine/EDR agent scans on the Sandbox server?
hidden: true
keywords: 
tags: 
---

It is not recommended to install an AV engine or EDR agent on the Sandbox server, unless it is a strict policy requirement within an organization.

If an EDR agent or AV engine is installed without proper configuration, then the Sandbox system simply cannot receive and analyze files that are flagged by the EDR agent or AV engine.

The following folders **must be excluded** in the EDR agent or AV engine:

- The Sandbox installation folder ( `/home/sandbox/sandbox` by default)
- `/var/lib/docker`
- `/data/db`
- `/data/graphdb`
