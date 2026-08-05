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

Palo Alto XSOAR is a security orchestration, automation and response (SOAR) platform, which allows security teams to automate and streamline security processes. By integrating **MetaDefender Sandbox** (previously known as OPSWAT Filescan Sandbox) with Palo Alto XSOAR, security teams can automate the process of scanning files for malware and other security threats. This integration allows security teams to quickly and easily scan files for potential threats, and take immediate action to mitigate any risks that are identified.

With the integration, you can send a file or URL scan request from XSOAR to Filescan, or search for previously scanned reports in Filescan.

You can find more information about XSOAR [here](https://www.paloaltonetworks.com/resources/datasheets/cortex-xsoar-overview).

MetaDefender Sandbox integration in the XSOAR marketplace available [here](https://cortex.marketplace.pan.dev/marketplace/details/OPSWATFilescan/).

## Installation

**Step #1** - Search for *OPSWAT Filescan* in the marketplace

{% image url="https://uploads.developerhub.io/prod/XX2D/h9r3s8bin6reyqbgr4xe0lrglguvz4z7jw082elxr9f9u8irbfymynfcaas95ftm.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/ahom2511fw1dqkxno1euojyjjv380q1f1ae93ru1jxrf5a0pkw4wm1pgvzn76v2t.png" /%}

**Step #2** - Click on the Install button in the top right corner.

Integration is then added to the basket. (The integration is free.)

{% image url="https://uploads.developerhub.io/prod/XX2D/g8bz7qf1svumwc05ukfx7j7g0771wttfrtvtwh995a83p5ymrqoyeyg59t5s887y.png" /%}

**Step #3** - Add an instance.

For that go to Settings -\> Integrations, search for '*OPSWAT*' and click on '*Add instance*' at the right side.

{% image url="https://uploads.developerhub.io/prod/XX2D/pac8w35sx060p8aeemktt94jcb502jkbyduy3cio9onag6aie6x1cyrbagvgwgb0.png" /%}

{% callout type="warning" title="Note" %}
A Filescan API key is required to use the integration.
{% /callout %}

You can use the Activation Key that you received from your OPSWAT Sales Representative, and follow the instructions on the [License Activation](https://docs.opswat.com/filescan/installation/license-activation) page or you can create an API key on the[ Community site](https://www.filescan.io/users/profile) under API Key tab.

{% image url="https://uploads.developerhub.io/prod/XX2D/j5uychucb9mum2qifeihffojv3bmg54hbcfid18fqipmppqe43ynvxxx667bkwuz.png" /%}

You need to add your API key, and if you have on-prem version of MetaDefender Sandbox, you can add your own server's URL. The default URL is the Filescan.io free community.

You can validate it under the 'Test results':

{% image url="https://uploads.developerhub.io/prod/XX2D/3hhplh6xxgkv6v2nj2oyi2sizqn5mke60vgssws0akuuhl549arqrd9pne6up3ik.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/nwqm38kfbdsbvigovxlt02xqzcimu4aaoxc3zsofwehfvsgqupr46rxgvm7dv7mc.png" /%}

## Available commands

### Scan URL

`opswat-filescan-scan-url`

Scan URL resource with Filescan [POST - Scan URL](/1.9.2/opswat-filescan/ref#scan-file-api-scan-url-post)

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

`!opswat-filescan-scan-url https://www.google.com`

#### Output example

{% image url="https://uploads.developerhub.io/prod/XX2D/iv0tmaec32yy5lfygv31qzlqopskyuejftlfichr062z00jmg6iwtwwe4xhubjm3.png" /%}

### Scan File

`opswat-filescan-scan-file`

Scan file resource with Filescan [POST - Scan File](/1.9.2/opswat-filescan/ref#scan-file-api-scan-file-post)

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

`!opswat-filescan-scan-file entry_id=<paste your entry id here> retry-interval=1`

#### Output example

{% image url="https://uploads.developerhub.io/prod/XX2D/rtbdlps1xbjlpp39n7q15vy6oufzj0y05n2su5zd1x2c4wg2htm90joxd0j2jn4o.png" /%}

### Search

`opswat-filescan-search-query`

Search for reports. Finds reports and uploaded files by various tokens. Use [GET - Search Report](/1.9.2/opswat-filescan/ref#search-report-api-reports-search-get) endpoint.

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

`!opswat-filescan-search-query query=theuselessweb limit=3`

#### Output example

{% image url="https://uploads.developerhub.io/prod/XX2D/5ir6e5bcx9alv6mfdpulz9dn0poypqr6ywn5w3dbnbvja3uc98gglggu0xob739m.png" /%}
