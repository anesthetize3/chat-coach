---
type: page
title: Multi-Server Deployment
listed: true
description: 
index_title: Multi-Server Deployment
hidden: false
keywords: 
tags: 
---

Should the throughput requirement exceed 25K samples/day, then a typical single-server sandbox deployment is not sufficient anymore. For these cases, a multi-server deployment is necessary. The following diagram gives an idea of how such an architecture may look like:

{% image url="https://uploads.developerhub.io/prod/XX2D/2ygws7j7h4dwelocbw4mw17epwcnqcc0zi4weirsct2tl5vdvshddysyja9x13wr.png" /%}

Basically, the idea is that the webservice and broker are installed on a single "frontend" server and the transformer (analysis nodes) are deployed on individual, additional servers. As the broker can be configured to forward incoming files to multiple remote analysis nodes, it is possible to scale throughput if needed. Please consult professional services for assistance and license requirements.
