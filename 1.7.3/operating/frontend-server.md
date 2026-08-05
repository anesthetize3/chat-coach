---
type: page
title: Frontend server
listed: true
description: 
index_title: Frontend server
hidden: false
keywords: 
tags: 
---

This is where the fsWebservice / nginx webserver lives (as a docker container). This is how it should look typically:

{% image url="https://uploads.developerhub.io/prod/XX2D/25mzx9q5f96yp3nlk1zuv6jia0o5gx71v857mq354jpml1x44uzm9pwsb7jtthnz.png" /%}

As the webservice has a variety of environment variables that have to be passed to the docker container, it is a requirement to use the following scripts (which are pre-populated) to start/stop the webservice:

`1 /home/filescanio/FileScanIO/launch_webservice.sh`

`2 /home/filescanio/FileScanIO/shutdown_webservice.sh`

---

**Database storage location**

`1 filescan@xyz:/data$ ls -al `

`2 total 16 `

`3 drwxr-xr-x  4 root root 4096 Jun 24  2021 . `

`4 drwxr-xr-x 20 root root 4096 Jul 25  2021 .. `

`5 drwxr-xr-x  3 root root 4096 Jun 24  2021 db `

`6 drwxr-xr-x  3 root root 4096 Jun 24  2021 graphdb`
