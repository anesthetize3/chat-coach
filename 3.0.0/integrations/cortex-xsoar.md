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

MetaDefender Aether integration in the XSOAR marketplace available [here](https://cortex.marketplace.pan.dev/marketplace/details/OPSWATMetaDefenderSandbox/).

## Installation

**Step #1** - Search for *MetaDefender Sandbox* in the marketplace

{% image url="https://uploads.developerhub.io/prod/XX2D/ryffrxdk4k6lljhzy2eylhx7bqpw6nnjuit95zqrp04yoex4s109aw2xrs3l1zkx.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/fkm2mbrpq5rg072w31eg2s4xg8p6qqe3slijzbod7a1a0h5lev6etyd2zdpfgs8g.png" /%}

**Step #2** - Click on the Install button in the top right corner.

Integration is then added to the basket. (The integration is free.)

{% image url="https://uploads.developerhub.io/prod/XX2D/7no48scjzd3sabcexoqe6utbdqzsfqaaji5gnmtrlarex9ig6feod1obhpkmol45.png" /%}

**Step #3** - Add an instance.

For that go to Settings -\> Integrations, search for '*OPSWAT*' and click on '*Add instance*' at the right side.

{% image url="https://uploads.developerhub.io/prod/XX2D/8xr9ou3xg9fm5ddo54e96a0sgpg3zv880tigfqfw9hz1jae9esirr7h6ahdsrrfg.png" /%}

{% callout type="warning" title="Note" %}
A Sandbox API key is required to use the integration.
{% /callout %}

You can use the Activation Key that you received from your OPSWAT Sales Representative, and follow the instructions on the [License Activation](https://docs.opswat.com/filescan/installation/license-activation) page or you can create an API key on the[ Community site](https://www.filescan.io/users/profile) under API Key tab.

{% image url="https://uploads.developerhub.io/prod/XX2D/pu42aez63y8t7cwis6g8y03krpn2tdd9adnfc6bm3dcale9qypzk3203fz88mssz.png" /%}

You need to add your API key, and if you have on-prem version of MetaDefender Sandbox, you can add your own server's URL. The default URL is the Filescan.io free community.

You can validate it under the 'Test results':

{% image url="https://uploads.developerhub.io/prod/XX2D/btmr8jdt4xq6hcdhwra9w0qso51dric6b7w5zv2ei90zfbkl842uaghn6ftddl6d.png" /%}

## Available commands

### Scan URL

`metadefender-sandbox-scan-url`

Scan URL resource with Sandbox  POST - Scan URL

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

`!metadefender-sandbox-scan-url https://www.google.com`

#### Output example

{% image url="https://uploads.developerhub.io/prod/XX2D/8bzvu6ty4kqux7xcmi4t5k9rnyxf6lyg71zplphen8j94qfppoz1x82sk7ceitvu.png" /%}

### Scan File

`metadefender-sandbox-scan-file`

Scan file resource with Sandbox POST - Scan File

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

`!metadefender-sandbox-scan-file entry_id=<paste your entry id here> retry-interval=1`

#### Output example

{% image url="https://uploads.developerhub.io/prod/XX2D/ympj4zmrur223r8kyznn8nc135mewwp77twsb3bxrj4zcvxqn4n79dz6642cgvhj.png" /%}

### Search

`metadefender-sandbox-search-query`

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

`!metadefender-sandbox-search-query query="google" limit=3`

#### Output example

{% image url="https://uploads.developerhub.io/prod/XX2D/1bo24s5vl3o1n38zodfwysw0k0eqxzsu9hfq0yvd89jsj3ej2met7lebkp4avqrz.png" /%}

## Compatibility

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Integration name
{% /cell %}
{% cell header=true %}
Version
{% /cell %}
{% cell header=true %}
Sandbox 1.9.\*
{% /cell %}
{% cell header=true %}
Sandbox 2.0.0 - 2.1.0
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
{% /row %}
{% row %}
{% cell %}
OPSWAT-MetaDefender-Sandbox
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
{% /row %}
{% row %}
{% cell %}
{% p /%}
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
{% /row %}
{% /table %}
