---
type: page
title: Previous change logs
listed: true
description: 
index_title: Previous change logs
hidden: false
keywords: 
tags: 
---

---

### Release: 1.9.2

Date: 24 January, 2024

**Added:**

- New indicators for Windows APIs related to specific activities
- Implemented flagging for LSASS dump using minidump
- Extracted remote templates inside xTable struct in MS Office documents
- Implemented parser for Debian packages

**Changed:**

- Renamed OPSWAT Filescan Sandbox to [**MetaDefender Sandbox**](https://www.opswat.com/products/metadefender/sandbox)
- Expanded malware configuration extractors to encompass the latest and most pertinent threats
- Improved detection of dynamic syscalls using the HellsGate bypass technique
- Enhanced Quishing and Phishing email detection
- Improved the capabilities of Batch, CSV, HTA, JavaScript, LNK, PowerShell, VBA, and VBScript emulation and fine-tuned timeout handling
- Extended log messages to provide better traceability across various system components

**Fixed:**

- Pinned the installed Docker version to 24 due to the breaking changes introduced in Docker 25
- Enhanced Application Security measures, especially for PowerShell emulation
- Fixed incomplete invitation URLs in User Management
- Resolved file scanning issue when file content was sent to the API in JSON body
- Fixed the MISP format when exporting scan reports
- Refactored functional tests for the Webservice API and resolved potential runtime issues
- Fixed several UTF-8 parsing issues in content parsers (related to HTML \& OLE files)
- Ensured that all whitelisted submissions get the Benign verdict
- Improved the stability of concurrent OSINT lookup tasks

---

### Release: 1.9.1

Date: 22 November, 2023

{% callout type="warning" title="Warning" %}
This version is not suitable for a clean installation due to breaking changes introduced in Docker 25. Please **use version 1.9.2 or later** for clean installations!
{% /callout %}

**Added:**

- Integrated OPSWAT Central Management (OCM) into the Web UI: [OCM Registration](../installation/ocm-registration.md)

{% image url="https://uploads.developerhub.io/prod/XX2D/ae99i5rz6qrrc2e89mkx2wswahb2sl4o464ho663es7dz9hshpmcb4ixgv21v4o9.png" /%}

- Automatic email notifications with the original email sender when scanning .eml files: [Email Notifications](../configuration/email-notifications.md)
- Detected and flagged .exe suffixes in URLs to highlight potential downloads of PEs
- Displayed additional Crypto Wallet Indicators of Compromise (IOCs) in scan reports
- Displayed the product's current version in the Web UI footer
- Showcased top malware families in the Trends page
- Identified clickable and non-clickable URLs from documents
- Implemented disassembly of relevant functions in 64-bit executables
- Implemented a parser for .ics files (vCalendar), including the extraction of attached files
- Extended support for JavaScript emulation in Adobe PDF files
- Enabled threat indicator monitoring and statistics support
- Enabled support for all file types when generating an executive summary using OpenAI’s GPT large language model (LLM): [ChatGPT (Executive Summary)](../integrations/open-ai-executive-summary.md)

**Changed:**

- Revamped the processing of threat indicators and the methodology behind verdict calculations
- Augmented documentation and introduced an automated system check to verify the utilization of CPUs with AVX support. [Technical Requirements](../installation/technical-requirements.md)
- Expanded malware configuration extractors to encompass the latest and most pertinent threats

{% image url="https://uploads.developerhub.io/prod/XX2D/obvs4pc14q0pba7yh2jgg9a7qmx522g35iw1v3f3y487tm8aq4thw7iakhqscmtf.png" /%}

- Implemented the generation of randomized internal passwords for fsBroker and fsTransform components during the installation process
- Upgraded the detection capabilities to more effectively identify malicious office documents
- Improved the extraction process for Crypto Wallets to ensure a more comprehensive and accurate output
- Fine-tuned the extraction of overlay elements in PDF files for increased precision
- Strengthened the system's capability to handle malformed Microsoft Office documents
- Enhanced heuristic domain identification to minimize false positives
- Improved the identification and parsing of VBA content within PDF files
- Enhanced memory management within the scan engine to boost overall efficiency
- Improved parsing for .NET executables for more accurate analysis
- Enhanced parsing for YARA rules to achieve greater precision in matching
- Improved the reporting mechanism for identifying and handling invalid signatures during certificate validation
- Elevated the capabilities of VBA and PowerShell emulation for heightened security measures
- Incorporated confidence values in phishing detections, influencing the final verdict for URL rendering
- Updated the "Download IOCs" button to selectively download items solely from the current page
- Refreshed the internal FSIO fuzzy hash blocklist to encompass emerging threat clusters

**Fixed:**

- Enhanced Application Security measures
- Improved health check functionality in scan job queues, automatically restarting when required
- Eliminated weak third-party YARA rules to prevent False Positives

---

### Release: 1.9.0

Date: 14 September, 2023

{% callout type="warning" title="Warning" %}
This version is not suitable for a clean installation due to breaking changes introduced in Docker 25. Please **use version 1.9.2 or later** for clean installations!
{% /callout %}

Added:

- New License Management interface added to the Web UI: [License Activation](../installation/license-activation.md)
- Automatically generate an executive summary with OpenAI’s GPT large language model (LLM): [ChatGPT (Executive Summary)](../integrations/open-ai-executive-summary.md)

{% image url="https://uploads.developerhub.io/prod/XX2D/pmclkopix4bom5cyjsfcqeu65rfd5u8jwl106kv06kk6c925kqxte9v4tcb170nk.png" /%}

- Support different retention periods for different verdicts
- The /api/scan/file API endpoint accepts base64-encoded file content in the JSON request body
- Support filenames with various unicode characters
- Support unpacking of 64-bit executables
- Integrated "[Detect It Easy](https://github.com/horsicq/Detect-It-Easy)" to identify characteristics of executable files related to compilation and packing
- Support malicious documents embedded in PDF files hidden as ActiveMime objects in MHTML format
- New threat indicators to detect the WikiLoader malware family (Microsoft Office files)
- Detection and extraction of embedded RTF files in Office documents, as described in [CVE-2023-36884](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36884)
- Detect XOR decoding routine near the executable entry point
- Enhance Threat Indicator for [Mavinject](https://lolbas-project.github.io/lolbas/Binaries/Mavinject/)

{% image url="https://uploads.developerhub.io/prod/XX2D/8pplvmn0ly267eeq3e215xchiyulj183dxclsar858xnmml7pp9niav3lnni9ueq.png" %}
Adversaries may abuse mavinject.exe to proxy execution of malicious code. Mavinject.exe is the Microsoft Application Virtualization Injector, a Windows utility that can inject code into external processes as part of Microsoft Application Virtualization (App-V) See example and new threat indicator.\
[https://attack.mitre.org/techniques/T1218/013/](https://attack.mitre.org/techniques/T1218/013/)
{% /image %}

Changed:

- Faster scan processing time
- Enhanced logging to provide more relevant information
- Improved VBA emulation to support additional features
- Refined emulation error handling for higher success ratio
- Enhanced threat indicators and verdict calculation
- Improved string analysis
- Optimized disk space utilization \& clean-up mechanisms
- Enhanced MITRE mapping for user clarity
- Enhanced flagging for suspicious imported APIs and modules

Fixed:

- Added version locks for dependencies in various emulator components
- Improved application security
- Incorrect detection of zip bombs
- Incorrect condition for the emulation of ActiveMime files
- Improved processing of large sample files

---

### Release: 1.8.1

Date: 14 July, 2023

{% callout type="warning" title="Warning" %}
This version is not suitable for a clean installation due to breaking changes introduced in Docker 25. Please **use version 1.9.2 or later** for clean installations!
{% /callout %}

Added:

- Compliance with CIS Level 1 OS hardening: [https://www.cisecurity.org/cis-benchmarks](https://www.cisecurity.org/cis-benchmarks)
- Detection for fast reverse proxy
- Detection for suspicious file extensions
- Detection for RCE in Office files (leveraged in CVE-2022-30190)
- Collector for identified packer statistics
- Indicator for malicious files with .scr extension
- Flagging for common words used as filename in phishing-delivered artifacts
- Increase brand coverage for phishing detection to support 300 brands
- Possibility to regenerate API key
- Buttons to download certificates and public key files

{% image url="https://uploads.developerhub.io/prod/XX2D/2xcxvu5tnqmqmq27iy4rjart56u866p74uqqwx4oy4cgazt4rl7ebrpej184yvz3.png" width=1000 /%}

Changed:

- Improved file type detection for more precise accuracy
- Improved VBA emulation to support additional features
- Improved emulation error handling to have a better success ratio
- Improved privacy and handling of personal information
- Improved verdict calculation
- Improved string analysis
- Improved detection and tagging of LOLBins
- Improved analysis of emulation indicators for dynamically allocated Windows APIs
- Improved analysis of URLs to detect commonly abused web services for Command and Control or exfiltration
- Improved logging and logging configuration
- Improved installation process (compatibility with hardened Ubuntu systems)
- Show if advanced scan options have been used

{% image url="https://uploads.developerhub.io/prod/XX2D/hpt4v3fdj0yrvxiqg4ph7v8pu0bkwz913nyjfu3f5cxyqm08gbo8rmca480afvpq.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/txia2ihlfi4dcge7zl1oan740ps6i6ppz8sypm1ryit685hjre05ocnqe45fa4kv.png" /%}

Fixed:

- Added version lock-in for some URL scanning container dependencies
- Fixed a crash that could occur when specific brands were detected (Coinbase, JCB)
- Bugs within YARA rule score parsing
- Issues and incorrect classification with identification and tagging of registry files
- Improved parsing for registry key paths
- Issues and misclassification of OSINT lookups for extracted hashes
- Improved report generator to be resilient against phishing detection failing in the URL scanning task

---

### Release: 1.8.0

Date: 8 June, 2023

{% callout type="warning" title="Warning" %}
This version is not suitable for a clean installation due to breaking changes introduced in Docker 25. Please **use version 1.9.2 or later** for clean installations!
{% /callout %}

Added:

- A new **single source of truth** reputation lookup for Hashes, URLs, IPs, and Domains. Automatically integrated with [MDCloud](https://docs.opswat.com/mdcloud) look up. Always yielding a result, independent of whether a report was generated for the search query.

{% image url="https://uploads.developerhub.io/prod/XX2D/sxq4cwh240m4qm5yyb0r4ylxdtsz403sbnes2kcxer57gi5m7b46so26nbvclz1q.png" /%}

- Threat Intelligence Similarity Search feature for Portable Executable (PE) files

{% image url="https://uploads.developerhub.io/prod/XX2D/5cwr31a79mzoo60dddpga6710r1id2fssk9coc5sr2c8279xrnps3cx8mgleq4si.png" /%}

- Emulation metadata parsing from self-extracting archive files
- Detection of appended files in images with steganography
- Administrative feature to overrule scan report verdict
- Detection of file executions initiated by msiexec on remotely fetched MSI files

Changed:

- Extended certificate whitelisting with QT Framework signatures
- Extended Filescan Reputation API with support for IPs, domains and URLs
- Extended Filescan Fuzzy Hash blacklist hits with additional details
- Optimized JPG processing speed
- Fine -tuned YARA rule behaviors
- Fine-tuned fuzzy hash lookup verdict contribution
- Improved RTF emulation success rate
- Enhanced startup time with lighting fast speed and performance
- Improved verdict calculation

Fixed:

- Service stability issues
- Service availability issues via automated restart mechanism
- Backend disk usage issues
- Backend service error handling issues
- Phishing URL detection issues
- OSINT provider verdict standardization issues

---

### Release: 1.7.4

Date: 20 April, 2023

Added:

- Added[ Status Page ](https://www.filescan.io/help/status)to inform users about historical health
- ‘What is your opinion about this sample’ vote feature, to influence accuracy of the Filescan verdict engine by users
- [Reputation API](https://docs.opswat.com/filescan/opswat-filescan/ref) with improved performance to provide overall verdict for SHA256 hashes, based on different trusted sources
- Yara rules now available in offline mode (static database, updated with each release)

Changed:

- Support for additional file types (TNEF, OneNote)
- Improvement on verdict precision (ex.: detect invalid digital certifications as malicious, detect suspicious Python patterns)

Fixed:

- Product installer - several native dependencies and Python packages are bundled into the installer, reducing installation time and potential issues
- Verdict inaccuracies

---

### Release: 1.7.3

Date: 10 February, 2023

Added:

- Trends page added - statistics on global trends and recent activities
- OPSWAT license activation solution added
- MetaDefender Multiscanning
- FSIO Fuzzy hash lookup

Changed:

- Verdict precision
- Fuzzyhash blacklist in OSINT section

Fixed:

- Product installer
- Verdict inaccuracies

---

### Release: 1.7.2

Date: 10 February, 2023

Added:

- OPSWAT Reputation lookup integration, including performance boost for the verdict
- Configurable retention policy (based on age/verdict)

Changed:

- Improvements on:
  - Emulation engine performance
  - Support for air gapped environments
  - FP/FN ratio, especially for PE installers
  - Number of threat indicators
- Detection of INNO installers

Fixed:

- Fix PDF parser issues
- Text and date format
- File re-scan job
- Various improvements on verdict accuracy
- Scan progress accuracy

---

### Release: 1.7.1

Date: 19 January, 2023

Added:

- Mime type composition overview for archives
- File upload and time estimate for large file uploads
- Added file extraction for MSI installers
- Added archive verdict based on all child items

Changed:

- Improved MSI installer detection (heuristic)

Fixed:

- Fixed a rare concurrency issue with the refresh token
- Fixed an issue where some child item reports would only appear belated in the overview page
- Various minor fixes

---

### Release: 1.70

Date: 16 December, 2022

Added:

- Support for VHD(x) file formats
- Added a logo picker that can be used to re-brand the product
- Added the option to disable the T\&C accept checkbox (admin backend)
- Added the option to specify the product name (admin backend)
- Added better support for large PE files (\>100MB)
- Added new threat indicators covering CPL file anomalies
- Added 'runYaraRulesOnInputFileMaxFileSizeInMb' for better control on when to skip YARA being applied to the input file
- Added media-type based prioritizing of archive files
- Added separately configurable max. processing thresholds for archive submissions
- Added media type to the /submit endpoint response (fsBroker)
- Added composition fields containing counters for all submitted, accepted and rejected files

Changed:

- Updated emulation engine
- Updated documentation (added troubleshooting guide)
- Improved heuristic javascript/vbs/powershell detection for text files without a suffix
- Default max. file size for processing is now 2GB

Fixed:

- Some potential performance issues with statistics related DB queries

---

### Release: 1.63

Date: 28 November, 2022

Fixed:

- remove "null"-byte padding from Javascript, which was throwing off the emulator

Release: 1.62

Date: 28th of November, 2022

Fixed:

- fsBroker retry attempts would only try one time (verifyAppServersAreAvailableRetryMax) breaking automatic service restarts on slow machines

---

### Release: 1.61

Date: 25 November, 2022

Added:

- Added support for ASF file parsing (WMV)
- Added support for CAB archives
- Added a capability to restart webservice without rebuilding docker

Changed:

- Updated emulation engine
- Updated documentation

Fixed:

- Fixed a false positive for DOTM files containing URLs

---

### Release: 1.60

Date: 28 October, 2022

Added:

- Added ability to extract and validate certificate data from OOXML files
- Added sample feed (public/private) with archive downloads
- Added support for CustomXMLParts
- Added support for the Format function
- Added "runWebserviceHealthCheckGracefulExitIfLastSuccessOlderThanXSec" to initiiate a soft restart in a rare deadlock scenario
- Added support for ACE files
- Added support for Microsoft Store apps ("ms-appx" tag and mime-type "application/vns.ms-appx")
- Added ability to specify multiple VirusTotal API keys in fsTransform
- Added ability to disable OSINT cache (see 'enableOSINTCache')
- Added ability to abort additional OSINT lookups if malware found (see 'abortOSINTLookupIfAnyProviderFoundMalware')
- Added a configurable "dark mode" for the webservice UX
- Added a beta-version of "Rapid mode" and individually configurable analysis options on the submission dialogue (admin-only)

Changed:

- Performance improvements for OOXML files with many AX controls
- Improved detection of embedded PE files
- Improved the performance of webservice background jobs
- Improved handling very large (50MB+) PDF and PE files

Fixed:

- Fixed a few minor bugs in the emulation engine

---

**Installation Guide**

1. Navigate to “RELEASE” and download "FileScanIO Quick Start Guide”
2. Download "fsBootstrap.zip" and "FileScanIO.zip" (\~779 MB)

SHA-256 fsBootstrap: 77f73891e16d3b2aced1c8a0a71f02ed26c95b589fc2ad190bf488bfde72632d

SHA-256 FileScanIO.zip: e2c4edb921c9ef0fcedf22a0172adcaf3e2bac3519bc9c02598c6180e2d33ae5

3. Follow the "FileScanIO Quick Start Guide" and use the fsBootstrap password **fsBootstrap 1.7.0 password: CUT9g2fPadWgH0tHM8gM**  as per guide.

*Note: please take note of the system requirements as outlined in the guide. As a general guidance, the better the hardware (CPU/RAM/Disc IOPS), the better the overall system performance.*

---

**ARCHIVE**

fsBootstrap 1.6.3 password: uLDHMMG4aGNlp6F0aUzI

fsBootstrap 1.6.1 password: JKHh8QE7EuquMFsNihP9

fsBootstrap 1.60RC1 password: k6HDFq5FZN3HnIp8NM7G
