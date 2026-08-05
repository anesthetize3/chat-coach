---
type: page
title: Hidden Artifact Extraction
listed: true
description: 
index_title: Hidden Artifact Extraction
hidden: true
keywords: 
tags: 
---

This feature allows the sandbox to reveal hidden artifacts embedded within PE files. Malicious artifacts are often **encoded and/or encrypted** to evade detection and obscure the sample's true intent. Uncovering these artifacts is essential, as they typically contain critical data, such as C2 information or payloads. By extracting them, the sandbox can perform a deeper scan, increasing the likelihood of identifying valuable IOCs.

## PE Resource XOR Decryption

Storing payloads in PE resources helps malware evade detection by static analysis tools. Many security tools focus on analyzing the executable’s main code section, while resources are often overlooked, making it easier to hide malicious content.

Why XOR encryption? It is widely used for its simplicity and efficiency in evading detection, but one key property of XOR is that when a bit is XORed with 0, the original bit remains unchanged. This characteristic makes XOR encryption particularly "weak" when applied to data with a large number of null bytes, such as those often found in PE files. By analyzing patterns in the encrypted data, especially in areas with many null bytes, the encryption key can be revealed, allowing to decrypt the hidden.

{% callout type="success" title="Encrypted Payload Extraction" %}
This sample is a malware loader that contains a encrypted payload in a resource.

On the following link you can find the sample from the screenshot below:

[https://www.filescan.io/uploads/66ab4c2e78d5c73fb1ca7f90/reports/eec0ead1-4ba2-4d6d-acf3-8ca73f9bec6f](https://www.filescan.io/uploads/66ab4c2e78d5c73fb1ca7f90/reports/eec0ead1-4ba2-4d6d-acf3-8ca73f9bec6f)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/3frusvomhkqajngmpxmubckxo9sg0rroofre7pzoilc76d13bk4hw5ecw6uvn8y1.png" %}
Hidden payload in PE resource
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/iu191f4oyug73odtadhnz7ff46shi996arcon9qmsfxobipm61pfk2jl03elpsop.png" %}
Payload extracted after XOR decryption
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/oqovp1ghrc1fg59pb0zsl0wk5u5h7d14ydnwk8e4d1g6a5x91br1dx4zc8so8w1g.png" %}
C2 information identified from the payload
{% /image %}

## Base64-encoded embedded files

Malicious actors embed base64-encoded content, such as executables, archives, or documents within seemingly benign text-based or document files, using them as decoys to evade detection. A more advanced observed evasion technique involves reversing base64-encoded content to bypass detection mechanisms.

MetaDefender Sandbox identifies these potentially malicious embedded files, extracts them, and analyzes their true functionality.

{% callout type="success" title="Encoded Payload Extraction" %}
The following sample shows a malicious .NET DLL embedded as a base64-encoded string within an image file

[https://www.filescan.io/uploads/682b0a0ac609634bd7c8e2eb/reports/25a80656-17eb-40a3-beb7-4f80797cf1a3/overview](https://www.filescan.io/uploads/682b0a0ac609634bd7c8e2eb/reports/25a80656-17eb-40a3-beb7-4f80797cf1a3/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/36cl338oqv5nhjs46w8zfjca2dqopqrzzowh5y09yd8gr2kms79dxmb0m2bd361g.png" %}
Detected embedded base64-encoded files
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/epk1hgm2w735ghw0nf7ukm53yp74k0sv8bzbpc66nk8s9eln7fej4otf22ue1zco.png" %}
The extracted .NET dll file that triggers threat indicators
{% /image %}
