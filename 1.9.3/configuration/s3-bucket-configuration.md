---
type: page
title: S3 File Storage
listed: true
description: 
index_title: S3 File Storage
hidden: true
keywords: 
tags: 
---

By default, any sample submitted to the webservice is stored locally at:

`/srv/backend/src/storage/files/*`

Due to limited hard disc storage space, it is thus recommended to configure the webservice to use a S3 Bucket in AWS in combination with a tight retention policy of the Broker and Transform backend components. To configure the webservice, edit the file at:

`/home/filescanio/FileScanIO/launch_webservice.sh`

Set the appropriate storage mode and S3 settings:

`export FSIO_S3_ACCESS_KEY_ID=XXX`

`export FSIO_S3_SECRET_ACCESS_KEY=YYY`

`export FSIO_S3_REGION=eu-central-1`

`export FSIO_S3_BUCKET_NAME=filescanio-myinstance`

`export FSIO_DEFAULT_FILE_MANAGER=s3`

… and restart the webservice:

`sudo service fsioweb stop`

`sudo service fsioweb start`
