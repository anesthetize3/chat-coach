---
type: page
title: Release Notes for v2.1.0
listed: true
description: 
index_title: Release Notes for v2.1.0
hidden: true
keywords: 
tags: 
---

## Date: 3 October, 2024

**What's New**

- **Ransomware Detection Enhancement**: Added severity Yara rule matches related to ransomware, helping to prioritize and respond to ransomware threats more effectively.

{% image url="https://uploads.developerhub.io/prod/XX2D/6f8qhtcih5a1rjvgesl5wdjpptucw2ui89w8hizj4rsd748kxrm41vqtefaueyhh.png" %}
***0.75 severity score for the ransomware***
{% /image %}

- **LNK File Threat Indicators**: Strengthened detection for LNK icon smuggling and LNK-MOTW (Mark of the Web) bypass attacks, both common techniques in modern malware.
- **OT Malware Detection**: Introduced a YARA ruleset specifically for OT (Operational Technology) malware, expanding protection to critical infrastructure systems.
- **Improved Resource Section Analysis**: Enhanced extraction and detection of overlays in the PE resource section, providing deeper insights into hidden malicious content.

{% image url="https://uploads.developerhub.io/prod/XX2D/9qi07z5u7gfrq5nzel9injueozarow1b0b0ofhrzvt1d9r9gb10czhml6zu2qghp.png" /%}

- **Downloadable Data**: You can now download extracted resource section data from PE files for offline analysis and further investigation.
- **.NET API Call Detection**: Added detection of unmanaged .NET API references, improving analysis of .NET-based malware.

{% image url="https://uploads.developerhub.io/prod/XX2D/gl3fzdkiwqvisu61uoqr4ksvmmk86rwmpnflho0tokep33f6osh0dcrxvztb5394.png" %}
***Before .NET API Call Detection implementation***
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/swbu55sffkct408r5qp2rnaw132yrphmjczvcxt3300mhdufp9spf4cz67l0xjb0.png" %}
***After .NET API Call Detection implementation***
{% /image %}

- **JPHP Support**: Enhanced malware detection with the ability to parse and decompile JPHP files, expanding the range of supported file types and languages. [Supported packers for unpacking](../../datasheet/executable-analysis/supported-packers-for-unpacking.md)
- **MSC File Support**: Added the ability to identify and parse Microsoft Management Console (MSC) files, further broadening threat detection capabilities.
- **Symantec Quarantine Repair**: Implemented a repair function for files restored from Symantec quarantine, ensuring files can be analysed post-restoration.
- **Custom Time zone \& Locale**: Users can now configure their preferred time zone and locale settings for a more personalized experience. [How do I set my time zone and locale?](../../faq/timezone-preferences.md)

{% image url="https://uploads.developerhub.io/prod/XX2D/ln1e4mep7z08vqq2pjsltpf6uykcga3ylkmdaunkwyyrteo82vd45c61ap8v0wy2.png" %}
***Time Zone and Locale in the "My Settings" menu***
{% /image %}

- **Admin User Failsafe**: Ensures that there is always at least one admin user to maintain platform security and control.

**Improvements**

- **YARA Rule Updates**: Reviewed and vetted third-party YARA rules. By default, YARA rules are loaded with priority from the OPSWAT repository.
- **Improved IOC Extraction**: Enhanced the extraction of indicators of compromise (IOC) from emulation for a more comprehensive report.
- **Better XOR Decryption**: Extended XOR decryption capabilities, improving analysis of encrypted malware.
- **Python Script Detection**: Improved detection of malicious Python scripts, a growing vector for attacks.
- **API Enhancements**: Made API endpoints more robust, ensuring seamless integration and communication with other systems.
- **Simplified Configuration**: Streamlined the engine configuration with renamed property files, making it easier for admins to manage settings.
- **Enhanced Emulation**: Increased emulation success rates, particularly through better recognition of file content types eligible for emulation.
- **Malicious Document Detection**: Improved the detection of malicious documents, adding new indicators and reducing the risk of document-based attacks.
- **Reduced False Positives**: Lowered false positive rates for heuristically detected or non-clickable IP addresses and URLs, improving the accuracy of threat analysis.
- **Admin Panel Improvements**: Enhanced the grouping of settings in the Admin panel for better organization and ease of use.
- **Disassembly Section Update**: Now displays RVA in hexadecimal format in the disassembly section, providing more detailed information for advanced analysis.
- **VBA Macro Display**: Displays extracted VBA macros, offering greater visibility into potentially malicious code hidden in documents.
- **Context-Aware Threat Indicators**: Improved threat indicators by factoring in the context of the analysis, leading to more accurate threat assessments.

**Bug Fixes**

- **Broker API Authorization Fix :** Resolved an issue with secret handling in the broker API to improve security.
- **Cronjob Overlap Fix**: Fixed an issue with the overlapping execution of the Sandbox auto-restart cronjob which prevented automatic restarts under heavy load.
- **Certificate Extraction Fix**: Resolved a long scan execution issue caused by certificate extraction in offline environments for signed PE files.
- **Syslog Protocol Standardization**: Standardized the usage of the CEF Syslog protocol for more consistent logging and event tracking.
- **Local APT Repository Fix**: Fixed permission issues with the local APT repository on hardened operating systems, ensuring smoother package management for offline installations.
