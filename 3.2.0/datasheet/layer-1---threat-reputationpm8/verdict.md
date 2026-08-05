---
type: page
title: Report Verdict
listed: true
description: 
index_title: Report Verdict
hidden: false
keywords: 
tags: 
---

The table provided below offers a high-level overview of submission classifications based on their potential threat levels and a summarized overview within your report verdicts.

{% callout title="Info" %}
From MetaDefender Sandbox 2.5.0,  the displayed verdicts will use the new, **human-friendly** variants from the table below. The old, **risk score based** verdicts can still be enabled through the Admin Panel, see the Configuration options under [General Settings](../../configuration/general-settings/general.md).
{% /callout %}

The final verdict is an aggregate of the detected threat indicators based on our proprietary verdict calculation logic, which is tuned to mitigate the occurrence of both false negative and false positive results, ensuring a more accurate and reliable assessment of potential threats.

The `threatLevel` field contains a numeric representation that corresponds to a given verdict. For some verdicts, the `threatLevel` is a range, not a single value. See the exact values below.

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[91] %}
**Human Friendly Verdict (New)**
{% /cell %}
{% cell header=true colwidth=[102] %}
**Risk Score Based Verdict (Old)**
{% /cell %}
{% cell header=true colwidth=[299] %}
**Description**
{% /cell %}
{% cell header=true colwidth=[135] %}
**Action**
{% /cell %}
{% cell header=true %}
Threat Level Values
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[91] %}
Trusted
{% /cell %}
{% cell colwidth=[102] %}
Benign
{% /cell %}
{% cell colwidth=[299] %}
The file has been whitelisted based on a hash match with the National Software Reference Library (NSRL), custom whitelists, or valid certificates from reputable software vendors.
{% /cell %}
{% cell colwidth=[135] %}
No Action
{% /cell %}
{% cell %}
\-1
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[91] %}
Undetermined
{% /cell %}
{% cell colwidth=[102] %}
Unknown
{% /cell %}
{% cell colwidth=[299] %}
The file is unsupported, contains insufficient data, or the analysis is inconclusive.
{% /cell %}
{% cell colwidth=[135] %}
Malware Analysis
{% /cell %}
{% cell %}
0
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[91] %}
No Threat Detected
{% /cell %}
{% cell colwidth=[102] %}
No Threat
{% /cell %}
{% cell colwidth=[299] %}
Although the file is supported, its reputation data and threat indicators do not indicate any known capability typically associated with malware.
{% /cell %}
{% cell colwidth=[135] %}
No Action
{% /cell %}
{% cell %}
0\.1-0.25
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[91] %}
Low Risk
{% /cell %}
{% cell colwidth=[102] %}
Suspicious
{% /cell %}
{% cell colwidth=[299] %}
The file contains some threat indicators commonly found in malware. To address this, please ensure that the [MD Cloud Reputation](https://docs.opswat.com/filescan/integrations/reputation-api-integration) service is enabled and perform an AV engine scan with [MetaDefender Multiscanning.](https://docs.opswat.com/filescan/integrations/metadefender-multiscanning)
{% /cell %}
{% cell colwidth=[135] %}
Perform AV engine/reputation check
{% /cell %}
{% cell %}
0\.5
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[91] %}
High Risk
{% /cell %}
{% cell colwidth=[102] %}
Likely Malicious
{% /cell %}
{% cell colwidth=[299] %}
The file exhibits numerous threat indicators commonly associated with malware, and there is no compelling evidence from the AV engine or reputation services to suggest otherwise.

**Note**: Behaviors often associated with malware—such as code injection, process manipulation, or network communication—can also occur in legitimate applications, making definitive conclusions challenging. In air-gapped environments, where certificate-based whitelisting and external reputation lookups are unavailable, legitimate application presenting such capabilities may be classified as "High Risk". See how [Adaptive Threat Context](https://www.opswat.com/docs/filescan/3.1.1/datasheet/adaptive-threat-context) helps to mitigate these false positives.
{% /cell %}
{% cell colwidth=[135] %}
Block file
{% /cell %}
{% cell %}
0\.75
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[91] %}
Confirmed Threat
{% /cell %}
{% cell colwidth=[102] %}
Malicious
{% /cell %}
{% cell colwidth=[299] %}
The file provides clear evidence of being malware, either due to a critical mass of threat indicators, a true positive indicator, or validation from a first-tier AV engine or reputable source.
{% /cell %}
{% cell colwidth=[135] %}
Block File
{% /cell %}
{% cell %}
1
{% /cell %}
{% /row %}
{% row %}
{% cell colwidth=[91] %}
System Error
{% /cell %}
{% cell colwidth=[102] %}
N/A
{% /cell %}
{% cell colwidth=[299] %}
The verdict could not be determined due to an internal malfunction (e.g., engine crash).
{% /cell %}
{% cell colwidth=[135] %}
Retry or Report Issue
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% /table %}

### **Verdict Visualization**

{% image url="../../../assets/5c4bf461b24b424d3b006150a253713e16d1a559.png" width=560 /%}

### Verdict Representation in the API Scan Results

If the **human-friendly** verdicts are enabled, then the API returns scan results in the following format: the `finalVerdict`  object contains the `verdict`  field that matches **risk score based** verdicts from the table above, and the `verdictLabel`  field matches the **human-friendly** verdicts.

{% callout title="Info" %}
For all API integrations, please use the `threatLevel`  field contains a stable numeric representation that corresponds to a given verdict. The text representation of a verdict might change in future versions, but the `threatLevel`  will have the same value.
{% /callout %}

{% code %}
```json
"finalVerdict": {
    "verdict": "SUSPICIOUS",
    "threatLevel": 0.5,
    "confidence": 1.0,
    "verdictLabel": "low_risk"
}
```
{% /code %}
