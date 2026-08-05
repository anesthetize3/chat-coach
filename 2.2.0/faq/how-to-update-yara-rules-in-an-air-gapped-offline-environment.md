---
type: page
title: How to update YARA rules in an air-gapped/offline environment?
listed: true
description: 
index_title: How to update YARA rules in an air-gapped/offline environment?
hidden: true
keywords: 
tags: 
---

To update the YARA rule set in an air-gapped/offline Sandbox environment, please follow these steps:

- Search for the **latest release** in the fsYara GitHub repository: [https://github.com/filescanio/fsYara/releases](https://github.com/filescanio/fsYara/releases)
- Click on that release, and download the `master_file.yarc`  file from the **release assets**:

{% image url="https://uploads.developerhub.io/prod/XX2D/xn4v1arl9df5y49y4lrr8st6sx3g5uqps50tacvi5q51zkhst8katus03ut7ighf.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/2o5s3yp3ykq3e5rvvetwynzs1fgghtlawjagyhryp9xbt425vqcfi2pfg5uj5l7p.png" /%}

- Transfer the downloaded `master_file.yarc` to your offline environment (e.g. using a USB drive)
- Replace the current master file in `/home/sandbox/sandbox/transform/yara/rules/master_file.yarc` with the new master file, and ensure that the `sandbox` user owns the new file:

{% code %}
```bash
cd /PATH/TO/YOUR/USB-DRIVE
sudo cp -f master_file.yarc /home/sandbox/sandbox/transform/yara/rules/master_file.yarc
sudo chown sandbox:sandbox /home/sandbox/sandbox/transform/yara/rules/master_file.yarc
```
{% /code %}

- Restart the `transform` component of the `sandbox` service, so the updated YARA rules are loaded into memory:

{% code %}
```bash
sudo service sandbox restart-transform
```
{% /code %}
