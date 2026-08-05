---
type: page
title: Assemblyline 4
listed: true
description: 
index_title: Assemblyline 4
hidden: false
keywords: 
tags: 
---

[Assemblyline 4](https://github.com/CybercentreCanada/assemblyline)  is a scalable file triage and malware analysis system integrating some of the cyber security community's tools.

With the integration, you can send a file or URL scan request from [Assemblyline 4](https://github.com/CybercentreCanada/assemblyline) to [Filescan Sandbox](https://docs.opswat.com/filescan/datasheet).

The source code of the integration is available [here](https://github.com/OPSWAT/assemblyline-service-opswat-filescan-sandbox).

The docker image is available [here](https://hub.docker.com/r/opswat/assemblyline-service-opswat-filescan-sandbox).

## Installation

In Assemblyline4 go to Administration -\> Services and click on the green plus button (add service):

{% image url="https://uploads.developerhub.io/prod/XX2D/70ai2q460umy3ciz8y4524i1rzgg98r92hqe9qaisknhil1bx7ka9j5hf08udlp9.png" /%}

Paste the [service manifest](https://github.com/OPSWAT/assemblyline-service-opswat-filescan-sandbox/blob/main/service_manifest.yml) on the pup-up window:

{% code %}
```yaml {% title="Service manifest for 4.4.1.dev0" %}
# Name of the service
name: OPSWAT_Filescan_Sandbox
# Version of the service
version: 4.4.1.dev0

description: This Assemblyline service interfaces with the OPSWAT Filescan Sandbox, detonating files and URLs. This integration was developed by OPSWAT. (C) OPSWAT, Inc.

accepts: .*
rejects: empty

stage: CORE
category: Dynamic Analysis

file_required: true
timeout: 600

# is the service enabled by default
enabled: true

uses_metadata: true

# -1000: safe
# 0 - 299: informational
# 300 - 699: suspicious
# 700 - 999: highly suspicious
# >= 1000: malicious

heuristics:
  - description: OPSWAT Filescan Sandbox determined that the file is benign.
    filetype: "*"
    heur_id: 1
    name: Filescan Sandbox verdict is benign.
    score: -1000
  - description: OPSWAT Filescan Sandbox signal group is benign.
    filetype: "*"
    heur_id: 2
    name: Benign threat indicators
    score: -1000
  - description: OPSWAT Filescan Sandbox determined that the file is informational/no threat.
    filetype: "*"
    heur_id: 3
    name: Filescan Sandbox verdict is no threat.
    score: 150
  - description: OPSWAT Filescan Sandbox signal group is informational/no threat.
    filetype: "*"
    heur_id: 4
    name: Informational threat indicators
    score: 150
  - description: OPSWAT Filescan Sandbox determined that the file is unknown.
    filetype: "*"
    heur_id: 5
    name: Filescan Sandbox verdict is unknown
    score: 299
  - description: OPSWAT Filescan Sandbox signal group is unknown.
    filetype: "*"
    heur_id: 6
    name: Unknown threat indicators
    score: 299
  - description: OPSWAT Filescan Sandbox determined that the file is suspicious.
    filetype: "*"
    heur_id: 7
    name: Filescan Sandbox verdict is suspicious
    score: 500
  - description: OPSWAT Filescan Sandbox signal group is suspicious.
    filetype: "*"
    heur_id: 8
    name: Suspicious threat indicators
    score: 500
  - description: OPSWAT Filescan Sandbox determined that the file is likely malicious.
    filetype: "*"
    heur_id: 9
    name: Filescan Sandbox verdict is likely malicious
    score: 850
  - description: OPSWAT Filescan Sandbox signal group is likely malicious.
    filetype: "*"
    heur_id: 10
    name: Likely malicious threat indicators
    score: 850
  - description: OPSWAT Filescan Sandbox determined that the file is malicious.
    filetype: "*"
    heur_id: 11
    name: Filescan Sandbox verdict is malicious
    score: 1000
  - description: OPSWAT Filescan Sandbox signal group is malicious.
    filetype: "*"
    heur_id: 12
    name: Malicious threat indicators
    score: 1000

# Docker configuration block which defines:
#  - the name of the docker container that will be created
#  - CPU and ram allocation by the container
docker_config:
  image: ${REGISTRY}opswat/assemblyline-service-opswat-filescan-sandbox:4.4.1.dev0
  cpu_cores: 1.0
  ram_mb: 1024
  allow_internet_access: true

config:
  api_key: ""
  host:  "https://www.filescan.io"
  poll_interval: 2
  timeout: 60

submission_params:
  - default: ""
    name: api_key
    type: str
    value: ""
  - default: 2
    name: poll_interval
    type: int
    value: 2
  - default: 60
    name: timeout
    type: int
    value: 60
  - default: ""
    name: description
    type: str
    value: ""
  - default: ""
    name: password
    type: str
    value: ""
  - default: ""
    name: is_private
    type: bool
    value: ""
```
{% /code %}

{% callout type="warning" title="Note" %}
If you use the yml file from github, please change the $SERVICE\_TAG vaiable everywhere to the actual docker tag. (Now it's 4.4.1.dev0)
{% /callout %}

Click on Add button on the bottom left.

After installation, you will find the service within the loaded services. Ensure that it has been enabled:

{% image url="https://uploads.developerhub.io/prod/XX2D/3l7ex3aky0lyaalx1klgm1hu5ln5rejydehatvdn8zsfn82hzcncnn9piqtsehiw.png" /%}

## Configuration

On the service details panel you can set the submission parameters and the service variables.

### Service variables

The service variables are the follows:

{% table layout="auto" %}
{% row %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
required
{% /cell %}
{% /row %}
{% row %}
{% cell %}
api-key
{% /cell %}
{% cell %}
Filescan Sandbox api-key
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
host
{% /cell %}
{% cell %}
Sandbox host
{% /cell %}
{% cell %}
[https://www.filescan.io](https://www.filescan.io)
{% /cell %}
{% cell %}
yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
poll-interval
{% /cell %}
{% cell %}
Submission polling interval
{% /cell %}
{% cell %}
2
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
timeout
{% /cell %}
{% cell %}
Submission polling timeout
{% /cell %}
{% cell %}
60
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% /table %}

{% inline-image url="asset:p8zeyhszj2ts" /%}

{% callout type="warning" title="Note" %}
A Filescan API key is required to use the integration.
{% /callout %}

You can use the Activation Key that you received from your OPSWAT Sales Representative, and follow the instructions on the [License Activation](https://docs.opswat.com/filescan/installation/license-activation) page or you can create an API key on the[ Community site](https://www.filescan.io/users/profile) under API Key tab.

You need to add your API key, and if you have on-prem version of OPSWAT Filescan, you can add your own server's URL. The default URL is Filescan Community.

After saving the settings you can use the service.

### Submission parameters

{% callout type="warning" title="Important" %}
To use the service, you must select the `OPSWAT_Filescan_Sandbox` service under the settings menu when submitting a file or a URL. You can found it under the Dynamic Analysis section:
{% /callout %}

{% inline-image url="../../assets/5b188c4f115b1d41326f67b3d8ce948d8e3732ad.png" /%}

Under the Service Specific Parameters section you can set the Filescsan Sandbox submission parameters:

{% inline-image url="../../assets/e8e5a684ad1614c7e5cea25325f6d9ae1d6eeb73.png" /%}

These parameters are:

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[129] %}
{% p /%}
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Required
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Api-Key \*
{% /cell %}
{% cell %}
Filescan Sandbox api-key
{% /cell %}
{% cell %}
Uses the service variable
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Poll-Interval \*
{% /cell %}
{% cell %}
Submission polling interval
{% /cell %}
{% cell %}
2
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Timeout \*
{% /cell %}
{% cell %}
Submission polling timeout
{% /cell %}
{% cell %}
60
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Description
{% /cell %}
{% cell %}
Uploaded file/URL description
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Password
{% /cell %}
{% cell %}
Custom password, in case uploaded archive is protected
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Is Private
{% /cell %}
{% cell %}
If file should not be available for download by other users
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% /table %}

\*In case that you would like to use different value than it was set  under the service variables.

## Available actions

### File scan

To scanning a file drag and drop the target file to the uploader area and click on 'UPLOAD AND SCAN' button:

{% inline-image url="asset:42j6c7jijvva" /%}

### URL/SHA256

To scan an URL, write the URL address to the field and click on SCAN button

{% inline-image url="asset:vgo9f6qvef2x" /%}

To scan a SHA256, copy the target file's SHA256 hash to the field.

{% callout type="warning" title="Note" %}
You can scan only that SHA256 what is exists in Assemblyline.
{% /callout %}

Result

After the scan is successfully performed, the main result will be visible with the most important informations:

{% inline-image url="../../assets/deec81925ccc4e2a2e9ac440f674a0869dafeec4.png" /%}

A summary report of the scan can be found under OPSWAT Filescan Sandbox result (heuristic):

{% inline-image url="asset:vvvmgu1ntjcv" /%}

Indicators are added in a subsections for heuristics:

{% inline-image url="asset:3etwep4a46xf" /%}

If any MITRE ATT\&CK was identified, it can be found under the ATT\&CK Matrix section:

{% inline-image url="../../assets/e3598ee0610fcad689e6cbdb0184126a556eee8f.png" /%}

If there were any parsable attributes in the result, they will appear under Attributions

{% inline-image url="../../assets/c551b4464331ac79588e31594ad7ed224491f0aa.png" /%}

IOCs were found under the Indicators of Compromise section:

{% inline-image url="../../assets/c355bca9fe4e6ae3929c0349fbc3097d4c2be62d.png" /%}

A more detailed report on the file is available by clicking on the links in the Files section:

{% inline-image url="../../assets/1353407613bc96c319e0568e7d8e0a6d989bc828.png" /%}

{% inline-image url="../../assets/d133aee75e2839d8e6c60ccd45d46202104926cf.png" /%}

Here you can found the generated tags:

{% inline-image url="../../assets/59233e10da7c753b0095fac5df6e0935bb9c9d4d.png" /%}

Furthermore, the link to the complete report is also available at your request below:

{% inline-image url="../../assets/ab14d4653559ee54661860a3ce7e2ba831d82d87.png" /%}

.
