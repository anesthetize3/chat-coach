---
type: page
title: Release Notes for v2.0.0
listed: true
description: 
index_title: Release Notes for v2.0.0
hidden: true
keywords: 
tags: 
---

## Date: 18 July, 2024

{% callout type="warning" title="Warning" %}
This version is not suitable for a clean Sandbox installation. Please **use version 2.1.0 or later** for clean installations!
{% /callout %}

**Added:**

- New Streamlined Design for the User Interface

{% image url="https://uploads.developerhub.io/prod/XX2D/a4lpeqkl4yq65w16mzfz49t8zkmm18w6p7hdq8b0767yuoe8zca73405yelf65z6.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/0qudwazjvh4qbblksh5o5mbvtph0hkgpngnjuxbnvlgs3q4576xjlmofcvjydvd8.png" /%}

- Support for the installation of MetaDefender Sandbox on offline systems: [Offline Installation](../../installation/offline-installation.md)
- Audit Logger framework for admin settings and user authentication events: [Audit Logging for Admin Settings and User Authentication](../../configuration/monitoring-and-logging/audit-logger.md)

{% image url="https://uploads.developerhub.io/prod/XX2D/wns1yenvvb9oooyxvueh6ayw4zpdyfq7utpfm4dt8vkpfrgjxovieesbmeaeck72.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/d21ibv3aihooid0488dlw4hf5s0nh36sup1jr54j0vsq6tl1y9sjigvtzhtkm648.png" /%}

- Support for AutoIT script files, including compiled AutoIT Portable Executables

{% image url="https://uploads.developerhub.io/prod/XX2D/tjsute04bl3uwbj1tftbvzcqkasztyfmtjerud0tsdmrr5un4xtpf7ole0ljo2lp.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/xswpfhy1fngwc887q1prrgckan94ywb9jryqrbh68t57v6uk6y528tp78k5tcqr1.png" /%}

- Parsing of MSI metadata and actions, including implementation for filtered file extraction
- Parsing of ODF files and macro extraction
- Parsing of Python pickle files, including implementation for malicious Threat Indicators
- Capability to identify potential obfuscation for extracted macro code
- New Threat Indicator for deceptive filenames commonly used for phishing files
- New Threat Indicator for undetected Equation Editor RTF exploit
- New single configuration option for offline mode
- Introduced a Machine Learning model to identify suspicious URLs even in offline mode (this experimental feature is only enabled by default in offline mode): auto$

{% image url="https://uploads.developerhub.io/prod/XX2D/bybs1cxhe61caizn39xvc9ok1r36mt9fvb76ntzb0x1dfnw7w4lnjgph89qczr5s.png" /%}

**Changed:**

- **Potentially Breaking API change:** The **INFORMATIONAL** verdict was renamed to **NO\_THREAT** in the API results to be consistent with the “No Threat” verdict shown on the UI
- Changed the required operating system to Ubuntu 22.04 LTS. Existing Sandbox installations on Ubuntu 20.04 must be upgraded to 22.04 before installing Sandbox 2.0.0: [Operating System Upgrade](../../installation/quick-upgrade/operating-system-upgrade.md)
- Modified the system architecture to run all Sandbox components in Docker containers. This change improves application security and reduces the overall installation time to about 20 minutes
- Upgraded to Java 17 and Python 3.10 for all relevant Sandbox components
- Renamed the `fsiolog`  command to `sblog` (used to watch Sandbox logs in real time)
- Enhanced parsing of LNK metadata and actions, including new Threat Indicators
- Improved Python-specific Threat Indicators
- Added context info to strings originating from extracted files
- Include proper tags for Golang, Rust and compiled-Python Portable Executables
- Improved processing for nested extracted files
- Enhanced Threat Indicators for imported APIs and emulation respectively
- Improved OSINT lookup workflow
- Changed the default verdict to NO\_THREAT if no Threat Indicators are found
- Disabled the ClamAV task by default for improved performance
- Improved URL analysis performance and stability
- Reduced the scan time overhead associated with the webservice component

**Fixed:**

- Fixed minor bugs and misdetections
- Improved application security
- Improved emulation efficacy
- Improved application performance and stability
- Resolved file upload issue in the MetaDefender Core MultiScanning integration
- Fixed an issue causing the remaining daily scan count decreasing without actual scans
- Scan reports are marked as finished if a non-essential subtask reaches a timeout
