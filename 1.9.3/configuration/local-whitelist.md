---
type: page
title: Local Whitelist
listed: true
description: 
index_title: Local Whitelist
hidden: true
keywords: 
tags: 
---

The local whitelists are stored in the `/home/filescanio/FileScanIO/fsTransform/external` folder, specifically:

- `whitelist_certificate_owners.txt`
- `whitelist_hashes.txt`
- `whitelist_iocs.txt`
- `whitelist_generated_hashes.txt`

These file can contain certificate owners, domains, URLs or MD5, SHA-1, SHA-256, SHA-512 hashes which are used to reduce noise from false positive IOC detections.

You can also add your own custom whitelist files (one entry per line) in the `/home/filescanio/FileScanIO/fsTransform/external` folder.

In this case, you need to **add the name of your custom file** to the following properties in `/home/filescanio/FileScanIO/fsTransform/conf/transform.properties.custom` :

- **whitelistCertificateOwnersFiles**
- **whitelistHashesFiles**
- **whitelistIOCsFiles**
- **whitelistDomains** (comma-separated list of domains)

{% callout type="warning" title="Warning" %}
It is important to set any custom option values in the **.custom properties file**!

It is also important to **NOT edit the existing whitelist files**!

The upgrade process will "reset" any configuration changes if you edit the default files and properties.
{% /callout %}

After changing these properties, it is necessary to restart the `fsio` service:

{% code %}
```bash
sudo service fsio restart
```
{% /code %}

## Example: Adding a whitelisted domain

{% callout type="warning" title="Warning" %}
In version 1.9.3, it is NOT possible to whitelist a full URL, but domains can be whitelisted by modifying both the **whitelistIOCsFiles** and the **whitelistDomains** properties!
{% /callout %}

Create a new file (e.g. `custom_whitelist_iocs.txt`) in the `external` folder, then add the domains that you wish to whitelist line-by-line. For example:

```
my-company.com
```

Add this property in `transform.properties.custom` :

```
whitelistIOCsFiles=whitelist_iocs.txt,custom_whitelist_iocs.txt
```

The same domain (e.g. `my-company.com` ) should be also added to the `whitelistDomains`  property. Please extend the comma-separated list of domains like this:

```
whitelistDomains=android.com,android.intent,xmlsoap.org,w3.org,openxmlformats.org,schemas.microsoft.com,go.microsoft.com,crl.microsoft.com,windows.com,windowsupdate.com,thawte.com,symcb.com,symauth.com,verisign.com,symantec.com,digicert.com,purl.org,ns.adobe.com,maxmind.com,schema.org,my-company.com
```

Save the files and remember to restart the `fsio` service!

## Example: Adding a whitelisted hash

Create a new file (e.g. `custom_whitelist_hashes.txt`) in the `external` folder, then add hash values (in MD5, SHA-1, SHA-256, or SHA-512 format) that you wish to whitelist line-by-line. For example:

```
0000368a1659bd1d3a0b826556a19a66
299643e208275caaace28abb7a43e2c56d59c376
5ef73237437496789f63f58b72661195836a0c60d5e81cb019a88d3ee426e82d
```

Add this property in `transform.properties.custom` :

```
whitelistHashesFiles=whitelist_hashes.txt,whitelist_generated_hashes.txt,custom_whitelist_hashes.txt
```

Save the file and remember to restart the `fsio` service!

## Example: Adding a whitelisted certificate owner

Create a new file (e.g. `custom_whitelist_certificate_owners.txt`) in the `external` folder, then add the certificate owners that you wish to whitelist line-by-line. To obtain the certificate owner for a digitally signed file, you may scan the file using Sandbox, then copy the relevant certificate owner from File Details -\> Extended Details -\> Certificates.

For example, this is the correct format for the Microsoft Corporation certificate owner:

```
CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, ST=Washington, C=US
```

Add this property in `transform.properties.custom` :

```
whitelistCertificateOwnersFiles=whitelist_certificate_owners.txt,custom_whitelist_certificate_owners.txt
```

Save the file and remember to restart the `fsio` service!
