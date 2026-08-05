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

Release: 1.7.3

Date: 10th of February, 2023

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

Release: 1.7.2

Date: 10th of February, 2023

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

Release: 1.7.1

Date: 19th of January, 2023

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

Release: 1.70

Date: 16th of December, 2022

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

Release: 1.63

Date: 28th of November, 2022

Fixed:

- remove "null"-byte padding from Javascript, which was throwing off the emulator

Release: 1.62

Date: 28th of November, 2022

Fixed:

- fsBroker retry attempts would only try one time (verifyAppServersAreAvailableRetryMax) breaking automatic service restarts on slow machines

---

Release: 1.61

Date: 25th of November, 2022

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

Release: 1.60

Date: 28th of October, 2022

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
