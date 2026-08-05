---
type: page
title: Dynamic Analysis
listed: true
description: 
index_title: Dynamic Analysis
hidden: true
keywords: 
tags: 
---

Adaptive Sandbox dynamic analysis features

**Step #1 - Open** `/home/sandbox/sandbox/transform.cfg` **in a text editor**

**Step #2 - Modify the configuration by adding or modifying the properties on this page**

**Step #3 - Save the file and restart the** `sandbox` **service**

## Phishing Detection

{% code %}
```bash {% title="transform.cfg" %}
runAnesidoraWebForURLToFileSubmissions=true
runAnesidoraWebLookupTimeoutMs=60000
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property Name
{% /cell %}
{% cell header=true %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runAnesidoraWebForURLToFileSubmissions
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable phishing detection
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runAnesidoraWebLookupTimeoutMs
{% /cell %}
{% cell %}
1 minute
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}

## Script Emulation

Enable JScript, VBScript, HTA/MSHTA and Powershell script emulation

{% code %}
```bash
runVBADecoderForOfficeFiles=true
runVBADecoderForPdfFiles=true
runVBADecoderForScriptFiles=true
runVBADecoderForHtmlFiles=true
runVBADecoderForExtractedFiles=true
runVBADecoderForDownloadedFiles=true
anesidoraVBAPerformDeepStaticAnalysisForExtractedFiles=true
anesidoraVBAPerformDeepStaticAnalysisForExtractedFilesMax=10
anesidoraVBAPerformDeepStaticAnalysisForExtractedFilesMaxSizeInKb=1024
anesidoraVBAExecutionTimeout=90
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[471] %}
Property Name
{% /cell %}
{% cell header=true colwidth=[65] %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runVBADecoderForOfficeFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable Office file emulation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runVBADecoderForPdfFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable PDF file emulation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runVBADecoderForScriptFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable script file emulation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runVBADecoderForHtmlFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable HTML file emulation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runVBADecoderForExtractedFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Emulate extracted files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runVBADecoderForDownloadedFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Emulate downloaded files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
anesidoraVBAExecutionTimeout
{% /cell %}
{% cell %}
90 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
anesidoraVBAPerformDeepStaticAnalysisForExtractedFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Execute static analysis on extracted files detected during emulation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
anesidoraVBAPerformDeepStaticAnalysisForExtractedFilesMax
{% /cell %}
{% cell %}
10
{% /cell %}
{% cell %}
Limit: the max number of files execute static analysis on
{% /cell %}
{% /row %}
{% row %}
{% cell %}
anesidoraVBAPerformDeepStaticAnalysisForExtractedFilesMaxSizeInKb
{% /cell %}
{% cell %}
1 MB
{% /cell %}
{% cell %}
Limit: the max size of files execute static analysis on
{% /cell %}
{% /row %}
{% /table %}

## PE Emulation

Enable Portable Executable emulation

{% callout type="warning" title="Warning" %}
This is an experimental feature
{% /callout %}

{% code %}
```bash {% title="transform.cfg" %}
runPEEmulator=false
peEmuEmulatePEFiles=true
peEmuEmulateRawShellcode=true
pEEmuExecutionTimeout=90
pEEmuPerformDeepStaticAnalysisForExtractedFiles=true
pEEmuPerformDeepStaticAnalysisForExtractedFilesMax=10
pEEmuIgnoreClueTypes=SessionStarted,EmulationEnd,Exception,UnhandledAPI
pEEmuConfigFile.Unix=
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property Name
{% /cell %}
{% cell header=true %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runPEEmulator
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Main switch to enable / disable PE emulation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
peEmuEmulatePEFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable PE emulation for PE files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
peEmuEmulateRawShellcode
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable PE emulation for raw shellcode
{% /cell %}
{% /row %}
{% row %}
{% cell %}
pEEmuExecutionTimeout
{% /cell %}
{% cell %}
90 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
pEEmuPerformDeepStaticAnalysisForExtractedFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Execute emulation on extracted files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
pEEmuPerformDeepStaticAnalysisForExtractedFilesMax
{% /cell %}
{% cell %}
10
{% /cell %}
{% cell %}
Limit: max number of extracted files to emulate
{% /cell %}
{% /row %}
{% row %}
{% cell %}
pEEmuIgnoreClueTypes
{% /cell %}
{% cell %}
SessionStarted, EmulationEnd, Exception, UnhandledAPI
{% /cell %}
{% cell %}
Emulation events to be ignored by the sandbox
{% /cell %}
{% /row %}
{% row %}
{% cell %}
pEEmuConfigFile.Unix
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Use the specific config file to modify API tracing filter and other PE emulator parameters
{% /cell %}
{% /row %}
{% /table %}
