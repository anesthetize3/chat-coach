---
type: page
title: License Activation
listed: true
description: 
index_title: License Activation
hidden: false
keywords: 
tags: 
---

## License restrictions

An activated and valid license deployment is necessary to access the full functionality of the product. Without such license it is not possible to start scan requests.

## License limitations

Scan limit: licenses contain a scan limit which defines the number of scans allowed daily. It is not possible to start new scan processes once the daily limit is depleted.

## Deployment ID

Product deployments are represented by a unique system fingerprint called `Deployment ID.`

Licensing is based on the generated deployment ID and a limited number of activations are possible for each license. Therefore every time your product is deployed with a different deployment ID, it will be captured as a different activation record accumulated into your total activations allowed.

Once the number of active deployments reached the deployment limit, new product activations are not possible.

{% callout type="warning" title="Notice" %}
The Deployment ID is an automatically generated unique fingerprint identifying the computer the product is deployed on. It might change when you alter the system that the product is installed on.
{% /callout %}

## License Actions

Navigate to *Admin panel \> Settings \> Integrations* tab and select *Licence Management*. You can find here the main license information and connected transform instances.

### Online license activation

Click on *Activate all*  (or *Activate*  for single instances) to open the activation dialog and select *Activate online*.

{% image url="https://uploads.developerhub.io/prod/XX2D/6uoghagm2o72lfmth1kq7rjndtz82bpa3sii3300g2pns1t8gezqrq1m0yf9mlfy.png" /%}

Fill in the license key text box with your license key and click on *Activate.* On success, the license of the selected instance becomes available, on error you will see a detailed error message.

### Offline license activation

In air-gapped environments the product can be activated with the help of another computer that has a working internet connection. The Deployment ID of the target computer and the Activation Key will be required to download an offline license file (.yml) via your [My OPSWAT](https://my.opswat.com/portal/products) portal. Follow the {% link href="https://my.opswat.com/portal/products(secondary:dialog-active)" %}displayed instructions{% /link %} for details.

#### Steps to activate offline

- Generate Deployment ID by executing the fsDeploymentID script, which can be found in the release package.
- Use your Activation Key and Deployment ID to download an offline license file from your {% link href="https://my.opswat.com/portal/products(secondary:dialog-active)" %}My OPSWAT{% /link %} portal.
- Navigate to the *License Management* page, open the activation dialog and select *Activate offline* .  Upload your license file and click on *Activate.*

{% image url="https://uploads.developerhub.io/prod/XX2D/kysibyjo959kfith46kvb7wkqy4m84deezbdf6owhc3phrd8oxcvoog6nplpod3u.png" /%}

On success, the license of the selected instance becomes available, on error you will see a detailed error message.

## Deactivation

Click on *Deactivate all* (or *Deactivate* for single instances) to open the deactivation dialog and review the instances to deactivate.

{% image url="https://uploads.developerhub.io/prod/XX2D/df3lximt3gun5snh45ho91d59ro3pzh8pxstedwe5mv4b1q5jnkj08odpobkgmxw.png" /%}

Click on *Deactivate.* On success, the license of the selected instance becomes unavailable, on error you will see a detailed error message.

## Troubleshooting

For online activation, make sure that there is a working internet connection and the OPSWAT Activation Server is reachable ([https://activation.dl.opswat.com](https://activation.dl.opswat.com))

{% code %}
```bash {% title="Test if Activation Server is network reachable" %}
wget -S --spider https://activation.dl.opswat.com 2>&1
```
{% /code %}

In case of expired license status ask for support on your [My OPSWAT](https://my.opswat.com/portal/products) portal.
