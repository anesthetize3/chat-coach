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

Should the throughput requirement exceed 25K samples/day, then a typical single-server sandbox deployment is not sufficient anymore. For these cases, a multi-server deployment is necessary. The following diagram gives an idea of how such an architecture may look like:

{% image url="https://uploads.developerhub.io/prod/XX2D/2ygws7j7h4dwelocbw4mw17epwcnqcc0zi4weirsct2tl5vdvshddysyja9x13wr.png" /%}

Basically, the idea is that the webservice and broker are installed on a single "frontend" server (main node) and the transform engine is deployed on multiple "analysis nodes" (according to the required throughput). As the broker can be configured to forward incoming files to multiple remote analysis nodes, it is possible to scale throughput as needed.

To achieve the above architecture make sure that the analysis nodes are able to communicate with the main node. Please apply the following additional steps during the install process:

**Step #1 - Install analysis nodes**

Install 2 or more analysis nodes on different servers. Follow the [Quick Install guide](https://docs.opswat.com/filescan/installation/quick-installation) and before starting the *bootstrap.sh* script, locate the following lines in *bootstrap.cfg* and change them as follows:

{% code %}
```bash {% title="bootstrap.cfg" %}
FileScanIOBroker_Install=false
FileScanIOWebservice_Install=false
```
{% /code %}

Run the install script, only fsTransform is going to be installed. To make sure that the process was successful, please run:

{% code %}
```bash
sudo service fsio status
```
{% /code %}

Repeat this step on each analysis node.

**Step #2 - Install main node**

Install main node (databases, fsBroker, fsWebservice) on a  separate server. Follow the [Quick Install guide](https://docs.opswat.com/filescan/installation/quick-installation) and before starting the *bootstrap.sh* script, locate the following line in *bootstrap.cfg* and change it as follows:

{% code %}
```bash {% title="bootstrap.cfg" %}
FileScanIO_Install=false
```
{% /code %}

Run the install script, fsBroker and fsWebservice are going to be installed alongside with the databases. To make sure that the process was successful, please run:

{% code %}
```bash
sudo service fsiobroker status
```
{% /code %}

**Step #3 - Configure fsBroker**

Open `/home/filescanio/FileScanIO/fsBroker/conf/broker.properties.custom` using a text editor and add the following lines (to match the desired architecture and the number of analysis nodes):

{% code %}
```bash {% title="broker.properties.custom" %}
applicationServers=app1,app2

app1.type=fsTransform
app1.host=<fsTransform1_IP_ADDRESS>
app1.protocol=https
app1.port=22001
app1.connectTimeout=30
app1.readTimeout=30
app1.submissionsPerMinute=120
app1.callbackProtocol=https
app1.callbackHost=$localIP
app1.callbackPort=$listenPort
app1.callbackFile=/store
app1.callbackSecret=$apiKey0.secret
app1.callbackDeleteTaskAfterProcessing=true
app1.secret=<fsTransform1_apikey> 

app2.type=fsTransform
app2.host=<fsTransform2_IP_ADDRESS>
app2.protocol=https
app2.port=22001
app2.connectTimeout=30
app2.readTimeout=30
app2.submissionsPerMinute=120
app2.callbackProtocol=https
app2.callbackHost=$localIP
app2.callbackPort=$listenPort
app2.callbackFile=/store
app2.callbackSecret=$apiKey0.secret
app2.callbackDeleteTaskAfterProcessing=true
app2.secret=<fsTransform2_apikey>
```
{% /code %}

`applicationServers=app1...appX`*,* where `X=<number-of-analysis-nodes>`

You can see 2 fsTransform instances in the above example, but you can add more, just make sure that they appear in the `applicationServers` list.

After saving your configuration, please restart fsBroker:

{% code %}
```bash
sudo service fsiobroker restart
```
{% /code %}

**Step #4 - Activate the analysis nodes**

Follow Step #9 of the [Quick Install guide](https://docs.opswat.com/filescan/installation/quick-installation) to add license keys and activate each analysis node.

Please make sure that your license covers the required quantity of instances, so you can use the same license key on all nodes!
