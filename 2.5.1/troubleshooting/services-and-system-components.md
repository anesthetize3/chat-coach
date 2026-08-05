---
type: page
title: Services and System Components
listed: true
description: 
index_title: Services and System Components
hidden: true
keywords: 
tags: 
---

## Sandbox Service

The Sandbox service consists of several Docker containers that implement different components of the system.

Internally, `docker compose` is used to manage all containers and networks in Docker.

The `sudo docker ps`  command can be used to check the status of these containers. This is how the list of containers should look typically:

{% image url="https://uploads.developerhub.io/prod/XX2D/rwj9qg8aeqa9reve9axhjl8743rnylm0d81f4di2p9vnebej68te628wololquft.png" /%}

It is important to check if the following critical containers are listed and healthy:

- webservice
- nginx/reverse\_proxy
- redis
- mongodb
- arangodb/graphdb
- broker
- transform

The logs for each container can be displayed in real time, e.g.:

{% code %}
```bash
docker logs -f broker
```
{% /code %}

The following helper scripts should be used to start/stop the `sandbox` service (including all containers):

{% code %}
```bash
/home/sandbox/sandbox/stop_sandbox.sh
/home/sandbox/sandbox/start_sandbox.sh
```
{% /code %}

It is also possible to interact with the `sandbox` service as a system service (this will produce very little output):

{% code %}
```bash
sudo service sandbox stop
sudo service sandbox start
```
{% /code %}

Additional commands are available to restart all components, or the broker and transform selectively:

{% code %}
```bash
sudo service sandbox restart
sudo service sandbox restart-broker
sudo service sandbox restart-transform
```
{% /code %}

## Database storage location

The MongoDB (db) and ArangoDB (graphdb) database files are stored in the `/data` directory:

{% image url="https://uploads.developerhub.io/prod/XX2D/xpqoaujuu7jj8eh9dmk7fpsku4wpxmbjuh21tg978fapzlebld936nxls52l4zwt.png" /%}

---
