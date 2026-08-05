---
type: page
title: Targeted Attacks
listed: true
description: 
index_title: Targeted Attacks
hidden: false
keywords: 
tags: 
---

## #1 APT spear-phishing targeting government sectors in the Middle East

**Target Profile:** {% badge text="diplomatic" type="warning" /%} {% badge text="maritime" type="warning" /%} {% badge text="military" type="warning" /%} {% badge text="governement" type="warning" /%}{% badge text="middle east" type="warning" /%}

**Threat Actor:** {% badge text="APT34" type="error" /%} {% badge text="Oilrig" type="error" /%} {% badge text="Karkoff" type="error" /%}

**Detection Spotlight:** {% badge text="emulation" /%}{% badge text="file extraction" /%}

The origin of the files is reportedly part of a spearphishing email, either attached to the email or downloaded from a link included in the email. After some research, we discovered that the sample was first spotted in 2021 and associated with APT34. The original filename is “جهوزية الزوارق والمراكب.doc”, which translates to English as “Boat and vessel readiness.doc”. The lure content of the document aligns with its title, using Lebanese Navy information that was reportedly potentially stolen during a previously reported compromise. The document prompts to enable macros. If enabled, it creates a directory pretending to be related to Google in order to remain unnoticed, where it drops 3 files. It also creates a scheduled task to execute one of three files: a small VBA script which uses Powershell to load the other two files through .NET Assembly reflection.  These two other files that are detected and extracted in the analysis are .NET DLLs, samples of the Karkoff malware family.

Aether researchers were able to hunt this sample by searching for themed documents filtering by specific languages, allowing them to spot interesting samples such as this, implemented to target government sectors in the Middle East.

{% callout title="URL to the sample" %}
[h](https://www.filescan.io/uploads/696fa5805db9ae47708a66dd)[ttps://www.filescan.io/uploads/6913e57a935d9f0d73ceb189/reports/a34defcd-dc41-491f-ab33-6954acc86efe/overview](https://www.filescan.io/uploads/6913e57a935d9f0d73ceb189/reports/a34defcd-dc41-491f-ab33-6954acc86efe/overview)
{% /callout %}

{% image url="../../assets/faf726b0007f81524bde0105c1290ad6147d030e.jpg" /%}

{% image url="../../assets/1b53a314858c8ab13ac974296af838ff3c5bfaf0.jpg" /%}

{% image url="../../assets/8c9a68e24e2b51f66b8e8285779814d20f07e3ce.jpg" /%}

{% image url="../../assets/6e662c15d6da5331fbb2be3c5569a4d260444328.jpg" /%}

---

## #2 APT spear-phishing campaign using in-house protected macros

**Target Profile:** {% badge text="pakistan" type="warning" /%} {% badge text="south asia" type="warning" /%} {% badge text="manufacturing" type="warning" /%}

**Threat: {% badge text="APT-C-35" type="error" /%}** {% badge text="donot" type="error" /%}

**Detection Spotlight:** {% badge text="emulation" /%}

This campaign is attributed to a South Asia–focused APT conducting highly targeted intrusions against organizations with business, industrial, or government relevance. The actor relies on spear-phishing emails for initial access, showing clear signs of victim profiling rather than mass distribution.

Malware is delivered via a malicious Office document, with the correct macro password included in the email body. The macro uses an in-house password check, meaning the malicious logic will not execute unless the correct password is entered, a mechanism that is especially effective at preventing automated analysis systems. It also includes a meaningless loop to waste analysis resources, dynamically generates shellcode, and executes it by abusing the callback mechanism of the Windows *CryptEnumOIDInfo* API, helping the payload evade detection.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/6970eca85db9ae47708bfcdb/reports/39bb8f35-499e-4353-a0f1-0e8ec4504956/overview](https://www.filescan.io/uploads/6970eca85db9ae47708bfcdb/reports/39bb8f35-499e-4353-a0f1-0e8ec4504956/overview)
{% /callout %}

{% image url="../../assets/3cfe9a28290fca92c52f2ab1c9eb2dfecc314978.png" /%}

{% image url="../../assets/b4ff0a02dd0d38946a9df5b690c5eca476841273.png" /%}

{% image url="../../assets/6e3b5cab3ae312be3e92cbca12d37535c7c39c91.png" /%}

---

## #3 Stealthy connectivity check before data exfiltration

**Target Profile:** {% badge text="iran" type="warning" /%} {% badge text="cyberespionage" type="warning" /%}

**Threat Actor: {% badge text="stealer" type="error" /%}**

**Detection Spotlight:** {% badge text="deep static" /%} {% badge text="emulation" /%}

This Office document targets critical infrastructure in Iran (with content in Persian) to steal sensitive information, such as credentials and documents, and periodically takes screenshots, potentially for espionage purposes.

After establishing persistence, it performs a stealthy initial internet connectivity check (against a trusted domain like google.com) to ensure a reliable connection, delaying further actions until network conditions allow the attack to proceed. This is a tactic commonly observed in attacks on critical infrastructure, environments where internet access may be intermittent or restricted.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/679664ec0a04287e8b028aff/reports/894ab8c8-f6e4-4030-8414-ea2715ad64f9/emulation\_data](https://www.filescan.io/uploads/679664ec0a04287e8b028aff/reports/894ab8c8-f6e4-4030-8414-ea2715ad64f9/emulation_data)
{% /callout %}

{% image url="../../assets/8ec84990ead77ef985bf3afb18d00f73719ee194.png" /%}

---

---

## #4 MuddyWater “Cybersecurity Guidelines” maldoc

**Target Profile:** {% badge text="middle east" type="warning" /%} {% badge text="diplomatic" type="warning" /%} {% badge text="maritime" type="warning" /%} {% badge text="financial" type="warning" /%} {% badge text="telecom" type="warning" /%}

**Threat: {% badge text="MuddyWater" type="error" /%}**

**Detection Spotlight:** {% badge text="emulation" /%}

A spearphishing email titled “Cybersecurity Guidelines”, sent from a legitimate account tied to a regional mobile operator, delivers a malicious Word document. Once the victim enables macros, the VBA code extracts a hex-encoded payload embedded inside the document (stored in a UserForm control), cleans it up, decodes it back into a Windows executable, writes it to disk, and launches it immediately. The launch step is handled through an obfuscated wrapper that rebuilds key strings at runtime to make the macro logic harder to follow.

That dropped executable is a Rust-based implant (“RustyWater”) that adds multiple defensive layers. It sets up anti-debug/anti-tamper behavior (e.g., registering a Vectored Exception Handler), keeps operational strings encrypted (position-independent XOR), and performs basic security-product discovery by checking for AV/EDR artifacts (agent files, service names, install paths) across 25+ tools. It also establishes persistence via a Run-key autostart entry, and uses HTTP-based C2 with layered obfuscation (JSON → Base64 → XOR) plus randomized callback timing (jitter). The execution can be further masked via injection into a legitimate Windows process.

Researchers found evidence of additional activity targeting the UAE, including decoy documents and impersonation-themed lures, suggesting a broader regional targeting set.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/6961a589d1d688e1d664a396/reports/84de06f5-5229-457c-9a07-af2c81ec7f8e/overview](https://www.filescan.io/uploads/6961a589d1d688e1d664a396/reports/84de06f5-5229-457c-9a07-af2c81ec7f8e/overview)
{% /callout %}

{% image url="../../assets/8c9b840befbb979dc4bad8697f479178c433998e.png" /%}

---

## 

## #5 Threat actor delivers targeted multistage polyglot malware

**Target Profile:** {% badge text="aviation" type="warning" /%} {% badge text="telecom" type="warning" /%} {% badge text="transportation" type="warning" /%}

**Threat: {% badge text="UNK_CraftyCamel" type="error" /%}**

**Detection Spotlight: {% badge text="deep static" /%}** {% badge text="emulation" /%}

This campaign is a highly targeted espionage operation against a very small number of organizations in the UAE, mainly in the aviation, satellite, and transportation sectors. The emails are carefully crafted and sent from a compromised legitimate Indian company, which helps build trust. While there is no confirmed APT attribution, the targeting and techniques overlap with Iran-aligned threat activity, suggesting a likely state-linked actor.

The attack is notable for its extensive use of polyglot files, which are valid in multiple formats at once. Victims receive a ZIP containing a fake Excel file that is actually a LNK shortcut, along with PDF/HTA and PDF/ZIP polyglots. These files abuse trusted Windows tools like mshta.exe to run hidden code, evade detection, and load the final payload disguised as an image.

{% callout title="URL to the sample" %}
[https://www.filescan.io/uploads/696fa5805db9ae47708a66dd](https://www.filescan.io/uploads/696fa5805db9ae47708a66dd)
{% /callout %}

{% image url="../../assets/70da27e92b2ec86fd398581a5979649c442c7ff2.png" /%}
