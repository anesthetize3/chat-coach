---
type: page
title: About logging commands
listed: true
description: 
index_title: About logging commands
hidden: false
keywords: 
tags: 
---

"fsiolog" and "fsiologbroker" are commands to view a colored version of the services’ output. It is an alias added to the \~/.bashrc that executes the following commands:

`alias fsiolog='sudo multitail -D -n 1000 -cS fsio -l "journalctl -f -u fsio"'`

and

`alias fsiologbroker='sudo multitail -D -n 1000 -cS fsio -l "jour-nalctl -f -u fsiobroker"'`
