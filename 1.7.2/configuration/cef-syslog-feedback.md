---
type: page
title: CEF Syslog Feedback
listed: true
description: 
index_title: CEF Syslog Feedback
hidden: true
keywords: 
tags: 
---

The broker component can be configured to send a CEF syslog summary string to any endpoint via TCP or UDP. Please refer to the "CEF Syslog Feedback settings" section of the broker.properties file. The CEF syslog feedback is generated and sent to the configured endpoint when the main transform task and all its subtasks are in a final processing state.

#### Example CEF syslog string:

`CEF:0|FileScan GmbH|fsBroker|1.1.0-1e895e7|transform-file| c378387344e0a552dc065de6bfa607fd26e0b5c569751c79fbf9c6f2e9 1c98079| cn1=1c281ba2-d4cd-4811-9ccc-fbf941c517b0 cn1Label=Task ID cn2=c378387344e0a552dc065de6bfa607fd26e0b5c569751c79fbf9c6f2e91c9807 cn2Label=SHA256 cn3=application/vnd.ms-word.document.macroenabled.12 cn3Label=Media Type cn4=2022-04-96 02:20+020096 cn4Label=Date cn5=antivm,macros,macros-on-open,obfuscated,powershell,docx cn5Label=All Tags cn6=EMU000,V004,S010,EMU006,S000,SIGG001,S041,V001,V000,Y000,S040 cn6Label=All Signal Group IDs`
