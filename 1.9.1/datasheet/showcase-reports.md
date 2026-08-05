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
