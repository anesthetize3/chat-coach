---
type: page
title: Release Notes for v2.3.0
listed: true
description: 
index_title: Release Notes for v2.3.0
hidden: true
keywords: 
tags: 
---

## Date: 23 May, 2025

**What's New**

- **OpenAI-powered Decompiler in Disassembly Sections:** Introduced an “Automatic RE” button within disassembly views. Security analysts can now generate AI-assisted decompiled code with inferred function names and contextual comments, presented in a two-tab layout (Disassembled/Decompiled) to accelerate reverse engineering workflows.

{% image url="https://uploads.developerhub.io/prod/XX2D/eah4j6drsjiwr0e0a7oi3xxvbutj6okf0s20jvukqnzgohogn8bg5z9tf5xqyhe8.png" %}
**Overview of Decompiled Function from npp.6.5.3 Installer**
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/xvce3r5145i51cck3pyy1vu01cqxxjluo3i1hg59k4jdmkul81esgjt068g6jbhf.png" %}
**Low-Level Code Instructions from npp.6.5.3 Installer**
{% /image %}

- **Classify Threat Indicators based on sandbox capabilities**: Improved classification and visibility of threat indicators derived from sandbox behavior. Enhancements include better translation, risk categorization, and filtering to support faster triage.
- **Report Deletion for Users:** End users can now delete their own analysis reports, while administrators maintain full privileges to remove any report across the system.
- **MS Entra Integration:** Users onboarded via Microsoft Entra (Azure AD) are now automatically mapped to the correct user groups, streamlining access control and user provisioning.
- **YARA Rules Enhancements:** Added a dedicated view for generated YARA rules, accessible via the Feed menu. Improved tagging, naming conventions, and metadata visibility for clearer rule management.

{% image url="https://uploads.developerhub.io/prod/XX2D/7qdhk1ou6eten8ici310ujdu2nzo9vd13dav3xrl6yl99mh9ghako40iskwsckpw.png" %}
**YARA Archive Page**
{% /image %}

- **HTML URL Parsing:** Integrated a new parser for analyzing URLs embedded within HTML content in emails and web threats, improving detection precision in phishing and redirection scenarios.
- **Phishing Detection Model Renamed: The** phishing detection model is now renamed to *brand detection*.
- **Support for Ubuntu 24.04:** MetaDefender Sandbox can also be installed on Ubuntu 24.04 LTS. Note that CIS Level 1/2 hardening is not yet available for Ubuntu 24.04; therefore, CIS compatibility will be added in a future release.

**Improvements**

- **UX Enhancements:** Fixed special character search issues, added configurable network modes, and improved threat indicator classification.
- **WebThreat Model Enhancement:** Detection accuracy has been improved by integrating three specialized models: structural, behavioral, and contextual. This enables deeper analysis of web threats.
- **Brand Detection Model Update:** The model now supports the *Marvell* brand. It has also been extended with OCR capabilities to improve the robustness of its decisions.
- **Offline URL Model Update:** The model has been retrained using a newly compiled set of URLs to enhance detection accuracy.
- **Performance Optimizations:** Improved threat detection performance by enhancing domain resolution speed, scan performance, and reducing memory usage.
- **String Extraction:** Improved string extraction logic, including better UTF-8 handling and efficiency.
- **API Enhancements:** Optimized API connection handling for better resource management and stability.

**Bug Fixes**

- **Report Loading:** Resolved internal server errors and username validation issues.
- **URL Handling:** Fixed issues with multi-redirected URLs, reputation lookups, and file type misdetection.
- **Zombie Process Fix:** Resolved an issue with the URL render process generating zombie processes, enhancing system stability.

## **Threat Detection Release Notes**

**What's New**

- **New Malware Family Detection:** Added config extractors for XWorm, Stealc, and new Lumma Stealer variants, boosting coverage of active campaigns. Also extended detection rules for emerging loaders and RAT such as PrivateLoader and Millenium RAT.
- **QR Code Pixel Repair:** Improved handling of QR codes with cropped bottom pixels, a tactic used by attackers to evade automatic scanners.
- **Short-Lived Certificate Whitelist Bypass Detection:** Prevents whitelisting of malware signed with short-lived certificates - a tactic used to bypass detection mechanisms.
- **API Hashing Detection:** Flags obfuscated API calls using hashing, being critical for catching stealthy malware.
- **Phishing DKIM Replay Abuse Detection:** Flags spoofed DKIM attempts, enhancing phishing resilience against recent campaigns that abuse Google Sites and DKIM replay to send valid-signed emails, bypassing filters and stealing credentials.
- **Enhanced PE Anomaly Detection:** Added 40+ signatures to detect PE structure anomalies, such as significant discrepancies between virtual size and raw size in PE headers.
- **APK Certificate Signer Validation:** Added validation and whitelisting of APK certificate signers to improve trust assessment and reduce false positives in mobile threat detection.

{% image url="https://uploads.developerhub.io/prod/XX2D/sb730wh8r2xrpnxuyul05f4on9q3vanz2ve16wirydiwpccyodphiyo2fij1qisn.png" %}
**Certificate details in Extended details tab**
{% /image %}

**Improvements**

- **Improved File Extraction From Base64 Artifacts:** Now supports extraction of embedded Base64-encoded files, including reverse cases seen in malware.

{% image url="https://uploads.developerhub.io/prod/XX2D/7b6ba6ilsw04fy6djl7lqa3scxek8i0jge8o7bhctgtsam4q7ysr7oyxqkfn1a9d.png" %}
**The threat indicator of base64 encoded embedded file extraction**
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/q3m2myil9b3d1f8q2ra0vxhkemg14of3r0jjic84ahjg2s33ug0uaeolkebt9d49.png" %}
**The extracted .NET dll file that triggers consumers**
{% /image %}

- **Script-Based Threat Detection Enhancements:** Improved detection of malicious JavaScript, VBA, and PowerShell behavior - including decoding, decryption, and suspicious cmdlet abuse. Emulated PowerShell code is now extracted as readable strings, enhancing visibility and analysis.
- **Disassembly Code Extraction Improvements:** Fixed issues with disassembly functions on RET instructions, implemented string annotation for immediate strings, and enhanced filtering to avoid disassembling junk code, improving the accuracy of extracted disassembly data.

{% image url="https://uploads.developerhub.io/prod/XX2D/etru9yp2dvr1wr24s5m7mjua7l2m5wc82h5xa38o9q5z1iloo5ai32ud773azxe5.png" %}
**String annotation for immediate strings**
{% /image %}

- **Adaptive Indicator Tuning for Signed PEs:** Fine-tuned context-aware indicators for signed PE files in offline environments, reducing false positives by improving detection accuracy when certificate validation is unavailable.
- **Improved Dropbox Download Handling:** Enhanced support for downloading and analyzing second-stage malware from Dropbox links in emails, addressing challenges with Dropbox's unique download mechanisms.

**Bug Fixes**

- **Certificate Validation Process Fix:** Resolved the issue where edge-case certificates, which are technically valid, were incorrectly detected as invalid.
