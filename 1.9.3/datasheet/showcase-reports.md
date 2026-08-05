---
type: page
title: Showcase Reports
listed: true
description: 
index_title: Showcase Reports
hidden: false
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

{% image url="https://uploads.developerhub.io/prod/XX2D/xyco8td7x29kmywpkxl5f67o54enzx11irg3oh5d02pg5l1yfx14i7uyztb7uagy.png" /%}

---

## #2 Phishing detection

By rendering suspicious websites and subjecting them to our advanced machine learning engine we're capable of identifying near 300 brands. In the example provided below, you can witness a Russian website masquerading as a computer gaming company known as Steam. Our solution excels in comparing the site's content to the genuine URL, swiftly identifying such fraudulent attempts to safeguard your digital assets and personal information.

[Learn more about this feature by clicking here.](../faq/brand-detection.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6437bf9d1f50fdcf669a0b60/reports/5a011dcb-dbcb-43e7-96a1-0199a1a86552/url\_details](https://www.filescan.io/uploads/6437bf9d1f50fdcf669a0b60/reports/5a011dcb-dbcb-43e7-96a1-0199a1a86552/url_details)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/t12y6hbfdrx89n54svxyjyn5w1l10tfliqa16k7i7pyx6fg4jtt5ojz883fxgws7.png" /%}

---

## #3 Malware config extraction of a packed sample

The sample below reveals a malware that was crypted using the UPX packing technique. Despite its attempt to obfuscate, our analysis successfully unpacked the payload, exposing its true identity as a Dridex Trojan. We were able to uncover the correct configuration, shedding light on the malicious intent behind this threat.

[Learn more about malware config extraction feature by clicking here.](executable-analysis/supported-malwares-for-config-extraction.md)

[Learn more about malware unpacking feature by clicking here.](executable-analysis/supported-packers-for-unpacking.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6509a2792d5fc006cad6d73c/reports/e1a4fc93-7224-417e-9ecf-817f977ce78d/overview](https://www.filescan.io/uploads/6509a2792d5fc006cad6d73c/reports/e1a4fc93-7224-417e-9ecf-817f977ce78d/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/cko3tbvbrey592fjdpu8my9jn2an9cvezsytyy56ucyssm8ppb8lhnr24ui2o3sh.png" width=300 /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/jf7so4567gplg3wjw5a5dcg1mn52uri1pwrhx50ru32k18lctlgnd4p8ao2dxxwb.png" /%}

---

## #4 Similarity Search

Employing Similarity Search functionality, has detected a file remarkably resembling a known malware. Notably, this file had been previously marked as non-malicious, revealing the potential for false negatives in our security assessments. This discovery empowers us to specifically target and rectify these overlooked threats.

[Learn more about this feature by clicking here.](../operationalguide/threat-intelligence/similarity-search.md)

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/64fab197d3406611cfae4c98/reports/2353dd56-c024-4fac-ab04-ad9487de5dcb/threat\_intelligence](https://www.filescan.io/uploads/64fab197d3406611cfae4c98/reports/2353dd56-c024-4fac-ab04-ad9487de5dcb/threat_intelligence)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/5ng1fxk14qo0n2hze46ar86ehp1sipd5ggzit8qmozcxznyhl6v8ndcr1vj6ztk4.png" /%}

---

## #5 Finding interesting things via Disassembly

### #5.1 Native executable

Our disassembling engine revealed intriguing findings within the target sample. Surprisingly, this sample monitors the system time using the uncommon `rdtsc` instruction and accesses an internal, undocumented structure in Windows. These unusual actions raise questions about its purpose and underscore the need for further investigation to assess potential risks to the system.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6437de44b4ec50bace5ff564/reports/a74af3b9-596f-4de8-8a82-f63e025e75d5/overview](https://www.filescan.io/uploads/6437de44b4ec50bace5ff564/reports/a74af3b9-596f-4de8-8a82-f63e025e75d5/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/ree6xr7o5vk2xad9r4i3zcen478vvz926x2rz48sr246sflkulmc48ctbme6wzld." /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/vcwdbxbymeldmsk81xrhv0fcx4ubgxema5uuddkkghpvn2ecm81lum8rr9767pzx.png" /%}

---

### #5.2 .NET Executable

The sample under examination was built using .NET framework. While we refrain from displaying the actual CIL, but our decompilation process extracts and presents noteworthy information, including strings, registry artifacts, and API calls. This comprehensive approach allows us to uncover potential indicators of compromise, facilitating a deeper understanding of the sample.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/64f8f5af2a262962b795a841/reports/f9ce513c-f9a1-4787-80ff-42003c0d3347/strings](https://www.filescan.io/uploads/64f8f5af2a262962b795a841/reports/f9ce513c-f9a1-4787-80ff-42003c0d3347/strings)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/quojuamq1ymq9cbmiy2xzw0y8qv97qz1w6vr9x4vir2tk5yb7j99jc1dxu3z6sj0." /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/s3qok7v2bisk146dsiw91hxhyqp46xjrp2q4sg3tcfh49s1trsmvfwxl8t3sfean.png" /%}

---

## #6 Shellcode emulation

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation\_data](https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/33dn71w3jkori9ahgfzr0rncbxyhhwpfnb2rt713rex4091qpqfxfxmu64u6sj6g.png" /%}

---

## #7 Highly obfuscated VBA macro

Obfuscated VBA macros present a significant challenge to deliver a reasonable response time of active threats. This unclear code makes the analysis and understanding of threats a high complex task that demands a lot of time and efforts. Our cutting-edge VBA emulation technology is able to overcome these challenges and provides a comprehensive analysis of obfuscated VBA macro together with clear insights into its functionality in seconds.

The analyzed sample is an Excel document with highly obfuscated VBA code that drops and runs a .NET DLL file, together with a LNK file in charge of continue the malware execution chain. After VBA emulation, MetaDefender Sandbox identifies launched processes and the main deobfuscating function, automatically extracts obfuscated strings and saves dropped files (previously hardcoded and encrypted in the VBA code). This rapidly show the main purpose of the malware and give us the possibility of a further analysis of this threat.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/6661fdc921581a92819b4d64/reports/e87e263e-27b5-45fc-bb99-733a553b3a36/overview](https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/rw8sjkss483eyr2iqc1h3y7mhvz2i9k29h48gssmati3e03zzdsnj0ayavlac2t1.png" %}
Threat indicators triggered based on emulation data
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/2ygi5b75aluvy79i859kekv3rnc2exnvb3x75l5k0dop2xsn1ojv13hq6qfu1t2p.png" %}
Obfuscated VBA code
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/po4b7u0grmsod4kvc65sblx60vusr4lq5au0x3672jg6bpneiywrim2ztor2k9hh.png" %}
Extracted strings after deobfuscating and emulating the VBA macro code
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/ar4cmv51f24t9p3k7c3et5qnmejn9u2iuhhknrwl426j7e4xs2invjrmgsfhrdi3.png" %}
Next stager PE file created by VBA emulation
{% /image %}

---

## #8 Sandbox evasion via Task Scheduler

Using Windows Task Scheduler to execute malicious payloads at a later time is a stealthy technique to evade sandbox environments seen in recent threats. It exploits the delay in execution to effectively bypass the short analysis window typical of sandboxes.

The following sample is an obfuscated VBScript that downloads the malicious payload and creates a scheduled task to run it 67 minutes later. Traditional sandboxes maintains the execution for only a few minutes and the malicious behavior would be never exposed. In the other hand, our VBScript emulator is able to detect and overcomes this evasion technique (T1497), adapting the execution environment to continue with further analysis, and getting the full report in 12 seconds.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/66682a7d21581a92819c335a/reports/64374035-17a1-4c48-b810-f4fdf6f3f0d8/overview](https://www.filescan.io/uploads/650a09b733582f234efc873c/reports/f48778d5-8cde-4309-ad93-639e7a055e14/emulation_data)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/fl2tkv9f97s7w632ikw01q3qoyy9l1um3s6af0ukqlov9b1pyjs9fn4ytn9fwgf8.png" %}
Schedule task created to gain persistence and evade sandbox analysis (execution delayed 67 mins)
{% /image %}

---

## #9 .NET Reflection

.NET Reflection is a powerful feature provided by the .NET framework that allows programs to inspect and manipulate a .NET file structure and behavior at runtime. It enables the examination of assemblies, modules, and types, as well as the ability to dynamically create instances of types, invoke methods, and access fields and properties.

Malware can use reflection to dynamically load and execute code from assemblies that are not referenced at compile time, allowing to fetch additional payloads from remote servers (or hidden in the current file) and execute them without writing them to disk, reducing the risk of detection.

In this case, we can see how the analysed VBScript loads and runs a .NET assembly into memory directly from bytes stored in a Windows register.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/666b0289ef9fdf64aa6adb06/reports/ce3451fe-3dd6-40f2-bf06-44136f2fe43c](https://www.filescan.io/uploads/666b0289ef9fdf64aa6adb06/reports/ce3451fe-3dd6-40f2-bf06-44136f2fe43c)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/zb3bzlkv0vorko3nbvaqtkil0q6bead397b5hmxo0d40q22qmxopulm5tntuzm3v.png" width=600 %}
VBScript saving a reversed and base64-encoded PE in a register and then running a .NET-based RAT using .NET reflection
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/xpv0owe77cobm0nm34bk4k7d1axqycp0jtadfv8c6hqxbybnrn8m197t05r84vj6.png" %}
Emulation actions showing the payload execution using .NET reflection
{% /image %}
