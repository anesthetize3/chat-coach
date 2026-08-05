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

{% image url="../../../assets/7ce6d249f60308a6a79f51ec9999b5aa1e11aef1.jpeg" /%}

{% image url="../../../assets/83b1bafbb61436188dfdd9dbd7f055e5364e0594.jpeg" /%}

{% image url="../../../assets/44d18e3a8878ba614c51e57eee610c619d7ec8ff.jpeg" /%}

## Base64-encoded embedded files

Malicious actors embed base64-encoded content, such as executables, archives, or documents within seemingly benign text-based or document files, using them as decoys to evade detection. A more advanced observed evasion technique involves reversing base64-encoded content to bypass detection mechanisms.

MetaDefender Sandbox identifies these potentially malicious embedded files, extracts them, and analyzes their true functionality.

{% callout type="success" title="Encoded Payload Extraction" %}
The following sample shows a malicious .NET DLL embedded as a base64-encoded string within an image file

[https://www.filescan.io/uploads/682b0a0ac609634bd7c8e2eb/reports/25a80656-17eb-40a3-beb7-4f80797cf1a3/overview](https://www.filescan.io/uploads/682b0a0ac609634bd7c8e2eb/reports/25a80656-17eb-40a3-beb7-4f80797cf1a3/overview)
{% /callout %}

{% image url="../../../assets/7604a6c0f1d0fb954b88108802d0e4574231567d.jpeg" /%}

{% image url="../../../assets/3d7efa0aea4b3482623668d07ff86888b54659bd.jpeg" /%}
