---
type: page
title: What URL analysis capabilities are in the sandbox?
listed: true
description: 
index_title: What URL analysis capabilities are in the sandbox?
hidden: true
keywords: 
tags: 
---

**MetaDefender Sandbox** (previously known as OPSWAT Filescan Sandbox) offers a variety of features around URL analysis. Here are the highlights:

- Full webpage rendering (Chrome), including capture of all GET/POST requests, Certificates and a Screenshot
- All potential IOCs captured during the webpage rendering phase are added to the main report and cross-checked against our real-time MD Cloud Reputation (includes 50B+ hashes, URLs, IPs, domains) service
- Machine Learning (ML) based image analysis for phishing detection
- Currently detects 339+ major brands
- Additional integrations with Google Safebrowsing

**Do you have an example API request/response?**

1. Submit a file using the `/api/scan/url` endpoint (Reference: [https://www.filescan.io/api/docs#/scan/scan\_file\_api\_scan\_url\_post](https://www.filescan.io/api/docs#/scan/scan_file_api_scan_url_post)) and obtain a flow\_id
2. Using that flow\_id, query the results using `/api/scan/<flow_id>/report` and apply at minimum the `ur%3ArenderResults` filter.

Example:

`https://www.filescan.io/api/scan/6437bf9d1f50fdcf669a0b60/report?filter=overallState&filter=finalVerdict&filter=allTags&filter=allSignalGroups&filter=ur%3ArenderResults`

The final verdict of the URL analysis can be obtained via the `finalVerdict` field, if the `overallState` field is set to SUCCESS (requires additional filters, see Example).

**Do you have documentation on the API fields returned?**

For all render related fields, please refer to the Chrome DevTools Protocol documentation, specifically Network Domain and related classes: [https://chromedevtools.github.io/devtools-protocol/tot/Network/](https://chromedevtools.github.io/devtools-protocol/tot/Network/)

Phishing detection related fields are present beneath the

{% code %}
```json
"phishDetection": {
   "brand": "Office365",
   "category": 1,
}
```
{% /code %}

Where the `category` field may be 0 (benign) or 1 (phishing detected). The `base64` field contains the rendered image.

{% image url="../../../assets/63cd10988594b87c951c35cc65a52a986c8c1ed0.png" /%}

{% image url="../../../assets/2ad882dc1c3b26db0aaac6a3863dd5bdbc7cf7f2.png" /%}
