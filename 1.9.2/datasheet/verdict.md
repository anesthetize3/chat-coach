---
type: page
title: Report Verdict
listed: true
description: 
index_title: Report Verdict
hidden: true
keywords: 
tags: 
---

The table provided below offers a high-level overview of submission classifications based on their potential threat levels and a summarized overview within your report verdicts.

The final verdict is an aggregate of the detected threat indicators based on our proprietary verdict calculation logic, which is tuned to mitigate the occurrence of both false negative and false positive results, ensuring a more accurate and reliable assessment of potential threats.

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[205] %}
**Verdict**
{% /cell %}
{% cell header=true colwidth=[517] %}
**Description**
{% /cell %}
{% cell header=true %}
**Action**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Benign
{% /cell %}
{% cell %}
The file has been whitelisted based on a hash match with the National Software Reference Library (NSRL), custom whitelists, or valid certificates from reputable software vendors.
{% /cell %}
{% cell %}
No Action
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Unknown
{% /cell %}
{% cell %}
The file is not supported due to insufficient data or an emulator/analysis engine crash.
{% /cell %}
{% cell %}
Malware Analysis
{% /cell %}
{% /row %}
{% row %}
{% cell %}
No Threat
{% /cell %}
{% cell %}
Although the file is supported, its reputation data and threat indicators do not indicate any known capability typically associated with malware.
{% /cell %}
{% cell %}
No Action
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Suspicious
{% /cell %}
{% cell %}
The file contains some threat indicators commonly found in malware. To address this, please ensure that the [MD Cloud Reputation](https://docs.opswat.com/filescan/integrations/reputation-api-integration) service is enabled and perform an AV engine scan with [MetaDefender Multiscanning.](https://docs.opswat.com/filescan/integrations/metadefender-multiscanning)
{% /cell %}
{% cell %}
Perform AV engine/reputation check
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Likely Malicious
{% /cell %}
{% cell %}
The file exhibits numerous threat indicators commonly associated with malware, and there is no compelling evidence from the AV engine or reputation services to suggest otherwise.
{% /cell %}
{% cell %}
Block file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Malicious
{% /cell %}
{% cell %}
The file provides clear evidence of being malware, either due to a critical mass of threat indicators, a true positive indicator, or validation from a first-tier AV engine or reputable source.
{% /cell %}
{% cell %}
Block File
{% /cell %}
{% /row %}
{% /table %}

**Verdict Visualization**

{% image url="https://uploads.developerhub.io/prod/XX2D/9mhbgrwoqd8cajlviavrsimgpb8mw957z29819s194252jvix3jydp28ksfn22xn.png" /%}
