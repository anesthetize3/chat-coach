---
type: page
title: Scan URL on the UI
listed: true
description: 
index_title: Scan URL on the UI
hidden: true
keywords: 
tags: 
---

**Step #1**- Go to [filescan.io/scan](https://www.filescan.io/scan)  page (replace the domain with your local/cloud version) and paste the target URL address to the text field and click the "Analyze" button.

{% image url="https://uploads.developerhub.io/prod/XX2D/ijzqtlc55h79qb5ljocxvo13af4l0x7vq6kmkrnblo5nyg5od7a0ndn6l0jbnnsg.png" /%}

**Step #2** - Customize options and accept the Term of Use and Privacy Policy

{% badge text="Required" type="error" /%} For scan it is necessary to accept the Term of Use and Privacy Policy.

**{% badge text="Optional" type="success" /%}** You can apply some optional settings:

- Password: You could provide a password for password-protected archives. The following common password will be applied automatically if no password is provided:
  - “infected”
  - “malware”
  - “virus”
  - “password”
- Do not share file: This setting prohibits other community members from accessing the file. However, the reports remain public.
- Skip whitelisted:  If the file is detected as "whitelisted", the file won't be scanned.

You can also add some description with #tags.

{% badge text="Optional" type="success" /%} {% badge text="Authentication required" type="warning" /%} For advanced options you must be authenticated. Advanced options are:

- Pre-configured analysis options: It excludes the apply\_fine-tune\_analysis use case. If you apply this setting, then the system will apply a preconfigured profile to execute the scan.
  - Rapid mode
- Fine-tune key aspects of your analysis: You can choose from the following list. The selection is optional. It is not required to select at least one.
  - YARA (Basic)
  - YARA (All)
  - File visualization
  - Images OCR
  - File downloads
  - OSINT Lookups
  - OSINT Lookups (Basic)
  - OSINT Lookups (All)
  - Domain resolving
  - WHOIS
  - IP geolocation
- Personalization: You can apply this feature to save the selected configuration.
  - Save preset

{% image url="https://uploads.developerhub.io/prod/XX2D/vmlyrt0o5a3tuz3chwx3kj7owm5lauqldlodllpinn9ijt6rst4stefzv1q90jke.png" /%}

**Step #3** - After clicking the Upload button, the scanning starts. The report will appear after the scanning is finished.

{% image url="https://uploads.developerhub.io/prod/XX2D/g1vq6n0sbm10rzwuhpwslaiz1j9n6a3v7iy0fywz73u86ryzi9rxbd3nri8mohj4.png" /%}
