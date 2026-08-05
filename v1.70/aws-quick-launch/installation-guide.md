---
type: page
title: Installation Guide
listed: true
description: 
index_title: Launching an EC2 instance from AMI baseline
hidden: false
keywords: 
tags: 
---

Please walk through the following steps to launch an EC2 instance from your AMI baseline:

**Step #1 - Right-click your AMI and select “Launch instance from image”**

{% image url="https://uploads.developerhub.io/prod/XX2D/4e16ipyk6t3kahvudct8k4jnx2xyy05peel1y4hfa33g7bgu9a4mk4rpg4j5vz4m.png" /%}

**Step #2 - Choose the appropriate instance type (see “Requirements”)**

{% image url="https://uploads.developerhub.io/prod/XX2D/325htm8loa1ksdbw8er0d3vjpnpgnhtt4ngxg3n9hkdhqeqsnvmnfjed0xsklf6k.png" /%}

**Step #3 - Create a security group that allows inbound SSH/HTTP/HTTPS access from your subnet (or in this case, from anywhere)**

{% image url="https://uploads.developerhub.io/prod/XX2D/chum1spul1f5da8vqsuqbeyses0vc2hdwoqy3c1ymtxvpqtj270t0vqaahtg0xt4.png" /%}

**Step #4 - Launch your instance and wait for the state to switch from “Pending” to “Running”**

{% image url="https://uploads.developerhub.io/prod/XX2D/sthfwsub070cftg31gcs8cofvo2hlt0kaiw908j4zdeapclklkb9f55gs1jmc51p.png" /%}

**Step #5 - The “Public IP” will be shown in the instance summary. You should be automatically redirected to HTTPS with a self-signed certificate**

{% image url="https://uploads.developerhub.io/prod/XX2D/hqa3tqmrk2mdl0gjs970yfv9s257dzf863l0lvtaqihhm3gnxe8zwbt6xfe79hzy.png" width=600 /%}

**Step #6 - Setup your initial administrator. To fine-tune the system settings, head to the webservice admin panel and/or SSH into your instance and configure the Broker/Transform component or webservice according to the user guidelines.**

{% image url="https://uploads.developerhub.io/prod/XX2D/3n4vndk16ef5sdha7yl7em0sk53qbn61rkslfi4k5qlp8mhrb8xqs1idnobh8q8y.png" width=300 /%}
