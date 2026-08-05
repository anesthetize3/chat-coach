---
type: page
title: Collect logfiles
listed: true
description: 
index_title: Collect logfiles
hidden: false
keywords: 
tags: 
---

If you have some issue with your system, logs can help to find out what went wrong. You can collect webservice logs, fsBroker and fsTransform logs.

Navigate to */srv/backend* and run he following commands:

{% code %}
```bash
sudo docker-compose -f docker-compose.yml -f docker-compose.queue.yml -f docker-compose.nginx.yml logs --no-color --tail=1000 |& tee logs.txt
sudo journalctl --since today | grep "fsio"
```
{% /code %}

{% callout type="warning" title="Important!" %}
This is only available from version 1.7.3
{% /callout %}
