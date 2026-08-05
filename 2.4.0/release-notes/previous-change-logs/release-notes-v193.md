---
type: page
title: Release Notes for v1.9.3
listed: true
description: 
index_title: Release Notes for v1.9.3
hidden: false
keywords: 
tags: 
---

---

## Date: 26 March, 2024

**Added:**

- Python Unpacking \& Decompilation for PyInstaller, Nuitka, and py2exe

{% image url="https://uploads.developerhub.io/prod/XX2D/o4kfahecjuspog1hbz1c83bihhrabbsfomh40rku776l4phtxmsmrojka3la6bte.png" /%}

- Extended the malware configuration extractor to support the Cobalt Strike malware family

{% image url="https://uploads.developerhub.io/prod/XX2D/cy1dx2dwjc37jsouz0mbfrl5447wt6gwflte14u32ptkmnrad70gwjp1gacw7i8k.png" /%}

- Included disassembly of exported functions for Windows binaries
- Threat indicator to flag when executable files have two different sections with the same section name
- Extraction of VBA macro code from DWG files (shown as OLE Stream in File Details section)
- Support for MITRE Att\&ack technique mapping from Yara rule metadata

{% image url="https://uploads.developerhub.io/prod/XX2D/zll8i3jfpqofh1kue1l4nm0fgc2va6xolvgr7qatq1hz6ywl972dgwhykamtue6f.png" /%}

- New DotnetInfo tab in the File Details section for .NET executables
- Added the “auditor” role, which functions as a read-only admin role
- MISP integration options in Admin Settings, see details at [MISP](../../integrations/misp.md)
- Added support for new Sandbox installations on Ubuntu 22.04 (it will be possible to upgrade the OS on older installations with the next major release coming later in 2024)

**Changed:**

- Improved proxy handling and proxy related bug fixes, see configuration details at [Proxy Usage](../../installation/quick-installation/installation-with-proxy.md)
- Enhanced script language detection using the guesslang library
- Fine-tuned several threat indicators to reduce false positive ratio
- Return "Unknown" verdict if no threat indicators are generated for URL and file submissions
- Improved detection for phishing calendar invites
- Enhanced recursive analysis of active content containers (email, Office documents, PDF, etc.)
- Improved scan process for corrupt OLE2 documents
- Return HTTP 429 responses to new scan requests when the scan queue is full
- Long-running scans are cancelled after user-defined timeout
- Show queue count statistics in Admin Panel/Statistics/Jobs/Scan Health
- Enhanced system resilience by continuing interrupted scans after a queue restart
- Improved URL rendering to bypass simple human verification check boxes (e.g. Cloudflare)
- Improved compatibility for filenames with special characters

**Fixed:**

- Resolved issues with license actions (deactivation, inconsistent states)
- Fixed several issues with existing threat indicators (ELF binaries, URL extraction, EML)
- Enhanced Application Security measures, especially for URL emulation
- Invitation links should work even if the "Sign up" feature is disabled
- Extended functional tests for the Webservice API and resolved potential runtime issues
- Fixed simple search not working for tags, e.g. #html
- URL preview should be displayed automatically on URL details page
- Only execute Similarity Search if the original verdict matches the specified configuration
