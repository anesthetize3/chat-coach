---
type: page
title: Upload a file on the UI
listed: true
description: 
index_title: Upload a file on the UI
hidden: false
keywords: 
tags: 
---

**How to upload and scan a file?**

### Step 1- Go to [filescan.io/scan](https://www.filescan.io/scan)  page

(replace the domain with your local/cloud version) and

- drag \& drop or
- upload a file via file browser after clicking on the box with the owl.

{% image url="https://uploads.developerhub.io/prod/XX2D/2c6r926hdy8wv5gnkieuej6s855efnvafyv7ndrwqclenl76g63qi7u2vtpe28gg.png" /%}

#### Uploading a file via File Browse

{% image url="https://uploads.developerhub.io/prod/XX2D/46l5zz857f7h10tflq8jqfojfa537hp8kbwe0b24ffrjy9vbc91tnt1d6bqlwfzl.png" /%}

### Step 2 - Customize analysis options

#### **Basic Options**

Set the most important analysis options for your upload

{% image url="https://uploads.developerhub.io/prod/XX2D/g0eacox1yhrw3a21b6xcodr39fesiopr5y4wmrx4p1au5mbjvvq5dxkzaley8e17.png" /%}

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

{% image url="https://uploads.developerhub.io/prod/XX2D/4n7kas7ms3n5sjtxr59okfil616cxkaivv4hjt8k4n0po5cr9mnxe1vpdg4lajrt.png" /%}

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

### Step 3 - Accept the Term of Use and Privacy Policy

{% badge text="Required" type="error" /%} For scan it is necessary to accept the Term of Use and Privacy Policy.

{% image url="https://uploads.developerhub.io/prod/XX2D/z0tolb8feodhc5deaperqsfzwxkh691p1pafc7hj4e7najrhbxqdq85pzqpdlnkh.png" /%}

### Step 4 - After clicking the Upload button, the scanning starts.

The report will appear after the scanning is finished.

{% image url="https://uploads.developerhub.io/prod/XX2D/82eq95bdo88lxgx75ndnwmucxn8eb5qju2vmfjrvzqytvjyj15z4z1pq8ck7m8ih.png" /%}
