---
type: page
title: File size limit Configuration - Move to Operational Guide
listed: false
description: 
index_title: File size limit Configuration - Move to Operational Guide
hidden: true
keywords: 
tags: 
---

By default, the hardcoded file size limit is 2000MB per submission. This can be changed. However, file sizes above 2000MB are not supported. If you want to change the limit, please do the following changes:

In \~/FileScanIO/fsBroker/conf/broker.properties modify:

`maxFileSizeInKilobytes=2097151`

*Note: remember to move your custom changes to broker.properties.custom to persist it beyond system upgrades.*

In \~/FileScanIO/fsWebservice/nginx/conf/production/default.conf modify:

`client_max_body_size 2000M;`

For set the `MAX_UPLOAD_SIZE` in the webservice please navigate Admin -\> Settings -\> Configuration -\> General:

{% image url="https://uploads.developerhub.io/prod/XX2D/9tiswkh1miqfn3n1nge3a5lkesyqpb58856rf2ua3tsmf16dxs2v5wqcj4t23ova.png" /%}

Now restart both the broker and the webservice for the changes to take affect:

`sudo service fsiobroker stop`

`sudo service fsiobroker start`

`sudo ~/FileScanIO/shutdown_webservice.sh`

`sudo ~/FileScanIO/launch_webservice.sh`

*Note: if you’re in an offline environment, please rather use the following command to launch the webservice (instead of the one shown above):*

`sudo ~/FileScanIO/launch_webservice.sh --no-build`
