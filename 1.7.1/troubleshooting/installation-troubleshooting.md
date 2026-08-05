---
type: page
title: Installation troubleshooting
listed: true
description: 
index_title: Installation troubleshooting
hidden: true
keywords: 
tags: 
---

In case any issues arise after installation please check the logs. The most important places where logs are shown are accessed with the the following commands (try to look for lines beginning with \[ERROR\]):

`fsiolog`

`fsiologbroker `

`sudo service fsio status`

`sudo service fsiobroker status`

`sudo docker logs fsio`

## "Unfortunately, the application server "app\*" is not reachable"

In this case the issue is that the analyzer "fsio" is unable to start up or it is not found. At first try to stop both the "fsio" and the "fsiobroker" services, then start the "fsio" service first. Wait a minute or so and then start the "fsiobroker" service as well.If the issue persists, please check deeper into logs.

## Generally, file-permission related issues

Please investigate whether the folder mentioned in the error message is owned by the filescanio user. It can be done using the  `ls -la <path>` command. In case it’s not owned by that user, recursively own it with the following command:

`cd <parent path>`

`chown -R filescanio:filescanio <folder name>`
