---
type: page
title: Logging
listed: true
description: 
index_title: View logfiles
hidden: true
keywords: 
tags: 
---

Use the "fsiolog" command to view a colored version of the output. It is an alias added to the \~/.bashrc that executes the following command:

`alias fsiolog=’sudo multitail -D -n 1000 -cS fsio -l “journalctl -f -u fsio”’`
