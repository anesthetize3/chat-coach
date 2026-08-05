---
type: page
title: Showcase Reports
listed: true
description: 
index_title: Showcase Reports
hidden: true
keywords: 
tags: 
---

In this section, we will highlight our cybersecurity software's key capabilities, including sample analysis, malware family decoding, disassembly unpacking, similarity search, and more. These features represent our commitment to providing comprehensive tools for detecting and combating malware effectively. Explore the reports below to delve into each capability in detail.

---

## #0 Synthetic (fabricated) sample

This sample stands as a purpose-built example to highlight the diverse capabilities of **MetaDefender Sandbox** (previously known as OPSWAT Filescan Sandbox). Crafted to show-off real-world cyber threats, embedding multiple files and file-types into each other. This effectively demonstrates our solution's prowess in adaptive threat analysis, behavioural analysis, and advanced security measures.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6551fb8d2546bd423f181cc3/reports/cc034b35-24c0-4b01-a75d-84a9c7639c59/overview](https://www.filescan.io/uploads/6551fb8d2546bd423f181cc3/reports/cc034b35-24c0-4b01-a75d-84a9c7639c59/overview)
{% /callout %}

Check out all the following great features of the previous link:

- All the various indicators, highlighting these:
  - Significant evidence of malicious (phishing) file
  - Malware config
  - Many PE related ones
  - Call for action indicators
  - Contains an URL encoded in a QR code
    - We do decode QR codes even if they're embedded. Check this out both as an indicator, as strings and as the picture itself rendered
- All the File details we show, make sure you're not only checking the input, but all the details of:
  - Extracted files (various filetypes with varying details shown!)
  - Downloaded files
- Emulation data - note that we're able to dig down multiple levels into the emulation. Check some of the interesting blocks, such as:
  - AccessLocale
  - StartProcess
  - CreateObject
- All the IOCs, including the URL from the QR code as well
- All the extracted strings with the filtering ability

## #1 Geofencing

Malware documents employing geofencing have become a significant threat to cybersecurity. These malicious files often employ location-based triggers, making detection and mitigation a challenging task. However, Adaptive Threat Analysis stands out from traditional approaches by offering the capability to accurately emulate and falsify the expected geolocation values, effectively neutralizing the tactics employed by malware, thus enhancing our ability to protect against such threats.

In the sample provided below, we can observe a geofencing malware attempting to execute exclusively within a specific country. However, our innovative solution successfully bypasses this restriction, as previously mentioned, by emulating the desired geolocation values, demonstrating our superior capability in countering such geofencing-based threats.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/643d529246e0911fda9eb28c/reports/65c685b3-a9ca-466d-9655-b6ab2ba0bf1a/emulation\_data](https://www.filescan.io/uploads/643d529246e0911fda9eb28c/reports/65c685b3-a9ca-466d-9655-b6ab2ba0bf1a/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/ey58xsppaomvc1txyqo3td8njymd0x83qoqdvpaemfyddouwuyys0knwaocjsnke.png" /%}

---

## #2 Phishing detection

By rendering suspicious websites and subjecting them to our advanced machine learning engine we're capable of identifying nearly 300 brands. In the example provided below, you can witness a Russian website masquerading as a computer gaming company known as Steam. Our solution excels in comparing the site's content to the genuine URL, swiftly identifying such fraudulent attempts to safeguard your digital assets and personal information.

[Learn more about this feature by clicking here.](../faq/brand-detection.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6437bf9d1f50fdcf669a0b60/reports/5a011dcb-dbcb-43e7-96a1-0199a1a86552/url\_details](https://www.filescan.io/uploads/6437bf9d1f50fdcf669a0b60/reports/5a011dcb-dbcb-43e7-96a1-0199a1a86552/url_details)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/t29hhpfmzlzylai7cismbqr3inzkrfgch0oo6k7ckrjmkazkv7jaietsevmwg9dg.png" /%}

---

## #3 Offline URL Reputation

The offline URL detector ML model provides a new layer of defense by effectively detecting suspicious URLs, offering a robust means to identify and mitigate threats posed by malicious links.  It leverages a dataset containing hundreds of thousands of URLs, meticulously labeled as either no threat or malicious by reputable vendors, to assess the feasibility of accurately detecting suspicious URLs through machine learning techniques.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6696cf5a3d7227f9379408e2/reports/30c313a7-40ac-46e8-a473-661f0e17dddd/osint](https://www.filescan.io/uploads/6696cf5a3d7227f9379408e2/reports/30c313a7-40ac-46e8-a473-661f0e17dddd/osint)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/gkvksc29zxsc2llyeubkv9ymfy2j00qditzw1grirwuhs0d86ps8jgaxkb6ct3pi.png" /%}

Learn more about the Suspicious URL Detection in Offline Mode by clicking here.

---

## #4 Malware config extraction of a packed sample

The sample below reveals a malware that was crypted using the UPX packing technique. Despite its attempt to obfuscate, our analysis successfully unpacked the payload, exposing its true identity as a Dridex Trojan. We were able to uncover the correct configuration, shedding light on the malicious intent behind this threat.

[Learn more about malware config extraction feature by clicking here.](executable-analysis/supported-malwares-for-config-extraction.md)

[Learn more about malware unpacking feature by clicking here.](executable-analysis/supported-packers-for-unpacking.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6509a2792d5fc006cad6d73c/reports/e1a4fc93-7224-417e-9ecf-817f977ce78d/overview](https://www.filescan.io/uploads/6509a2792d5fc006cad6d73c/reports/e1a4fc93-7224-417e-9ecf-817f977ce78d/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/s35t1rykvf5dg9ckvek1fd5fme0t6k82s46zwj0zku0yinojb88alorxxoopd9hq.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/fek6vn8snywbtou20q10peeycjmfmg8x0kgf36pb4sih570e39r85amrhpdm3p2n.png" /%}

---

## #5 Similarity Search

Employing Similarity Search functionality, has detected a file remarkably resembling a known malware. Notably, this file had been previously marked as non-malicious, revealing the potential for false negatives in our security assessments. This discovery empowers us to specifically target and rectify these overlooked threats.

[Learn more about this feature by clicking here.](../operationalguide/threat-intelligence/similarity-search.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/64fab197d3406611cfae4c98/reports/2353dd56-c024-4fac-ab04-ad9487de5dcb/threat\_intelligence](https://www.filescan.io/uploads/64fab197d3406611cfae4c98/reports/2353dd56-c024-4fac-ab04-ad9487de5dcb/threat_intelligence)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/3u8aldlct63r5wfnhqas7gj21ekpirnlqmgu6q0ebohyvql5rgcgh9zbcmq1zneo.png" /%}

---

## #6 Finding interesting things via Disassembly

### #6.1 Native executable

Our disassembling engine revealed intriguing findings within the target sample. Surprisingly, this sample monitors the system time using the uncommon `rdtsc` instruction and accesses an internal, undocumented structure in Windows. These unusual actions raise questions about its purpose and underscore the need for further investigation to assess potential risks to the system.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6437de44b4ec50bace5ff564/reports/a74af3b9-596f-4de8-8a82-f63e025e75d5/overview](https://www.filescan.io/uploads/6437de44b4ec50bace5ff564/reports/a74af3b9-596f-4de8-8a82-f63e025e75d5/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/ytqk6mbd2ylu77pa1miu2kw51r4nrodsjoudhh3b1rqb08xfyfafqhttojfts88i.png" /%}

{% inline-image url="asset:hpx0o3ar03ds" /%}

---

### #6.2 .NET Executable

The sample under examination was built using .NET framework. While we refrain from displaying the actual CIL, but our decompilation process extracts and presents noteworthy information, including strings, registry artifacts, and API calls. This comprehensive approach allows us to uncover potential indicators of compromise, facilitating a deeper understanding of the sample.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/64f8f5af2a262962b795a841/reports/f9ce513c-f9a1-4787-80ff-42003c0d3347/strings](https://www.filescan.io/uploads/64f8f5af2a262962b795a841/reports/f9ce513c-f9a1-4787-80ff-42003c0d3347/strings)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/g35lapajb99nm5d5i80s511oqtc2nnt9oqeen12dtxj2oir7etef6o3wffv4car1.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/5583ckdt58cgw15kgqmjrk342lozk4hk56ihi7qtmd2xwcbbq2m1o5pswgb3squm.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/evvbfpxosjy7j5gvfi87a8x5dlp2bkh38829nqvt5gt12u86dssrgzwbvnbbwt8g.png" /%}

---

## #7 Shellcode emulation

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation\_data](https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/z4g00u4kuotyn4zymgrhk0f8nk99dtr24ef5pfuxhq4uze2z5cywnxisvmczodxw.png" /%}

---

## #8 Highly obfuscated VBA macro

Obfuscated VBA macros present a significant challenge to deliver a reasonable response time of active threats. This unclear code makes the analysis and understanding of threats a high complex task that demands a lot of time and efforts. Our cutting-edge VBA emulation technology is able to overcome these challenges and provides a comprehensive analysis of obfuscated VBA macro together with clear insights into its functionality in seconds.

The analyzed sample is an Excel document with highly obfuscated VBA code that drops and runs a .NET DLL file, together with a LNK file in charge of continue the malware execution chain. After VBA emulation, MetaDefender Sandbox identifies launched processes and the main deobfuscating function, automatically extracts obfuscated strings and saves dropped files (previously hardcoded and encrypted in the VBA code). This rapidly show the main purpose of the malware and give us the possibility of a further analysis of this threat.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/6661fdc921581a92819b4d64/reports/e87e263e-27b5-45fc-bb99-733a553b3a36/overview](https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/ufa2l881vv7425a3zm9fr57cnje968siylzkw1fiij1dqo7717i11c33uf3r90u2.png" %}
Emulation calls the same function excessively
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/daa0eutr20g5yqopem5jfzw8lkgqqixk5yqpl8j9vycfplrn64apg0dnteuqlxmp.png" %}
Obfuscated VBA macro code
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/otpeewl41ykqcy4jhd7yjtyv49j8egon18nqdqvhzx8xb82cbfyrm9130k7iipe6.png" %}
Extracted strings after deobfuscating and emulating the VBA macro code
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/aimvhzihcsa6wxwywo9a94mdrwtekn7uq52wgxts12onvj3cty4gld7te6sauyyw.png" %}
Next stager PE file created by VBA emulation
{% /image %}

---

## #9 Sandbox evasion via Task Scheduler

Using Windows Task Scheduler to execute malicious payloads at a later time is a stealthy technique to evade sandbox environments seen in recent threats. It exploits the delay in execution to effectively bypass the short analysis window typical of sandboxes.

The following sample is an obfuscated VBScript that downloads the malicious payload and creates a scheduled task to run it 67 minutes later. Traditional sandboxes maintains the execution for only a few minutes and the malicious behavior would be never exposed. In the other hand, our VBScript emulator is able to detect and overcomes this evasion technique (T1497), adapting the execution environment to continue with further analysis, and getting the full report in 12 seconds.

{% callout title="URL to the sample" %}
[Filescan.IO - Analysis Report for b161c8e32c0f33a182b5b2479521d3b826ce739ac0b3f3de9042e17d53873e57 - Emulation\_data](https://www.filescan.io/uploads/66682a7d21581a92819c335a/reports/64374035-17a1-4c48-b810-f4fdf6f3f0d8/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/fbleb6duf09cwnqtjjltrtfsgq85lw3jfxjxuz8v15cnn1btgj9ct8uj4gt0ie7r.png" %}
Schedule task created to gain persistence and evade sandbox analysis (execution delayed 67 mins)
{% /image %}

---

## #10 .NET Reflection

NET Reflection is a powerful feature provided by the .NET framework that allows programs to inspect and manipulate a .NET file structure and behavior at runtime. It enables the examination of assemblies, modules, and types, as well as the ability to dynamically create instances of types, invoke methods, and access fields and properties.

Malware can use reflection to dynamically load and execute code from assemblies that are not referenced at compile time, allowing to fetch additional payloads from remote servers (or hidden in the current file) and execute them without writing them to disk, reducing the risk of detection.

In this case, we can see how the analysed VBScript loads and runs a .NET assembly into memory directly from bytes stored in a Windows register.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/666b0289ef9fdf64aa6adb06/reports/ce3451fe-3dd6-40f2-bf06-44136f2fe43c](https://www.filescan.io/uploads/666b0289ef9fdf64aa6adb06/reports/ce3451fe-3dd6-40f2-bf06-44136f2fe43c)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/lheyppk5u2v3ny2mqk2o3zfk3romg6ytglk5ctv9xea7dj99vux29amipk0nwsbv.png" %}
VBScript saving a reversed and base64-encoded PE in a register and then running a .NET-based RAT using .NET reflection
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/zhz1n32s9vtlbgmiajpmzcndyayt3ahkezelywbqadil1qws37i476d8haecqdjt.png" %}
Emulation actions showing the payload execution using .NET reflection
{% /image %}
