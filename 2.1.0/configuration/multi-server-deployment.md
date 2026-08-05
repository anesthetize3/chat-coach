---
type: page
title: Multi-Server Deployment
listed: true
description: 
index_title: Multi-Server Deployment
hidden: true
keywords: 
tags: 
---

{% callout title="Info" %}
A multi-server deployment can provide **increased throughput**, but it is NOT designed to be a High-Availability deployment (as the "main node" remains a Single Point of Failure in this system).
{% /callout %}

Should the throughput requirement exceed 25K samples/day, then a typical single-server sandbox deployment is not sufficient anymore. For these cases, a multi-server deployment is necessary. The following diagram gives an idea of how such an architecture may look like:

{% image url="https://uploads.developerhub.io/prod/XX2D/8j49yzz5kvwll7ah067gkcjlox1s2b7ins9nd94lzseq7t97ht2qv1p101s5gm88.png" /%}

Basically, the idea is that the webservice and broker are installed on a single "frontend" server (main node) and the transform engine is deployed on multiple "analysis nodes" (according to the required throughput). As the broker can be configured to forward incoming files to multiple remote analysis nodes, it is possible to scale throughput as needed.

To achieve the above architecture make sure that the analysis nodes are able to communicate with the main node. Please apply the following additional steps during the install process:

**Step #1 - Install analysis nodes**

Install 2 or more analysis nodes on different servers. Follow the [Quick Install guide](https://docs.opswat.com/filescan/installation/quick-installation) and before starting the `install.sh` script, locate the following lines in `install.cfg` and change them as follows:

{% code %}
```bash {% title="install.cfg" %}
SandboxBroker_Install=false
SandboxWebservice_Install=false
```
{% /code %}

Run the install script, only transform is going to be installed. To make sure that the process was successful, please run:

{% code %}
```bash
sudo service sandbox status
```
{% /code %}

Repeat this step on each analysis node.

**Step #2 - Install main node**

Install main node (databases, broker, webservice) on a  separate server. Follow the [Quick Install guide](https://docs.opswat.com/filescan/installation/quick-installation) and before starting the *install.sh* script, locate the following line in `install.cfg` and change it as follows:

{% code %}
```bash {% title="install.cfg" %}
SandboxTransform_Install=false
```
{% /code %}

Run the install script, broker and webservice are going to be installed alongside with the databases. To make sure that the process was successful, please run:

{% code %}
```bash
sudo service sandbox status
```
{% /code %}

**Step #3 - Configure broker**

Open `/home/sandbox/sandbox/broker.cfg` using a text editor and add the following lines (to match the desired architecture and the number of analysis nodes):

{% code %}
```bash {% title="broker.cfg" %}
applicationServers=app1,app2,app3

app1.type=fsTransform
app1.host=<transform1_IP_ADDRESS>
app1.protocol=https
app1.port=22001
app1.connectTimeout=30
app1.readTimeout=30
app1.secret=<transform1_apikey>
app1.submissionsPerMinute=120
app1.callbackProtocol=https
app1.callbackHost=<broker_IP_ADDRESS>
app1.callbackPort=$listenPort
app1.callbackFile=/store
app1.callbackSecret=$apiKey0.secret
app1.callbackDeleteTaskAfterProcessing=true

app2.type=fsTransform
app2.host=<transform2_IP_ADDRESS>
app2.protocol=https
app2.port=22001
app2.connectTimeout=30
app2.readTimeout=30
app2.secret=<transform2_apikey>
app2.submissionsPerMinute=120
app2.callbackProtocol=https
app2.callbackHost=<broker_IP_ADDRESS>
app2.callbackPort=$listenPort
app2.callbackFile=/store
app2.callbackSecret=$apiKey0.secret
app2.callbackDeleteTaskAfterProcessing=true

app3.type=fsTransform
app3.host=<transform3_IP_ADDRESS>
app3.protocol=https
app3.port=22001
app3.connectTimeout=30
app3.readTimeout=30
app3.secret=<transform3_apikey>
app3.submissionsPerMinute=120
app3.callbackProtocol=https
app3.callbackHost=<broker_IP_ADDRESS>
app3.callbackPort=$listenPort
app3.callbackFile=/store
app3.callbackSecret=$apiKey0.secret
app3.callbackDeleteTaskAfterProcessing=true
```
{% /code %}

`applicationServers=app1...appX`*,* where `X=<number-of-analysis-nodes>`

You can see 3 transform instances in the above example, but you can add more, just make sure that they appear in the `applicationServers` list.

Please **make sure to update** the following values for each app:`host, secret, callbackHost`

After saving your configuration, please restart broker:

{% code %}
```bash
sudo service sandbox restart
```
{% /code %}

**Step #4 - Activate the analysis nodes**

Follow Step #8 of the [Quick Install guide](https://docs.opswat.com/filescan/installation/quick-installation) to add license keys and activate each analysis node.

Please make sure that your license covers the required quantity of instances, so you can use the same license key on all nodes!
