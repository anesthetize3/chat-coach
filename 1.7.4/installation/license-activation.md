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

### Online license activation

The product will connect directly to the OPSWAT licensing server online, and acquire its license based on your purchased Activation Key. License activation will happen automatically once a valid activation key is detected.

Steps to activate online:

- Create a file named `license.yml` in your fsTransform installation directory: `<installdir>/fsTransform/license/license.yml`
- Copy your activation key to the newly created license.yml file

{% code %}
```yaml {% title="Example license.yml containing a dummy activation key" %}
xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx
```
{% /code %}

### Offline license activation

In air-gapped environments the product can be activated with the help of another computer that has a working internet connection. The Deployment ID of the target computer and the Activation Key will be required to download an offline license file (.yml) via your [My OPSWAT](https://my.opswat.com/portal/products) portal. Follow the {% link href="https://my.opswat.com/portal/products(secondary:dialog-active)" %}displayed instructions{% /link %} for details.

#### Steps to activate offline

- Generate Deployment ID by executing the fsDeploymentID script, which can be found in the release package.
- Use your Activation Key and Deployment ID to download an offline license file from your {% link href="https://my.opswat.com/portal/products(secondary:dialog-active)" %}My OPSWAT{% /link %} portal.
- Copy your offline license file to the fsTransform installation directory:  `<installdir>/fsTransform/license/` folder.

{% code %}
```bash {% title="DeploymentId generation" %}
./fsDeploymentID

OPSWAT Filescan

Deployment ID:
	FSCANxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

'Copy the above deployment id to use it for Offline License Activation on https://my.opswat.com.'
```
{% /code %}

{% callout type="warning" title="Warning" %}
Please note that only one \*.yml file is allowed in the license directory.
{% /callout %}

## Deactivation

If a new license file is detected, the product will try to deactivate the existing deployment automatically, releasing the used deployment slot. Offline activated licenses cannot be automatically deactivated.

## Troubleshooting

If your license doesn't work it has probably expired or the system your Filescan instance is running on has changed. If the issue cannot be resolved ask for support on your [My OPSWAT](https://my.opswat.com/portal/products) portal.
