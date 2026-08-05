---
type: page
title: Release Notes for v2.5.0
listed: true
description: 
index_title: Release Notes for v2.5.0
hidden: false
keywords: 
tags: 
---

## Date: 27 October, 2025

{% callout title="Awareness" %}
OPSWAT releases **MetaDefender Sandbox 2.5.0,** enabling faster IOC updates, broader threat coverage of malware families, and deeper visibility.
{% /callout %}

## MetaDefender Sandbox 2.5.0 Release Notes

**Sandbox 2.5.0** adds Rocky Linux support, MP3 analysis, offline certificate validation, and enhanced emulation.

### What's New

- **Periodic Threat Detection Updates -** MetaDefender Sandbox now supports independent updates of detection logic and threat indicators, ensuring faster deployment of new protections and quicker response to emerging threats.
- **Rocky Linux Support** – Added full support for Rocky Linux, including installation pipelines, testing, and release documentation, ensuring reliable Sandbox deployments on this platform.
- **Web Threat Detection** - Enhanced ML-based detection with multi-label classification, advanced content analysis, automated data pipelines, improved false positive handling, and style analysis.

{% image url="../../assets/bde32cd7ee097e53388ee09d54a78b17cfd9cd74.png" %}
URL Details
{% /image %}

- **MP3 Filetype Support** – Expanded filetype coverage with MP3 parsing and analysis.

### Improvements

- **Trends Page Updates** – Redesigned Trends pages with new tabs, filters, charts, and components, improved mobile responsiveness, and connected statistics and backend jobs for better performance.
- **Verdict Renaming** – Implemented UI-only renaming of verdicts with dynamic mapping to maintain backward compatibility in the API and database, including the addition of a SYSTEM\_ERROR verdict and support for both old and new verdicts in API responses.
- **Updated Translations** –Refined translations for a smoother, more consistent user experience.
- **Emulation Graph Enhancements** – Updated the emulation graph to highlight processes by threat level, making it easier to identify malicious or suspicious activity.

{% image url="../../assets/8707cdf9dce1ed79eb5335026607c0d8ad050844.png" %}
Improved emulation graph
{% /image %}

### Bug Fixes

- **Authentication UX** – Corrected several login and password handling issues, including error placement, unclickable buttons, and empty input handling.
- **Report \& UI** – Resolved report duplication, tag sizing, long URL formatting, PDF preview errors, and navigation inconsistencies.
- **Emulation Page** – Fixed 500 error occurring when loading the Emulation page.
- **Incorrect URL Extraction** – Resolved parsing issues causing incomplete or inaccurate URL extraction.
- **Reporting \& Metadata** – Corrected metadata keys to ensure consistency.
- **Offline License Activation** – Resolved an issue with offline license activation caused by an unreadable file.

## PE Emulator (Beta) Release Notes

- **PE Section Handling** – Improved emulation memory management for emulated PE mapping
- **Covert API Lookups** – Sandbox now reports API lookups directly from the export table (as opposed to conventional GetProcAddress)

## MetaDefender Sandbox 2.5.0 Threat Detection Release Notes

The latest Threat Detection updates include capability to detect AI-based evasion techniques, advanced installer and filetype support, and improved zero-day defence, empowering organizations with proactive, agile protection against modern threats.

### What’s new

- **Periodic Threat Detection Updates -** The latest Threat Detection updates include capability to detect AI-based evasion techniques, advanced installer and filetype support, and improved zero-day defence, empowering organizations with proactive, agile protection against modern threats.
- **Double Base64 Decoding** – Detects payloads hidden in multiple layers of Base64 encoding, commonly used by advanced malware to evade security controls.
- **Extended Threat Indicators for Pickle \& PyTorch** – Detects weaponized Python serialization and machine learning model files often used for supply chain and AI-related attacks.

{% image url="../../assets/42402c79e2e716291fcfe45e88f4ef9b1dc1248e.png" %}
Detection of Pickle file capabilities
{% /image %}

- **Improved AI Evasion Detection** – Enhanced identification of the **nullifAI evasion technique** and **stack pickle manipulations**, strengthening AI/ML malware defense.

{% image url="../../assets/9b655cf245b2d5a1eb307f3ac985f4889a0b9c52.png" %}
Stacked Pickle trick evasion
{% /image %}

- **New Installer Package Support** – Added extraction and analysis for:
  - **Advanced Installer packages**
  - **NSIS (Nullsoft Scriptable Install System) packages**
  - **Inno Setup packages**
  - **Wise Installer packages** - This expands coverage for malware distributed via custom installer frameworks.

{% image url="../../assets/4d6f5c4b1d658d10fa4b7b7229c611102742dbbb.png" %}
Static file extraction for PE installer
{% /image %}

{% image url="../../assets/a641c41e1ad7364447d216b30c62453b5a124704.png" %}
Threat indicators detecting actions defined in installer scripts
{% /image %}

- **CVE-2018-15982 Detection** – Identifies exploitation of a critical Adobe Flash vulnerability.
- **Equation Editor Exploit Detection** – Detects obfuscated versions of this long-abused Microsoft Office exploit.

{% image url="../../assets/f825fdf02ca302a6a8098a6051ed2d00aab62f0d.png" %}
Signal group and threat indicator detecting obfuscated and malformed exploit document
{% /image %}

- **Extended PDF Threat Indicators** – Better phishing detection in PDF documents, with new heuristics for malicious links and embedded content.
