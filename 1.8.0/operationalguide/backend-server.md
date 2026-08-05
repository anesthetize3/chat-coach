---
type: page
title: Backend Server
listed: true
description: 
index_title: Backend Server
hidden: true
keywords: 
tags: 
---

**Sandbox Engine**

The sandbox engine (fsTransform) lives on the backend server and also utilizes a few services, which should always be running in the background. Specifically, the URL analysis engine and a NSRL whitelist lookup service. This is how it should typically look:

{% image url="https://uploads.developerhub.io/prod/XX2D/k8qqfkristqwil3tnrnao2a89c8r30tgeo3hwersh7nqa7z82lqjsbino1fobmic.png" /%}

---

**Broker Service**

The broker runs as the “fsiobroker” service and should be looking like this:

{% image url="https://uploads.developerhub.io/prod/XX2D/jhih4ttu5s1ui21wpygmxklxp1x23u6gczql8mje62p5av8hswj8xziwvibl263i.png" /%}

---

**Sandbox Service**

The analyzer runs as the “fsio” service and should be looking like this:

{% image url="https://uploads.developerhub.io/prod/XX2D/9mf9ujis1lqqhx1lrzcufpij0iotsnyr8sael3gwkpuujmg11c6efetvzk275hnc.png" /%}

---

**Restarting the Broker/Sandbox Engine**

`sudo service fsio stop`

`sudo service fsio start`

`sudo service fsiobroker stop`

`sudo service fsiobroker start`

---

**Verifying the status of the Broker/Sandbox Engine**

The broker/sandbox engine have port 22001 and 23001 open:

{% image url="https://uploads.developerhub.io/prod/XX2D/j8848dn8s6p3cbx750rteqqex7bdl9b7dybur0k4tp7qv6o7kbqqlax5tk0rq09u.png" /%}
