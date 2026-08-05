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

{% image url="https://uploads.developerhub.io/prod/XX2D/57t98l8gx7cut4vwtzh5t1sselltucf99qtz0l7c5pdetotr1wtk5d56g6vi9vlg.png" /%}

### Step 2 - Customize analysis options and accept the Term of Use and Privacy Policy

#### Basic Options

{% image url="https://uploads.developerhub.io/prod/XX2D/wzjtk1k5e852ktqu7xj3uhundr6v85hpwt7b0r6ifiwv1y3iql4xcdz1mpefyyoj.png" /%}

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

{% image url="https://uploads.developerhub.io/prod/XX2D/17zay7e5wwbiyclpb24ri3ng20w5wdw0aj81y14glsml5t2c64w22znws8ic5iph.png" /%}

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

{% image url="https://uploads.developerhub.io/prod/XX2D/dzbalyvsyosmlx94u0mgmjjaxdkil8lx0eooybmj4dpdpk946buyw1nhet22ardy.png" /%}

### Step 3 - Accept the Term of Use and Privacy Policy

{% badge text="Required" type="error" /%} For scan it is necessary to accept the Term of Use and Privacy Policy.

{% image url="https://uploads.developerhub.io/prod/XX2D/xm3uz988y0sap1dw9vx4cybfwgewh4a5odoftaginhawrj47vrxfb8ntyrrscgt5.png" /%}

### Step 4 - Get the report

After clicking the Upload button, the scanning starts. The report will appear after the scanning is finished.

{% image url="https://uploads.developerhub.io/prod/XX2D/lxyg0hjovjnmnpa0a20bqr7bqoik70i9pbic3jvwy5ckyybkodnva2f4zud8ybyv.png" /%}
