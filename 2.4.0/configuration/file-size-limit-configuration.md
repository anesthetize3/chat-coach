---
type: page
title: File size limit configuration
listed: false
description: 
index_title: File size limit configuration
hidden: true
keywords: 
tags: 
---

By default, the hardcoded file size limit is 2000MB per submission. This can be changed. However, file sizes above 2000MB are not supported. If you want to change the limit, please do the following changes:

In `/home/sandbox/sandbox/broker.cfg` add or modify this line:

`maxFileSizeInKilobytes=2097151`

In `/home/sandbox/sandbox/webservice/nginx/conf/production/default.conf`  modify:

`client_max_body_size 2000M;`

For set the `MAX_UPLOAD_SIZE` in the webservice please navigate Admin -\> Settings -\> Configuration -\> General:

{% image url="https://uploads.developerhub.io/prod/XX2D/9tiswkh1miqfn3n1nge3a5lkesyqpb58856rf2ua3tsmf16dxs2v5wqcj4t23ova.png" /%}

Now restar the sandbox service for the changes to take affect:

`sudo service sandbox restart`
