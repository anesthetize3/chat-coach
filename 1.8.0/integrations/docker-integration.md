---
type: page
title: Docker Integration
listed: true
description: 
index_title: Docker Integration
hidden: false
keywords: 
tags: 
---

It is possible to run the transform processor node in its own docker container. To build a docker image, deploy the system using the bootstrap process (see Quick Installation), configure it to your liking, navigate to the root folder and run:

`docker-compose -f docker-compose.yml build --force-rm`

`docker-compose -f docker-compose.yml up -d`
