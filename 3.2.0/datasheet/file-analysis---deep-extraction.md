---
type: page
title: File Analysis & Deep Extraction
listed: true
description: 
index_title: File Analysis & Deep Extraction
hidden: false
keywords: 
tags: 
---

## #1 Synthetic (fabricated) sample

**Detection Spotlight:** {% badge text="deep static" /%}{% badge text="unpacking" /%}{% badge text="emulation" /%}{% badge text="malware config" /%}

This sample stands as a purpose-built example to highlight the diverse capabilities of **MetaDefender Sandbox** (previously known as OPSWAT Filescan Sandbox). Crafted to show-off real-world cyber threats, embedding multiple files and file-types into each other. This effectively demonstrates our solution's prowess in adaptive threat analysis, behavioral analysis, and advanced security measures.

Check out all the following great features of the previous link:

- Many detailed indicators, highlighting these:
  - Significant evidence of malicious (phishing) file
  - Malware config
  - Many PE related ones
  - Call for action indicators
  - Contains an URL encoded in a QR code
    - We do decode QR codes even if they're embedded. Check this out both as an indicator, as strings and as the picture itself rendered
- File details shown in additional files, make sure you are not only checking the input, but all the details of:
  - Extracted files (different file types with many details shown!)
  - Downloaded files
- Emulation data - note that we're able to dig down multiple levels into the emulation. Check some of the interesting blocks, such as:
  - AccessLocale
  - StartProcess
  - CreateObject
- Identified sets of IOCs, including the URL from the QR code as well
- Thorough string extraction with the filtering ability

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6551fb8d2546bd423f181cc3/reports/cc034b35-24c0-4b01-a75d-84a9c7639c59/overview](https://www.filescan.io/uploads/6551fb8d2546bd423f181cc3/reports/cc034b35-24c0-4b01-a75d-84a9c7639c59/overview)
{% /callout %}

---

## #2 Threat Pattern Correlator

**Detection Spotlight:** {% badge text="simsearch" /%}{% badge text="AI detection" /%}

Employing Threat Pattern Correlator functionality, sandbox has detected a file remarkably resembling a known malware. Notably, this file had been previously marked as non-malicious, revealing the potential for false negatives in our security assessments. This discovery empowers us to specifically target and rectify these overlooked threats.

It is important to highlight that Threat Pattern Correlato is highly valuable for threat research and hunting, as it can help uncover samples from the same malware family or campaign, providing additional IOCs or relevant information about specific threat activities.

[Learn more about this feature by clicking here.](layer-1---threat-reputationpm8npn/advanced-reputation/threat-pattern-correlator.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/682b67e1c609634bd7c989af/reports/53383651-1d20-490a-82fb-c5f476599f71/similarity\_search](https://www.filescan.io/uploads/682b67e1c609634bd7c989af/reports/53383651-1d20-490a-82fb-c5f476599f71/similarity_search)
{% /callout %}

{% image url="../../assets/8748572c939b876ca940869bb563491200653bc7.png" /%}

---

## #3 Finding interesting things via Disassembly

### #3.1 Native executable

**Detection Spotlight:** {% badge text="deep static" /%}

Our disassembling engine revealed intriguing findings within the target sample. Surprisingly, this sample monitors the system time using the uncommon `rdtsc` instruction and accesses an internal, undocumented structure in Windows, commonly used for different malicious tricks. These unusual actions raise questions about its purpose and underscore the need for further investigation to assess potential risks to the system.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6437de44b4ec50bace5ff564/reports/a74af3b9-596f-4de8-8a82-f63e025e75d5/disassembly](https://www.filescan.io/uploads/6437de44b4ec50bace5ff564/reports/a74af3b9-596f-4de8-8a82-f63e025e75d5/disassembly)
{% /callout %}

{% image url="../../assets/86aaf710d971315785c0a57cd2ce6042d7e7cace.png" /%}

{% image url="../../assets/0a8910993de12a3efa747ce1a0cff65ce8d7c8c3.png" /%}

### #3.2 .NET Executable

**Detection Spotlight:** {% badge text="deep static" /%}

The sample under examination was built using .NET framework. While we refrain from displaying the actual CIL, our decompilation process extracts and presents noteworthy information, including strings, registry artifacts, and API calls.

Besides that, we parse the .NET metadata to identify .NET-specific functions and resources. This process allows to extract detailed information about the assembly, such as methods, classes, and embedded resources, which is critical for analyzing the behavior and structure of .NET applications.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/671257087f0507a8d241e285/reports/c80b84e5-5431-4ebc-9c35-56cc7921ec71/overview](https://www.filescan.io/uploads/671257087f0507a8d241e285/reports/c80b84e5-5431-4ebc-9c35-56cc7921ec71/overview)
{% /callout %}

{% image url="../../assets/38cc703cfd6792c9b1b744372c5b17b52cfff8ba.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/z7zje5iq50wtxquy5k47xq0pva7oam3km4wbu5cy14e2pmiadxz5ydju2bjglgii.png" /%}

---

## #4 Malware config extraction of a packed sample

**Detection Spotlight:** {% badge text="unpacking" /%}{% badge text="malware config" /%}

The sample below reveals a malware that was packed using the UPX packing technique. Despite its attempt to evade detection and defenses, our analysis successfully unpacked the payload, exposing its true identity as a Dridex Trojan. We were able to uncover the malware configuration, shedding light on the malicious intent behind this threat, extracting valuable IOCs.

[Learn more about malware config extraction feature by clicking here.](layer-1---threat-reputationpm86o8/executable-analysis/supported-malwares-for-config-extraction.md)

[Learn more about malware unpacking feature by clicking here.](layer-1---threat-reputationpm86o8/executable-analysis/supported-packers-for-unpacking.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6710df185c4ea75bc80ab7e0/reports/9e0ef23b-fbc1-4a56-af25-01dc3d3671c3/overview](https://www.filescan.io/uploads/6710df185c4ea75bc80ab7e0/reports/9e0ef23b-fbc1-4a56-af25-01dc3d3671c3/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/s35t1rykvf5dg9ckvek1fd5fme0t6k82s46zwj0zku0yinojb88alorxxoopd9hq.png" /%}

{% image url="../../assets/21184f3c64e499efdcdb1b57f1c71ac4f1341276.png" /%}

---

## #5 XOR decrypting payload stored in PE resource

**Detection Spotlight:** {% badge text="deep static" /%}{% badge text="unpacking" /%}

This feature enables to reveal hidden artifacts encrypted within PE resources. Malicious artifacts are often encrypted to evade detection and obscure the true intent of the sample. Uncovering these artifacts is essential, as they typically contain critical data (as C2 information) or payloads. By extracting them, the sandbox can deliver a deeper scan, with higher chance of identifying the most valuable IOCs.

Both storing encrypted data in a PE resource and using XOR encryption are techniques widely used by malware for these two basic reasons:

- Storing payloads in PE resources helps malware evade detection by static analysis tools. Many security tools focus on analyzing the executable’s main code section, while resources are often overlooked, making it easier to hide malicious content.
- XOR encryption shines for its simplicity and efficiency in evading detection, being time and resource efficient.

But XOR encryption has a weakness when applied to data with a large number of null bytes (such as PE files). This is because if a bit is XORed with 0, the original bit remains unchanged. By analyzing patterns in the encrypted data, especially in areas with many null bytes, the encryption key can be revealed, allowing to decrypt the hidden.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/66ab4c2e78d5c73fb1ca7f90/reports/eec0ead1-4ba2-4d6d-acf3-8ca73f9bec6f/overview](https://www.filescan.io/uploads/66ab4c2e78d5c73fb1ca7f90/reports/eec0ead1-4ba2-4d6d-acf3-8ca73f9bec6f/overview)
{% /callout %}

{% image url="../../assets/7ce6d249f60308a6a79f51ec9999b5aa1e11aef1.jpeg" /%}

{% image url="../../assets/83b1bafbb61436188dfdd9dbd7f055e5364e0594.jpeg" /%}

{% image url="../../assets/44d18e3a8878ba614c51e57eee610c619d7ec8ff.jpeg" /%}

---

## #6 Stealthy .NET Loader with Bitmap Payload

**Detection Spotlight:** {% badge text="deep static" /%}{% badge text="unpacking" /%}{% badge text="malware config" /%}

RoboSki is the most commonly observed .NET loader in recent years. This loader hides a multi-stage payload chain behind legitimate code and image resources. It decrypts a bitmap image to load a fileless .NET DLL, protected with ConfuserEx, which finally drops the final payload.

This threat uses obfuscation, runtime decryption, and fileless techniques to evade static detection. Threat insights are protected, making crucial actionable intelligence not accessible by simple detonating the sample — and manual unpacking is time-consuming and error-prone.

Why removing protection layers matters? Mitigating protection layers (like ConfuserEx control-flow obfuscation and string encryption) is crucial because it restores readable logic, making code actionable for detection and analysis.

Sandbox Highlights

- Unpacks .NET loaders automatically — including protected stages.
- Removes control-flow obfuscation to expose real logic and increase unpacking successful rate.
- Extracts hidden payloads and configs (C2s, persistence, stealing hooks) in one pass.

{% image url="../../assets/a43c61bd0793ef65b6f215d4d6cb78505fefe320.png" %}
Attack Timeline VS Sandbox Analysis
{% /image %}

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/686faccc80b46be06e9dbbdf/reports/21f43b71-56bf-4494-a2d2-9b76ff75d17c](https://www.filescan.io/uploads/686faccc80b46be06e9dbbdf/reports/21f43b71-56bf-4494-a2d2-9b76ff75d17c)
{% /callout %}

{% image url="../../assets/26169e62692ad61b1584976bdcc26ed20a238cf4.png" /%}
