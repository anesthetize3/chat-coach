---
type: page
title: Palo Alto - Cortex XSOAR
listed: true
description: 
index_title: Palo Alto - Cortex XSOAR
hidden: false
keywords: 
tags: 
---

Palo Alto XSOAR is a security orchestration, automation and response (SOAR) platform, which allows security teams to automate and streamline security processes. By integrating **MetaDefender Aether** (previously known as MetaDefender Sandbox) with Palo Alto XSOAR, security teams can automate the process of scanning files for malware and other security threats. This integration allows security teams to quickly and easily scan files for potential threats, and take immediate action to mitigate any risks that are identified.

With the integration, you can send a file or URL scan request from XSOAR to Aether, or search for previously scanned reports in Aether.

You can find more information about XSOAR [here](https://www.paloaltonetworks.com/resources/datasheets/cortex-xsoar-overview).

MetaDefender Aether integration in the XSOAR marketplace available [here](https://cortex.marketplace.pan.dev/marketplace/details/OPSWATMetaDefenderAether/).

## Installation

**Step #1** - Search for *MetaDefender Aether* in the marketpla

{% image url="../../assets/d57b81648c4f8256a427830c0c64264906b34054.png" /%}

{% image url="../../assets/1ea850a9f0f88c95c43dc1840d88da03dce5062e.png" /%}

**Step #2** - Click on the Install button in the top right corner.

Integration is then added to the basket. (The integration is free.)

{% image url="../../assets/4549cfbf5b02275f42246815d59f7fe9643b5382.png" /%}

**Step #3** - Add an instance.

For that go to Settings -\> Integrations, search for '*OPSWAT*' and click on '*Add instance*' at the right side.

{% image url="../../assets/235bbfcdbf795098fd90a7a740beb6a7defc1e18.png" /%}

{% callout type="warning" title="Note" %}
An Aether API key is required to use the integration.
{% /callout %}

You can use the Activation Key that you received from your OPSWAT Sales Representative, and follow the instructions on the [License Activation](https://docs.opswat.com/filescan/installation/license-activation) page or you can create an API key on the[ Community site](https://www.filescan.io/users/profile) under API Key tab.

{% image url="../../assets/f86def7cee7a88c10ac82d4b38ac76779f2e8ed1.png" /%}

You need to add your API key, and if you have on-prem version of MetaDefender Aether, you can add your own server's URL. The default URL is the Filescan.io free community.

You can validate it under the 'Test results':

{% image url="../../assets/06bf2f5b92002754c9762bda7358634fddf2e072.png" /%}

## Available commands

### Scan URL

`metadefender-aether-scan-url`

Scan URL resource with Aether  POST - Scan URL

#### Command Arguments

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
Required
{% /cell %}
{% /row %}
{% row %}
{% cell %}
url
{% /cell %}
{% cell %}
The URL to submit
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
timeout
{% /cell %}
{% cell %}
The timeout for the polling in seconds
{% /cell %}
{% cell %}
600
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
hide\_polling\_output
{% /cell %}
{% cell %}
Hide polling output.
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
description
{% /cell %}
{% cell %}
Uploaded file/url description
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
tags
{% /cell %}
{% cell %}
Tags array to propagate
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
password
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
is\_private
{% /cell %}
{% cell %}
If file should not be available for download by other users
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% /table %}

#### Command example

`!metadefender-aether-scan-url url=https://github.com`

#### Output example

{% image url="../../assets/01f47a753629678f26aa8ef9fe58114d2911ec25.png" /%}

### Scan File

`metadefender-aether-scan-file`

Scan file resource with Aether POST - Scan File

#### Command Arguments

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
Required
{% /cell %}
{% /row %}
{% row %}
{% cell %}
entry\_id
{% /cell %}
{% cell %}
The War Room entry ID of the file to submit.
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
timeout
{% /cell %}
{% cell %}
The timeout for the polling in seconds
{% /cell %}
{% cell %}
1200
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
hide\_polling\_output
{% /cell %}
{% cell %}
Hide polling output.
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
description
{% /cell %}
{% cell %}
Uploaded file/url description
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
tags
{% /cell %}
{% cell %}
Tags array to propagate
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
password
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
is\_private
{% /cell %}
{% cell %}
If file should not be available for download by other users
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% /table %}

#### Command example

`!metadefender-aether-scan-file entry_id=<paste your entry id here> retry-interval=1 password=infected`

#### Output example

{% image url="../../assets/0b9e2266ea197dbd58e9a4a4ff7840929ad10962.png" /%}

### Search

`metadefender-aether-search-query`

Search for reports. Finds reports and uploaded files by various tokens. Use GET - Search Report endpoint.

#### Arguments

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
Required
{% /cell %}
{% /row %}
{% row %}
{% cell %}
query
{% /cell %}
{% cell %}
The query string
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
page
{% /cell %}
{% cell %}
Page number, starting from 1
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
page\_size
{% /cell %}
{% cell %}
Page size. Can be 5, 10 or 20
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
limit
{% /cell %}
{% cell %}
Number of total results. Maximum 50. (If page and page\_size was also provided, then it will be ignored.)
{% /cell %}
{% cell %}
10
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% /table %}

#### Command example

`!metadefender-aether-search-query query=https://theuselessweb.com/ limit=10`

#### Output example

{% image url="../../assets/b85b3d9919bdabd7120d31c0890971713eb9e434.png" /%}

## Compatibility

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[199] %}
Integration name
{% /cell %}
{% cell header=true colwidth=[94] %}
Version
{% /cell %}
{% cell header=true %}
Sandbox 1.9.\*
{% /cell %}
{% cell header=true colwidth=[109] %}
Sandbox 2.0.0 - 2.1.0
{% /cell %}
{% cell header=true %}
Aether 1.0.0-
{% /cell %}
{% /row %}
{% row %}
{% cell %}
OPSWAT-Filescan (deprecated)
{% /cell %}
{% cell %}
`1.*.*`
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
OPSWAT-MetaDefender-Sandbox (deprecated)
{% /cell %}
{% cell %}
1\.0.0
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
OPSWAT-MetaDefender-Sandbox (deprecated)
{% /cell %}
{% cell %}
1\.0.1
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}

\*not recommended
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MetaDefender Aether
{% /cell %}
{% cell %}
1\.0.0
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% /table %}
