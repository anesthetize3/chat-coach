---
type: page
title: Archive unpack file limits
listed: true
description: 
index_title: Archive unpack file limits
hidden: true
keywords: 
tags: 
---

By default, the "fsBroker" component will apply certain limits to the total number of files which will be inspected inside of an archive (e.g. ZIP, ISO, CAB). They are configured in the \~/FileScanIO/fsBroker/conf/broker.properties configuration:

{% code %}
```json
maxSubmitFileCountForArchive=10000
maxSubmitFileCountForArchiveExecutables=100
maxSubmitFileCountForArchiveDocuments=10
maxSubmitFileCountForArchiveOther=10
```
{% /code %}

*Note: document files are PDF/Office files and executables Windows PE files.*

After changing the settings, please restart the broker to make them take effect:

{% code %}
```json
sudo service fsiobroker stop && sudo service fsiobroker start
```
{% /code %}
