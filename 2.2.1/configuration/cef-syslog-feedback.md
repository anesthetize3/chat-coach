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
# Syslog header config
syslogHeaderPrivalFacility=16
syslogHeaderPrivalSeverity=6
syslogHeaderHost=
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
{% row %}
{% cell %}
syslogHeaderPrivalFacility
{% /cell %}
{% cell %}
16
{% /cell %}
{% cell %}
Facility value used in the syslog header
{% /cell %}
{% /row %}
{% row %}
{% cell %}
syslogHeaderPrivalSeverity
{% /cell %}
{% cell %}
6
{% /cell %}
{% cell %}
Severity value used in the syslog header
{% /cell %}
{% /row %}
{% row %}
{% cell %}
syslogHeaderHost
{% /cell %}
{% cell %}
- {% p /%}
{% /cell %}
{% cell %}
The hostname value is used in the syslog header. If not configured, the application will try to detect and use the local hostname.
{% /cell %}
{% /row %}
{% /table %}

{% callout type="warning" title="syslogHeaderHost" %}
Since the broker is running in a dockerized environment, the detected hostname might not be useful, therefore it is possible to set a user defined hostname which will be used in the syslog header.
{% /callout %}

## Example CEF syslog message:

```plaintext {% title="message" %}
<134>1 2024-09-05T08:04:24.410Z hostname - - - - CEF:0|OPSWAT Inc.|broker|1.1.0-53dd79f|transform-file|OPSWAT Sandbox scan result|6|cs1Label=Task ID cs1=6c77d761-6958-4e2a-aa7c-88de393c4cf1 cs2Label=SHA256 cs2=6c297c89d32d7fb5c6d10b1da2612c9557a5126715c4a78690d5d8067488f5f2 cs3Label=Media Type cs3=application/x-ms-installer cs4Label=Date cs4=2024-09-05 10:17+0200249 cs5Label=All Tags cs5=expand,fingerprint,lolbin,msi cs6Label=All Signal Group IDs cs6=H061,S007,R007,H071,PE000,SIGG038,I001
```

## Scan verdict and CEF severity mapping

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Scan verdict
{% /cell %}
{% cell header=true %}
CEF severity
{% /cell %}
{% /row %}
{% row %}
{% cell %}
BENIGN
{% /cell %}
{% cell %}
0
{% /cell %}
{% /row %}
{% row %}
{% cell %}
NO\_THREAT
{% /cell %}
{% cell %}
1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SUSPICIOUS
{% /cell %}
{% cell %}
3
{% /cell %}
{% /row %}
{% row %}
{% cell %}
LIKELY\_MALICIOUS
{% /cell %}
{% cell %}
6
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MALICIOUS
{% /cell %}
{% cell %}
9
{% /cell %}
{% /row %}
{% row %}
{% cell %}
UNKNOWN
{% /cell %}
{% cell %}
0
{% /cell %}
{% /row %}
{% /table %}

## Test syslog integration

The syslog integration can be tested with the help of a commonly used syslog server like [syslog-ng](https://syslog-ng.github.io/). You can find an example syslog-ng configuration file below, accepting messages on tcp or udp and storing them to a local file.

{% code %}
```clike {% title="Example syslog-ng test configuration" %}
@version: 3.35

source s_net {
  syslog(
    ip("0.0.0.0") port(514) transport("udp")
  );

  syslog(
    ip("0.0.0.0") port(514) transport("tcp")
  );
};

destination d_file {
  file("/syslog");
};

log {source(s_net); destination(d_file); };
```
{% /code %}
