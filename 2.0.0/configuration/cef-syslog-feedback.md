---
type: page
title: CEF Syslog Feedback
listed: true
description: 
index_title: CEF Syslog Feedback
hidden: false
keywords: 
tags: 
---

The broker component can be configured to send a CEF syslog summary string to any endpoint via TCP or UDP.

The CEF syslog feedback is generated and sent to the configured endpoint when the main transform task and all its subtasks are in a final processing state.

To modify the syslog feedback configuration:

**Step #1 - Open** `/home/sandbox/sandbox/broker.cfg` **in a text editor**

**Step #2 - Add or modify the following properties (no need to overwrite default values):**

{% code %}
```json {% title="broker.cfg" %}
##############################
# CEF Syslog Feedback settings
##############################
cefSyslogEnabled=false
cefSyslogHost=
cefSyslogPort=514
cefSyslogProtocol=tcp
cefSyslogTimeoutMs=10000
cefSyslogUseSSL=false
```
{% /code %}

**Step #3 - Save the file and restart the** `sandbox` **service**

## Property details

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[276] %}
Property Name
{% /cell %}
{% cell header=true colwidth=[113] %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
cefSyslogEnabled
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Main switch to enable / disable CEF syslog feedback
{% /cell %}
{% /row %}
{% row %}
{% cell %}
cefSyslogHost
{% /cell %}
{% cell %}
- {% p /%}
{% /cell %}
{% cell %}
Host name or IP address of the log server
{% /cell %}
{% /row %}
{% row %}
{% cell %}
cefSyslogPort
{% /cell %}
{% cell %}
514
{% /cell %}
{% cell %}
Port of the log server
{% /cell %}
{% /row %}
{% row %}
{% cell %}
cefSyslogProtocol
{% /cell %}
{% cell %}
tcp
{% /cell %}
{% cell %}
Connection protocol to use: tcp or udp
{% /cell %}
{% /row %}
{% row %}
{% cell %}
cefSyslogTimeoutMs
{% /cell %}
{% cell %}
10 seconds
{% /cell %}
{% cell %}
Connection timeout used for TCP sockets
{% /cell %}
{% /row %}
{% row %}
{% cell %}
cefSyslogUseSSL
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Switch to enable / disable SSL verification for TCP sockets
{% /cell %}
{% /row %}
{% /table %}

## Example CEF syslog string:

```plaintext {% title="message" %}
CEF:0|OPSWAT Inc.|broker|1.1.0-1e895e7|transform-file| c378387344e0a552dc065de6bfa607fd26e0b5c569751c79fbf9c6f2e9 1c98079| cn1=1c281ba2-d4cd-4811-9ccc-fbf941c517b0 cn1Label=Task ID cn2=c378387344e0a552dc065de6bfa607fd26e0b5c569751c79fbf9c6f2e91c9807 cn2Label=SHA256 cn3=application/vnd.ms-word.document.macroenabled.12 cn3Label=Media Type cn4=2022-04-96 02:20+020096 cn4Label=Date cn5=antivm,macros,macros-on-open,obfuscated,powershell,docx cn5Label=All Tags cn6=EMU000,V004,S010,EMU006,S000,SIGG001,S041,V001,V000,Y000,S040 cn6Label=All Signal Group IDs
```
