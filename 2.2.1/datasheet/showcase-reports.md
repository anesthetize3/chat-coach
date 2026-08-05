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

This section highlights our cybersecurity software's key capabilities, including sample analysis, malware family decoding, similarity unpacking, similarity search, and more. These features demonstrate our commitment to providing comprehensive tools for detecting and combating malware. Explore the reports below to delve into each capability in detail.

---

## #0 Synthetic (fabricated) sample

This sample stands as a purpose-built example to highlight the diverse capabilities of **MetaDefender Sandbox** (previously known as OPSWAT Filescan Sandbox). Crafted to show-off real-world cyber threats, embedding multiple files and file-types into each other. This effectively demonstrates our solution's prowess in adaptive threat analysis, behavioral analysis, and advanced security measures.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6551fb8d2546bd423f181cc3/reports/cc034b35-24c0-4b01-a75d-84a9c7639c59/overview](https://www.filescan.io/uploads/6551fb8d2546bd423f181cc3/reports/cc034b35-24c0-4b01-a75d-84a9c7639c59/overview)
{% /callout %}

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

It is important to note that this feature is particularly useful in air-gapped environments where online reputation lookups are not available.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6696cf5a3d7227f9379408e2/reports/30c313a7-40ac-46e8-a473-661f0e17dddd/osint](https://www.filescan.io/uploads/6696cf5a3d7227f9379408e2/reports/30c313a7-40ac-46e8-a473-661f0e17dddd/osint)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/yxr3s89ofvfgxoy6mf0g225889q79e903xwrltm7xt6po3glp3lbxlvmtvyuormg.png" /%}

[Learn more about the Suspicious URL Detection in Offline Mode by clicking here.](/metadefender-sandbox/2.1.0/datasheet/offline-url-detector)

---

## #4 Malware config extraction of a packed sample

The sample below reveals a malware that was packed using the UPX packing technique. Despite its attempt to evade detection and defenses, our analysis successfully unpacked the payload, exposing its true identity as a Dridex Trojan. We were able to uncover the malware configuration, shedding light on the malicious intent behind this threat, extracting valuable IOCs.

[Learn more about malware config extraction feature by clicking here.](executable-analysis/supported-malwares-for-config-extraction.md)

[Learn more about malware unpacking feature by clicking here.](executable-analysis/supported-packers-for-unpacking.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6710df185c4ea75bc80ab7e0/reports/9e0ef23b-fbc1-4a56-af25-01dc3d3671c3/overview](https://www.filescan.io/uploads/6710df185c4ea75bc80ab7e0/reports/9e0ef23b-fbc1-4a56-af25-01dc3d3671c3/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/s35t1rykvf5dg9ckvek1fd5fme0t6k82s46zwj0zku0yinojb88alorxxoopd9hq.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/pn1768x1doobvf0mrpfo7ddxhip2u1wjwahbcnt9lrdezkgod8zmvqdluumpm9z2.png" /%}

---

## #5 Similarity Search

Employing Similarity Search functionality, sandbox has detected a file remarkably resembling a known malware. Notably, this file had been previously marked as non-malicious, revealing the potential for false negatives in our security assessments. This discovery empowers us to specifically target and rectify these overlooked threats.

It is important to highlight that Similarity Search is highly valuable for threat research and hunting, as it can help uncover samples from the same malware family or campaign, providing additional IOCs or relevant information about specific threat activities.

[Learn more about this feature by clicking here.](advanced-reputation/similarity-search.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/64fab197d3406611cfae4c98/reports/2353dd56-c024-4fac-ab04-ad9487de5dcb/similarity\_search](https://www.filescan.io/uploads/64fab197d3406611cfae4c98/reports/2353dd56-c024-4fac-ab04-ad9487de5dcb/similarity_search)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/uoeotp8sesjxub7rvuue271zl8sovlaeigw60zzwz6y6bjw2gb9rgr69p7ir60u1.png" /%}

---

## #6 Finding interesting things via Disassembly

### #6.1 Native executable

Our disassembling engine revealed intriguing findings within the target sample. Surprisingly, this sample monitors the system time using the uncommon `rdtsc` instruction and accesses an internal, undocumented structure in Windows, commonly used for different malicious tricks. These unusual actions raise questions about its purpose and underscore the need for further investigation to assess potential risks to the system.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6437de44b4ec50bace5ff564/reports/a74af3b9-596f-4de8-8a82-f63e025e75d5/disassembly](https://www.filescan.io/uploads/6437de44b4ec50bace5ff564/reports/a74af3b9-596f-4de8-8a82-f63e025e75d5/disassembly)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/ytqk6mbd2ylu77pa1miu2kw51r4nrodsjoudhh3b1rqb08xfyfafqhttojfts88i.png" /%}

{% inline-image url="../../assets/dd0feb82aef8dce3b606aa581dd2ed7a7e18bac3.png" /%}

---

### #6.2 .NET Executable

The sample under examination was built using .NET framework. While we refrain from displaying the actual CIL, our decompilation process extracts and presents noteworthy information, including strings, registry artifacts, and API calls.

Besides that, we parse the .NET metadata to identify .NET-specific functions and resources. This process allows to extract detailed information about the assembly, such as methods, classes, and embedded resources, which is critical for analyzing the behavior and structure of .NET applications.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/671257087f0507a8d241e285/reports/c80b84e5-5431-4ebc-9c35-56cc7921ec71/overview](https://www.filescan.io/uploads/671257087f0507a8d241e285/reports/c80b84e5-5431-4ebc-9c35-56cc7921ec71/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/bb0j2jlox2smw1b579mmlf92wu0xhsq13llsz4s32futr1j6yx64jwrb1u2opz85.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/z7zje5iq50wtxquy5k47xq0pva7oam3km4wbu5cy14e2pmiadxz5ydju2bjglgii.png" /%}

---

## #7 Shellcode emulation

Many application exploits bring their final payload in raw binary format (shellcode), which might be an obstacle when parsing the payload. With our shellcode emulation we are able to discover and analyse the behaviour of the final payload, in this example for a widely leveraged Office vulnerability in the equation editor. Hence opening the door to gathering the relevant IOCs.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation\_data](https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/z4g00u4kuotyn4zymgrhk0f8nk99dtr24ef5pfuxhq4uze2z5cywnxisvmczodxw.png" /%}

---

## #8 Highly obfuscated VBA macro

Obfuscated VBA macros present a significant challenge to deliver a reasonable response time of active threats. This unclear code makes the analysis and understanding of threats a high complex task that demands a lot of time and efforts. Our cutting-edge VBA emulation technology is able to overcome these challenges and provides a comprehensive analysis of obfuscated VBA macro together with clear insights into its functionality in seconds.

The analyzed sample is an Excel document with highly obfuscated VBA code that drops and runs a .NET DLL file, together with a LNK file in charge of continuing the malware execution chain. After VBA emulation, MetaDefender Sandbox identifies launched processes and the main deobfuscating function, automatically extracts obfuscated strings and saves dropped files (previously hardcoded and encrypted in the VBA code). This rapidly show the main purpose of the malware and give us the possibility of a further analysis of this threat.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/6661fdc921581a92819b4d64/reports/e87e263e-27b5-45fc-bb99-733a553b3a36/overview](https://www.filescan.io/uploads/6661fdc921581a92819b4d64/reports/e87e263e-27b5-45fc-bb99-733a553b3a36/overview)
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

The following sample is an obfuscated VBScript that downloads the malicious payload and creates a scheduled task to run it 67 minutes later. Traditional sandboxes maintain the execution for only a few minutes and the malicious behavior would be never exposed. In the other hand, our VBScript emulator is able to detect and overcomes this evasion technique, adapting the execution environment to continue with further analysis, and getting the full report in 12 seconds.

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

---

## #11 XOR decrypting payload stored in PE resource

This feature enables to reveal hidden artifacts encrypted within PE resources. Malicious artifacts are often encrypted to evade detection and obscure the true intent of the sample. Uncovering these artifacts is essential, as they typically contain critical data (as C2 information) or payloads. By extracting them, the sandbox can deliver a deeper scan, with higher chance of identifying the most valuable IOCs.

Both storing encrypted data in a PE resource and using XOR encryption are techniques widely used by malware for these two basic reasons:

- Storing payloads in PE resources helps malware evade detection by static analysis tools. Many security tools focus on analyzing the executable’s main code section, while resources are often overlooked, making it easier to hide malicious content.
- XOR encryption shines for its simplicity and efficiency in evading detection, being time and resource efficient.

But XOR encryption has a weakness when applied to data with a large number of null bytes (such as PE files). This is because if a bit is XORed with 0, the original bit remains unchanged. By analyzing patterns in the encrypted data, especially in areas with many null bytes, the encryption key can be revealed, allowing to decrypt the hidden.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/66ab4c2e78d5c73fb1ca7f90/reports/eec0ead1-4ba2-4d6d-acf3-8ca73f9bec6f/overview](https://www.filescan.io/uploads/66ab4c2e78d5c73fb1ca7f90/reports/eec0ead1-4ba2-4d6d-acf3-8ca73f9bec6f/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/vfdjthjp8arb8mwl5r3onr5wg927w5f9xwhkfdq3xjo6w4disnp7ad710khba94a.png" %}
Hidden payload in PE resource
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/t8o2kycym1m784num3a0j8a32fgs7ckfdsrx5klbhlfai074jagmeh8vummi9frq.png" %}
Payload extracted after XOR decryption
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/zmze68i14xj7643n3a3wof15qzu43dfp67gk9djgq5snp4wts81w1ysd0zbrixf5.png" %}
C2 information identified from the payload
{% /image %}

---

## #12 Evasive Archive Concatenation

Attackers use archive concatenation to hide malware by appending multiple archives into a single file, exploiting how different tools process them. This technique creates multiple central directories - key structural elements used by archive managers - causing discrepancies during extraction and enabling the bypass of detection for malicious content hidden in overlooked parts of the archive.

MD Sandbox detects and extracts content from all concatenated archives, ensuring no file is missed and effectively neutralizing this evasive technique.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/678f361f17177fed56b4bc54](https://www.filescan.io/uploads/678f361f17177fed56b4bc54)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/13uhxug59kqbczslmcso09edgbz9h9q40f5iuf4nf3z087rg0sz7dpr42xy9tt4h.png" /%}

---

## #13 Mitigating bloated executables

Threat actors bloat intentionally executables with junk data to evade detection by exploiting resource limitations and analysis time constraints in sandboxes. This evasion technique looks to overwhelm tools or bypass scans by exceeding time limits.

MD sandbox detects bloated executables early, removes junk data, and processes a smaller file for efficient analysis. This debloating process targets various methods, including junk in overlays, PE sections, and certificates, ensuring accurate detection while conserving original resources.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/67a5dcb5a55c685dbbf28985/reports/7be3e68b-7436-44c1-9eb5-fb041c800b2c/overview](https://www.filescan.io/uploads/67a5dcb5a55c685dbbf28985/reports/7be3e68b-7436-44c1-9eb5-fb041c800b2c/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/9rqnwog3cz69iqld045riyrxfj60k0797v6831o4ke2xhxvie2p79wsk9o6yz4qz.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/nxptydwxds7vt3g8fbcpeisydz0oacvi2665wro9cy7f9mjw999e72f3yxvwpagj.png" /%}

---

## #14 Document targeting critical infrastructures

This Office document targets critical infrastructure in Iran (with content in Persian) to steal sensitive information, such as credentials and documents, and periodically takes screenshots, potentially for espionage purposes.

After establishing persistence, it performs a stealthy initial internet connectivity check (against a trusted domain like google.com) to ensure a reliable connection, delaying further actions until network conditions allow the attack to proceed. This is a tactic commonly observed in attacks on critical infrastructure, environments where internet access may be intermittent or restricted.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/679664ec0a04287e8b028aff/reports/894ab8c8-f6e4-4030-8414-ea2715ad64f9/emulation\_data](https://www.filescan.io/uploads/679664ec0a04287e8b028aff/reports/894ab8c8-f6e4-4030-8414-ea2715ad64f9/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/0511k54ws3y6n6jn86kjtasdkw31vkge7i3pr0mraykzrodqan279d75ua5qmams.png" /%}

---

## #15 Evasion through corrupted OOXML (office) documents

Researchers discovered intentionally corrupted OOXML documents (modern office documents). By modifying the binary content near the internal file headers, the purposely broken files may be misdetected as ZIP files by automatic scans which will attempt to extract compressed files.

Document viewers will automatically repair the document upon opening. At this point, despite the document containing phishing content, it may have effectively bypassed defenses. Automated analysis will not be able to read its content and therefore miss the relevant indicators.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/676172737e0ef1ddadddf145/reports/10075c64-30f4-4215-9eef-e41078dcb205/overview](https://www.filescan.io/uploads/676172737e0ef1ddadddf145/reports/10075c64-30f4-4215-9eef-e41078dcb205/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/msxmkjrf26y1z905pc7rrup1chue8hh2lwaig0nz4a01xb7md4oco16tb3nq3w63.png" /%}
