---
type: page
title: Sandbox Tags
listed: true
description: 
index_title: Sandbox Tags
hidden: true
keywords: 
tags: 
---

Tags are automatically generated based on the sample's analysis, providing a concise summary of key findings.

Tags are color-coded based on their severity context, with common colors like {% badge text="mediatype" /%}, {% badge text="likely malicious or malicious" type="error" /%}, and {% badge text="no threat" type="primary" /%} or {% badge text="suspicious" type="warning" /%}.

Some tags are dynamically derived from sandbox components or external sources, including:

- Threat indicators,
- YARA rules,
- Malware family attribution from [supported configuration extractors](metadefender-sandbox/2.1.0/datasheet/supported-malwares-for-config-extraction)
- CVE identifiers related to vulnerabilities,
- MISP Galaxy family names.

{% callout title="Info" %}
Note that [each supported file type](/metadefender-sandbox/2.2.0/datasheet/supported-file-types) has its own media type tag not listed here!
{% /callout %}

{% tabs %}
{% tab title="Analysis Tags (Sorted)" %}
{% callout type="warning" title="Attention!" %}
Color used for each {% badge text="tag" /%} does not represent the actual severity.
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[206] %}
Tag
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="64bits" /%}
{% /cell %}
{% cell %}
Targets 64-bit architecture
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="adaptive-context" /%}
{% /cell %}
{% cell %}
Threat indicator severity has been adjusted based on the adaptive context
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="adware" /%}
{% /cell %}
{% cell %}
Displays unwanted ads or collects data for advertising purposes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="anti-debug" /%}
{% /cell %}
{% cell %}
Contains anti-debugging capabilities
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="anti-security" /%}
{% /cell %}
{% cell %}
Attempts to disable or evade security tools
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="anti-vm" /%}
{% /cell %}
{% cell %}
Detects virtual environments
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="apt" /%}
{% /cell %}
{% cell %}
Found Advanced Persistent Threat-related activities
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="backdoor" /%}
{% /cell %}
{% cell %}
Provides a backdoor for unauthorized remote access
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="banker" /%}
{% /cell %}
{% cell %}
Targets financial data
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="bloated" /%}
{% /cell %}
{% cell %}
Bloated executable to evade heuristic and malware analysis
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="botnet" /%}
{% /cell %}
{% cell %}
Attempts botnet communication
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="byovd" /%}
{% /cell %}
{% cell %}
Brings Your Own Vulnerable Driver to exploit kernel vulnerabilities
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="compiled-script" /%}
{% /cell %}
{% cell %}
Script compiled into an executable file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="corrupted" /%}
{% /cell %}
{% cell %}
Damaged or malformed file, often to evade analysis
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="cpl" /%}
{% /cell %}
{% cell %}
Windows Control Panel
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="crypto" /%}
{% /cell %}
{% cell %}
Involves cryptographic operations
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="delphi" /%}
{% /cell %}
{% cell %}
Delphi programming language
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="disassembled" /%}
{% /cell %}
{% cell %}
Contains disassembled code
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="dropper" /%}
{% /cell %}
{% cell %}
Delivers additional payloads
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="embedequation" /%}
{% /cell %}
{% cell %}
Contains embedded Office equation objects
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="evasive" /%}
{% /cell %}
{% cell %}
Attempts to evade detection
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="exploit" /%}
{% /cell %}
{% cell %}
Targets specific software vulnerabilities
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="fingerprint" /%}
{% /cell %}
{% cell %}
Gathers system information to identify or profile the environment
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="geofencing" /%}
{% /cell %}
{% cell %}
Enables malicious execution only in specific geographical regions
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="golang" /%}
{% /cell %}
{% cell %}
Go programming language
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="greyware" /%}
{% /cell %}
{% cell %}
Suspicious or potentially unwanted software (PUP)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="hacktool" /%}
{% /cell %}
{% cell %}
Detected hacktool artifacts
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="installer" /%}
{% /cell %}
{% cell %}
Identified as known installer
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="invalid-signature" /%}
{% /cell %}
{% cell %}
Contains a digital signature that is invalid or tampered with
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="keylogger" /%}
{% /cell %}
{% cell %}
Contains keylogging capabilities
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="language-x" /%}
{% /cell %}
{% cell %}
Identified language (being "x" the language code), which is often related to the attack target. Common codes are "uk" (Ukrainian), "ru" (Russian), or "zh" (Chinese)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="large-file" /%}
{% /cell %}
{% cell %}
A file unusually large, possibly bloated to hinder analysis
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="lolbin" /%}
{% /cell %}
{% cell %}
Living-off-the-land binary
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="macros" /%}
{% /cell %}
{% cell %}
Uses Office macros
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="macros-on-change" /%}
{% /cell %}
{% cell %}
Executes code when the document is edited
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="macros-on-close" /%}
{% /cell %}
{% cell %}
Executes code when the document is closed
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="macros-on-event" /%}
{% /cell %}
{% cell %}
Executes code on specific user or system event
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="macros-on-open" /%}
{% /cell %}
{% cell %}
Executes code when the document is open
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="masquerade" /%}
{% /cell %}
{% cell %}
Pretends to be legitimate software to deceive users
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="metasploit" /%}
{% /cell %}
{% cell %}
Linked to the Metasploit penetration testing framework
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="mirai" /%}
{% /cell %}
{% cell %}
Detected Mirai artifacts
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="monikerlink" /%}
{% /cell %}
{% cell %}
Exploits moniker-based links
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="msdt" /%}
{% /cell %}
{% cell %}
Leverages Microsoft Support Diagnostic Tool for execution
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="obfuscated" /%}
{% /cell %}
{% cell %}
Presents obfuscated data to evade detection
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="overlay" /%}
{% /cell %}
{% cell %}
Contains an overlay, appended data at the end of the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="packed" /%}
{% /cell %}
{% cell %}
Original executable has been packed to protect against analysis
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="persistence" /%}
{% /cell %}
{% cell %}
Gains persistence to maintain presence after a reboot
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="phishing" /%}
{% /cell %}
{% cell %}
Detected phishing attempt
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="ping" /%}
{% /cell %}
{% cell %}
Uses ping tool for checking connectivity
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="polyglot" /%}
{% /cell %}
{% cell %}
File which can be considered of multiple file types to bypass defenses
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="pyarmor" /%}
{% /cell %}
{% cell %}
Obfuscates Python scripts with Pyarmor
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="pyinstaller" /%}
{% /cell %}
{% cell %}
Python-compiled PE file with PyInstaller
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="qrcode" /%}
{% /cell %}
{% cell %}
Uses QR codes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="ransomware" /%}
{% /cell %}
{% cell %}
Detected ransomware activities
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="rat" /%}
{% /cell %}
{% cell %}
Detected Remote Access Trojan artifacts
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="reconnaissance" /%}
{% /cell %}
{% cell %}
File capabilities include information discovery/enumeration about the target system
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="reflection" /%}
{% /cell %}
{% cell %}
Executes code dynamically via NET reflection
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="revoked-cert" /%}
{% /cell %}
{% cell %}
Uses a certificate that has been revoked
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="self-signed-cert" /%}
{% /cell %}
{% cell %}
Uses self-signed and untrusted certificate
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="sendkeys" /%}
{% /cell %}
{% cell %}
Simulates user keystrokes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="sfx" /%}
{% /cell %}
{% cell %}
Self-extracting archive
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="shellcode" /%}
{% /cell %}
{% cell %}
Contains malicious shellcode
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="signed" /%}
{% /cell %}
{% cell %}
File is digitally signed
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="smb" /%}
{% /cell %}
{% cell %}
Performs Server Message Block (SMB) communication
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="spyware" /%}
{% /cell %}
{% cell %}
Monitors and exfiltrates sensitive user data
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="stealer" /%}
{% /cell %}
{% cell %}
Targets sensitive data
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="stripped" /%}
{% /cell %}
{% cell %}
Strips content to evade detection
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="tor" /%}
{% /cell %}
{% cell %}
Attempts TOR communication
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="vbastomped" /%}
{% /cell %}
{% cell %}
Detected VBA stomping to bypass detection
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="webdav" /%}
{% /cell %}
{% cell %}
Exploits WebDAV protocol for file transfer
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% badge text="wix" /%}
{% /cell %}
{% cell %}
Installer created using WiX toolset
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}
{% /tabs %}
