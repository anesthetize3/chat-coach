---
type: page
title: Scan URL on the UI
listed: true
description: 
index_title: Scan URL on the UI
hidden: false
keywords: 
tags: 
---

### Step 1- Go to [filescan.io/scan](https://www.filescan.io/scan)  page

*(replace the domain with your local/cloud version)*

Paste the target URL address to the text field and click the "**Analyze Link**" button.

{% image url="../../../assets/a850881c3fcb40d82f630e38737fd976da980fbb.png" /%}

### Step 2 - Customize analysis options and accept the Term of Use and Privacy Policy

#### Basic Options

{% image url="../../../assets/fba9c7efba3084b71bdb2eabdbe025c9964f71d5.png" /%}

**Tags:** You can add some description with #tags

**{% badge text="Optional" type="success" /%}** You can apply some optional settings:

- ***Password***: You could provide a password for password-protected archives. The following common password will be applied automatically if archive uses common password:
  - “infected”
  - “malware”
  - “virus”
  - “password”
- ***Do not share file***: This setting prohibits other community members from accessing the file. However, the reports remain public (Including screenshots and extracted texts.)
- ***Skip whitelisted***: If the file is detected as "whitelisted", the file won't be scanned and report won't be created.

#### Advanced Options

{% image url="../../../assets/fe9c5f54512cfd2bcee994d142663048ddca75f7.png" /%}

{% badge text="Optional" type="success" /%} {% badge text="Authentication required" type="warning" /%} For advanced options you must be authenticated. Advanced options are:

- ***Pre-configured analysis options***: It excludes the apply\_fine-tune\_analysis use case. If you apply this setting, then the system will apply a preconfigured profile to execute the scan. -
- ***Fine-tune key aspects of your analysis***: You can choose from the following list. The selection is optional. It is not required to select at least one.
  - **YARA (Basic)** - *Enabling YARA rule matches on input file*
  - **YARA (All)** - *Enabling YARA rule matches on extracted artefacts*
  - **File visualization** - *Enabling file visualization (e.g. PDF rendering)*
  - **Images OCR** - *Enabling OCR text recognition on extracted images*
  - **File downloads** - *Enabling downloading files from extracted URLs*
  - **OSINT Lookups** - *Enable OSINT Lookups globally*
  - **OSINT Lookups (Basic)** *- Enable OSINT Lookups on the IOCs related to the input file*
  - **OSINT Lookups (All)** *- Enable OSINT Lookups also on the extracted artifacts*
  - **Domain resolving** *- Enable Resolving domains to the IPs (DNS)*
  - **WHOIS** - *Enable WHOIS record lookups*
  - **IP geolocation** *- Enable metadata lookups for Extracted IDs*
- ***Personalization:*** You can apply this feature to save the selected configuration.
  - **Save preset**

{% image url="../../../assets/ac53e63ba34766aa4d1c8144ab0397a1f87d09dc.png" /%}

### Step 3 - Accept the Term of Use and Privacy Policy

{% badge text="Required" type="error" /%} For scan it is necessary to accept the Term of Use and Privacy Policy.

{% image url="../../../assets/4b2aa6cded8c7c9c64973b40658aa9c41ff32679.png" /%}

### Step 4 - Get the report

After clicking the Upload button, the scanning starts. The report will appear after the scanning is finished.

{% image url="../../../assets/f0eee366121a2a4a5cca7f773d77b63da7fea775.png" /%}
