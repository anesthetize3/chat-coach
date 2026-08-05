---
type: page
title: Local Whitelist
listed: true
description: 
index_title: Local Whitelist
hidden: false
keywords: 
tags: 
---

The local whitelists are stored in the `/home/sandbox/sandbox/transform/external` folder, specifically:

- `whitelist_certificate_owners.txt`
- `whitelist_hashes.txt`
- `whitelist_iocs.txt`
- `whitelist_generated_hashes.txt`

These file can contain certificate owners, domains, URLs or MD5 hashes which are used to reduce noise from false positive IOC detections.

You can also add your own custom whitelist files (one entry per line) in the `/home/sandbox/sandbox/transform/external` folder.

In this case, you need to **add the name of your custom file** to the following properties in `/home/sandbox/sandbox/transform.cfg` :

- **whitelistCertificateOwnersFiles**
- **whitelistHashesFiles**
- **whitelistIOCsFiles**

{% callout type="warning" title="Warning" %}
It is important to set any custom option values in the **transform.cfg properties file**!

It is also important to **NOT edit the existing whitelist files**!

The upgrade process will "reset" any configuration changes if you edit the default files and properties.
{% /callout %}

After changing these properties, it is necessary to restart the `sandbox` service:

{% code %}
```bash
sudo service sandbox restart
```
{% /code %}

## Example: Adding a whitelisted domain or URL

Create a new file (e.g. `custom_whitelist_iocs.txt`) in the `external` folder, then add the domains and URLs that you wish to whitelist line-by-line. For example:

```
my-company.com
https://www.some-other-company.com/globalnav/_all/reimagined.js
```

Add this property in `transform.cfg` :

```
whitelistIOCsFiles=whitelist_iocs.txt,custom_whitelist_iocs.txt
```

Save the file and remember to restart the `sandbox` service!

## Example: Adding a whitelisted hash

Create a new file (e.g. `custom_whitelist_hashes.txt`) in the `external` folder, then add hash values (in MD5 format) that you wish to whitelist line-by-line. For example:

```
0000368a1659bd1d3a0b826556a19a66
```

Add this property in `transform.cfg` :

```
whitelistHashesFiles=whitelist_hashes.txt,whitelist_generated_hashes.txt,custom_whitelist_hashes.txt
```

Save the file and remember to restart the `sandbox` service!

## Example: Adding a whitelisted certificate owner

Create a new file (e.g. `custom_whitelist_certificate_owners.txt`) in the `external` folder, then add the certificate owners that you wish to whitelist line-by-line. To obtain the certificate owner for a digitally signed file, you may scan the file using Sandbox, then copy the relevant certificate owner from File Details -\> Extended Details -\> Certificates.

For example, this is the correct format for the Microsoft Corporation certificate owner:

```
CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, ST=Washington, C=US
```

Add this property in `transform.cfg` :

```
whitelistCertificateOwnersFiles=whitelist_certificate_owners.txt,custom_whitelist_certificate_owners.txt
```

Save the file and remember to restart the `sandbox` service!
