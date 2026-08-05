---
type: page
title: Upload a file on the UI
listed: true
description: 
index_title: Upload a file on the UI
hidden: true
keywords: 
tags: 
---

**How to upload and scan a file?**

### Step 1 - Go to the main page

Navigate to the main page of your MetaDefender Aether instance and either drag and drop a file or upload one using the file browser by clicking on the upload area.

{% image url="../../../assets/07e3485cfd562472afd719a952551576f34d9f44.png" /%}

#### Uploading a file via File Browse

{% image url="../../../assets/db354aa6cd2fdb3486fa972fd5672d9faf5c8080.png" /%}

### Step 2 - Customize analysis options

#### **Basic Options**

Set the most important analysis options for your upload

{% image url="../../../assets/b160e6f6b091ddb6812fb1798b81d5a395b35a14.png" /%}

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

{% image url="../../../assets/3ec67e6f5c55480fc05d7431f2667fd8879d595e.png" /%}

{% badge text="Optional" type="success" /%} {% badge text="Authentication required" type="warning" /%} For advanced options you must be authenticated. Advanced options are:

- ***Pre-configured analysis options***: It excludes the apply\_fine-tune\_analysis use case. If you apply this setting, then the system will apply a preconfigured profile to execute the scan.
  - **Rapid mode** - Most simple analysis, disable multiple individual options
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

### Step 3 - Accept the Term of Use and Privacy Policy (Filescan.io)

{% badge text="Required" type="error" /%} For scan it is necessary to accept the Term of Use and Privacy Policy.

{% image url="../../../assets/4b2aa6cded8c7c9c64973b40658aa9c41ff32679.png" /%}

### Step 4 - Start the scan

After clicking the **Upload** button, the scanning process will begin.

{% image url="../../../assets/98898691ba99d41ca7b0852d3b88ab01d7678b8c.png" /%}
