---
type: page
title: Android Application Package (APK) Analysis
listed: true
description: 
index_title: Android Application Package (APK) Analysis
hidden: true
keywords: 
tags: 
---

Android applications are a frequent vector for malware delivery, posing significant risks to both users and organizations. MetaDefender Sandbox can play a crucial role in detecting malicious behavior within APK files through in-depth static analysis.

Our sandbox offers advanced APK analysis capabilities, providing deep insights into Android malware:

- **APK file parsing**: Extracts essential metadata and structural information, such as requested permissions, signing certificates, and registered receivers and services.
- **Code disassembly and resource decoding**: Powered by Apktool, enabling reverse engineering of APKs.
- **Smali code analysis**: Leverages a proprietary smali parser to identify risky method calls by analyzing the assembly-like code.
- **Extensive threat detection**: 100+ threat indicators to enable detection of unknown mobile malware.
- **MITRE Mobile Matrix**: Extended coverage of the MITRE Mobile Matrix. Check it out [here](/metadefender-sandbox/2.2.0/datasheet/mitre-attack-coverage).

## Showcase Report: Detecting Cerberus and its malicious capabilities

{% callout title="Cerberus" %}
Android banking Trojan that steals sensitive and confidential banking data.
{% /callout %}

Here we can see how Cerberus can intercept communications (using high priority intents), including one-time passwords and transaction verification codes from banking apps, allowing attackers to bypass two-factor authentication. Check out the full report [here](https://www.filescan.io/uploads/679a56fba2886cdc5ac63ebb/reports/0611de87-6957-43e6-b644-d3fddc24cdd3)!

{% image url="https://uploads.developerhub.io/prod/XX2D/adyo35i7my5yxsb5dr61sv1wuttx51d907aoob4v8di5dtzt4yddo4l4g310xmyl.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/kcmnfnynoeh3rmsdjtl7w43vqpu8ehdpjxlynzuyll9qxqwzwj3pap4uiqlfzf52.png" /%}
