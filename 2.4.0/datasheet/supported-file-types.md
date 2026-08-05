---
type: page
title: Supported File Types
listed: true
description: 
index_title: Supported File Types
hidden: false
keywords: 
tags: 
---

{% callout title="Info" %}
MetaDefender Sandbox accepts files below the size limit for analysis. The table below lists the most prevalent file types officially supported, organized by category. Unlisted file types may yield less accurate analysis results.
{% /callout %}

## Application Files

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
A3X
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
AutoIt v3 Script
{% /cell %}
{% /row %}
{% row %}
{% cell %}
AU3
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
AutoIt v3 Script
{% /cell %}
{% /row %}
{% /table %}

## Office Documents

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DOCX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Word Document (.docx)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DOCM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Word Macro-Enabled Document (.docm)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DOTX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Word Template (.dotx)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DOTM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Word Macro-Enabled Template (.dotm)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DOC
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Word 97-2003 Document (.doc)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DOT
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Word 97-2003 Template (.dot)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLSX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel Workbook (.xlsx)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLSB
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel Binary Workbook
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLSM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel Macro-Enabled Workbook (.xlsm)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLS
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel 97-2003 Workbook (.xls)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLTX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel Template (.xltx)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLTM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel Macro-Enabled Template (.xltm)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PPTX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint Presentation (.pptx)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PPTM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint Macro-Enabled Presentation (.pptm)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PPSX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint Slide Show (.ppsx)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PPT
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint 97-2003 Presentation (.ppt)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PPAM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint Add-in
{% /cell %}
{% /row %}
{% row %}
{% cell %}
POTX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint Template
{% /cell %}
{% /row %}
{% row %}
{% cell %}
POTM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint Macro-Enabled Template
{% /cell %}
{% /row %}
{% row %}
{% cell %}
POT
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint 97-2003 Template
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ODT
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
OpenDocument Text
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ODS
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
OpenDocument Spreadsheet
{% /cell %}
{% /row %}
{% row %}
{% cell %}
RTF
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Rich Text Format
{% /cell %}
{% /row %}
{% row %}
{% cell %}
HWP
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Hangul Word Processor
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PUB
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Publisher
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ONE
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes, limited" type="success" /%}\*
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft OneNote exported section
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DOC95
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Word 95 Document (.doc)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DOT95
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Word 95 Template (.dot)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLS95
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel 95 Workbook (.xls)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PPT95
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft PowerPoint 95 Presentation (.ppt)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ODC
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Office Data Connection
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ODF
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
OpenDocument Formula
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ODG
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
OpenDocument Graphics
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ODI
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
OpenDocument Image
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ODP
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
OpenDocument Presentation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel 4.0 Macro sheet
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XLT
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Excel Template
{% /cell %}
{% /row %}
{% /table %}

## Encrypted Documents

{% callout title="Note" %}
Encrypted documents are handled with special processing to extract and analyze content while maintaining security protocols.
{% /callout %}

## Executable Files

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PE (EXE/DLL)
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes, limited" type="success" /%}\*\*
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
PE unpacking \& re-analysis. Beta PE emulator available for 32-bit EXE files.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PE (dotnet\_pe)
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes, limited" type="success" /%}\*\*
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
PE.NET decompilation \& re-analysis. (Not emulated)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PE (other)
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes, limited" type="success" /%}\*\*
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Other specific PE types (SFX, Golang, Rust, etc.)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
APK
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Android
{% /cell %}
{% cell %}
Android Application Package
{% /cell %}
{% /row %}
{% row %}
{% cell %}
CPL
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Control Panel Extension
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ELF
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Unix
{% /cell %}
{% cell %}
Executable and Linkable Format
{% /cell %}
{% /row %}
{% row %}
{% cell %}
LNK
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Windows Shortcut
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MSI
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Windows Installer Package
{% /cell %}
{% /row %}
{% /table %}

## Image Files

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
BMP
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Hidden data checks
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DWG
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
VBA macro extraction
{% /cell %}
{% /row %}
{% row %}
{% cell %}
JPG
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Hidden data checks
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PNG
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Hidden data checks
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SVG
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes, limited" type="success" /%}\*
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Scalable Vector Graphics
{% /cell %}
{% /row %}
{% /table %}

## Disk Image Files

{% callout title="Note" %}
Disk image files are analyzed for contained file systems and embedded content.
{% /callout %}

## Media Files

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ASF
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Windows Media Video
{% /cell %}
{% /row %}
{% row %}
{% cell %}
WMV
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Metadata analysis
{% /cell %}
{% /row %}
{% /table %}

## Other

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
CHM
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Compiled HTML Help
{% /cell %}
{% /row %}
{% row %}
{% cell %}
CLASS (java-bytecode)
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Limited support. Yet just for a few specific malware config extraction
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Java
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Java Decompilation \& re-analysis
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MHT, MHTML
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Web Archive
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MSC
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft Management Console
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MSO
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Microsoft office active/macro object files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
OLE
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Object Linking and Embedding
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Pickle
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Python Pickle
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SCT
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Windows Scriptlet
{% /cell %}
{% /row %}
{% /table %}

## Adobe Files

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PDF
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes, limited" type="success" /%}\*
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Portable Document Format
{% /cell %}
{% /row %}
{% /table %}

## Text Files

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
HTML
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes, limited" type="success" /%}\*
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Hypertext Markup Language
{% /cell %}
{% /row %}
{% row %}
{% cell %}
TXT
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Plain Text
{% /cell %}
{% /row %}
{% row %}
{% cell %}
HTA
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
HTML Application
{% /cell %}
{% /row %}
{% row %}
{% cell %}
WSF
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Windows Script File
{% /cell %}
{% /row %}
{% row %}
{% cell %}
BAT
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Batch Script
{% /cell %}
{% /row %}
{% row %}
{% cell %}
JScript
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Microsoft's implementation of JavaScript
{% /cell %}
{% /row %}
{% row %}
{% cell %}
JSE
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
JScript Encoded
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PS1
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
PowerShell
{% /cell %}
{% /row %}
{% row %}
{% cell %}
VBScript
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Visual Basic Script
{% /cell %}
{% /row %}
{% row %}
{% cell %}
CSV
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Comma-Separated Values
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ICS
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
iCalendar
{% /cell %}
{% /row %}
{% row %}
{% cell %}
JS
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
JavaScript
{% /cell %}
{% /row %}
{% row %}
{% cell %}
JSON
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
JavaScript Object Notation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PY
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Python
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SH
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Unix
{% /cell %}
{% cell %}
Shell script
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XML
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Multi-OS
{% /cell %}
{% cell %}
Extensible Markup Language
{% /cell %}
{% /row %}
{% /table %}

## Email Files

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[121] %}
File Type
{% /cell %}
{% cell header=true colwidth=[130] %}
**Static Analysis**
{% /cell %}
{% cell header=true colwidth=[145] %}
**Dynamic Analysis**
{% /cell %}
{% cell header=true colwidth=[102] %}
OS
{% /cell %}
{% cell header=true %}
**Comment**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
EML
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes, limited" type="success" /%}\*
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Electronic Mail
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MBOX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Mailbox Format
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MSG
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
Outlook Message
{% /cell %}
{% /row %}
{% row %}
{% cell %}
RFC822
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
Windows
{% /cell %}
{% cell %}
RFC822 Email Format
{% /cell %}
{% /row %}
{% /table %}

## Archive Files

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[119] %}
Supported Archive Types
{% /cell %}
{% cell header=true colwidth=[130] %}
Archives extraction
{% /cell %}
{% cell header=true colwidth=[128] %}
Type-specific analysis
{% /cell %}
{% cell header=true %}
Comment
{% /cell %}
{% /row %}
{% row %}
{% cell %}
7Z
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ACE
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="custom" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
BZIP2/BZ2
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
CAB
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
Requires version 1.6.1 or later
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DEB
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}\*
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
GTAR
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
GZIP
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
LZIP
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ISO
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
PKG (NodeJS)
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
RAR
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SFX (PEEXE)
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
TBZ2
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="custom" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
TAR
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
TGZ
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
TXZ
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MSU
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
VHD
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
Requires 1.6.3 or later
{% /cell %}
{% /row %}
{% row %}
{% cell %}
WHL
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
XPI
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ZIP
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ZIPX
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="N/A" type="primary" /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% /table %}

*\* The most relevant files are identified and extracted, along with the file list. But not all of the contained files.*

---

*Note: The MIME type is detected automatically regardless of the provided file suffix.*

*\* if the file contains objects that have dedicated dynamic analysis support (e.g. JavaScript in PDF)*

*\*\* Read more about [supported unpackers](https://docs.opswat.com/filescan/datasheet/supported-packers-for-unpacking)* and full overview of executable capabilities available [here](https://docs.opswat.com/filescan/datasheet/executable-analysis)

#### Maximum File Size:

The maximum file size is 2000 MB.

*Note: All file size limits can be configured.*

#### Maximum parallel uploads

Maximum parallel uploads - as part of an archive - from v2.*.*:

- 1000 executables,
- 10 documents,
- 10 other
