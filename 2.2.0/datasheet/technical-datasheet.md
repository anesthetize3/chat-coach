---
type: page
title: Technical Datasheet
listed: true
description: 
index_title: Technical Datasheet
hidden: false
keywords: 
tags: 
---

The purpose of this page is to provide Question/Responses to technical questions that are frequently asked.

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Category
{% /cell %}
{% cell header=true colwidth=[182] %}
Feature
{% /cell %}
{% cell header=true %}
MetaDefender Sandbox Compliance
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Requirements
{% /cell %}
{% cell %}
Hardware Requirements
{% /cell %}
{% cell %}
Minimum requirements (on premise):

- **Ubuntu Server 22.04** or **Red Hat Enterprise Linux 9.5**
- 8 vCPUs (better: 16)
- 32 GB RAM
- 256 GB SSD (better: 512 GB)\*

*Note: if the customer requires more than 25000 scans/day, a custom multi-server setup is necessary and needs to be scoped out with the engineering team.*

Due to the low resource requirements and cloud-native capability, MetaDefender Sandbox does not require nested VMs and can be deployed and operated with its proprietary emulation technology running directly on the host system.

More information available: [Throughput / Hardware Requirements](../installation/technical-requirements.md#throughput--hardware-requirements)

- Disc space recommendation is assuming default retention settings and an average file size is assumed to be in the single digit MB range. If very large files are sent at large quantities, total disc size has to be much larger or retention settings more strict.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Minimum Cloud Requirements
{% /cell %}
{% cell %}
AWS EC2 instances:

- 5000 scans/day: `r6a.xlarge`
- 10000 scans/day: `m6a.2xlarge`
- 25000 scans/day: `c6a.4xlarge`
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Performance
{% /cell %}
{% cell %}
System performance
{% /cell %}
{% cell %}
25000 scans/day is the peak performance for a single-server deployment. This translates to roughly **\~1000 scans/hour**. A higher throughput is possible, but will require a multi-server setup.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Average Processing Time
{% /cell %}
{% cell %}
**The average processing time per scan is \~20 seconds.** On production, it is currently \~12 seconds/scan, but this varies widely based on the input mix.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Supported file types
{% /cell %}
{% cell %}
Side-by-side comparison including dynamic analysis available: [Supported File Types](supported-file-types.md).

Files:

APK, ASF, BAT, DLL, DOC, DOCM, DOCX, DOT, DOTM, DOTX, ELF, EML, HTA, HTML, HWP, Java, JScript, JSE, LNK, MBOX, OLE, PDF, PE, PE, POT, POTM, POTX, Powershell, PPAM, PPSX, PPT, PPTM, PPTX, PUB, RFC822, RTF, SCT, SVG, VBScript, WSF, XLS, XLSM, XLSX, XLTM, XLTX..etc.

[Click here to see all the supported file types](https://docs.opswat.com/filescan/datasheet/supported-file-types)

*Note: the maximum (default) file size is 100MB per upload, but can be configured (on premise only).*

*Note #2: the MIME type is detected automatically regardless of the provided file suffix.*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Archives Supported
{% /cell %}
{% cell %}
7Z, ACE, BZIP2, CAB, GTAR, GZIP, LZIP, ISO, RAR, TAR, ZIP

More information available: [Supported File Types](supported-file-types.md).
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Maximum File Size
{% /cell %}
{% cell %}
Default: 2000MB

Note: all file size limits can be configured
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Maximum parallel uploads (part of an archive)
{% /cell %}
{% cell %}
Default: 1000 executables, 10 documents, 10 other
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Integrations
{% /cell %}
{% cell %}
API
{% /cell %}
{% cell %}
- OpenAPI specification, including a Swagger documentation available via the webservice
- Python pip package as a convenience tool that wraps around the API
- Includes full system management (administration), as well as file/URL scanning and threat graph search
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
YARA
{% /cell %}
{% cell %}
- Automated, repeated download of a configurable list of GitHub repositories. All downloaded YARA rules are filtered and compiled to a performant .yarc file, as well as applied to the input file and all extracted/downloaded child objects.
- On premise: ability to add custom YARA rules
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
SIEM
{% /cell %}
{% cell %}
- On premise: a CEF (common event format) syslog feedback can be configured to integrate with a SIEM system (e.g. IBM QRadar, Splunk)
- Web UX / API: includes a “query generator” that will, for selected IOCs, generate a query that can be used to pivot to e.g. Crowdstrike’s platform and continue threat hunting
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
MITRE
{% /cell %}
{% cell %}
All proprietary generic threat indicators are mapped to the appropriate MITRE ATT\&CK tactic and technique (if applicable)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
E-Mail
{% /cell %}
{% cell %}
- On premise: the backend “broker” can be configured to ingest E-Mail files from a postfix server
- Webservice: we have a full “IMAP” integration that can be polled and ingest any inbound E-Mail, including E-Mail management (e.g. the option to delete the ingested E-Mail)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
OSINT
{% /cell %}
{% cell %}
- VirusTotal
- ClamAV
- YARA (see above)
- OPSWAT Reputation Service
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
MD Core
{% /cell %}
{% cell %}
The sandbox engine is also available as part of an integration with MD Core. More details: [MD Core Adaptive Sandbox Engine Features](../integrations/md-core-engine.md)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
SOAR
{% /cell %}
{% cell %}
- Palo Alto - Cortex XSOAR
- Splunk SOAR
- Assemblyline 4

Full list: [https://docs.opswat.com/filescan/integrations](https://docs.opswat.com/filescan/integrations)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Reporting
{% /cell %}
{% cell %}
Report Formats
{% /cell %}
{% cell %}
The following report formats are available and exportable via the UX or API:

- Single-file HTML
- Single-file PDF
- MISP
- STIX (2.1)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Threat Intelligence
{% /cell %}
{% cell %}
Search
{% /cell %}
{% cell %}
MetaDefender Sandbox includes a threat graph and extensive searching capabilities (e.g. a prevalence search to identify other reports that shared the same IOCs within a specified time frame).

Example: [Advanced Search / Examples](../adminguide/advanced-search.md#examples)

As of MetaDefender Sandbox 1.8.0, a new Threat Intelligence Similarity search feature is available, which enables detection of unknown threats. Read more [here](https://www.opswat.com/blog/introducing-opswat-threat-intelligence-similarity-search).
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Storage
{% /cell %}
{% cell %}
On premise: it is stored locally within the on premise instance and no data is shared with third-parties.

Cloud: it is stored locally within the managed instance and no data is shared with third-parties.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Deployment and Maintenance
{% /cell %}
{% cell %}
Deployment
{% /cell %}
{% cell %}
The deployment is fully automated and takes about 25-30 minutes depending on the internet connectivity. See more in the [Installation](../installation/installation-introduction.md).

Note: the solution may be installed and operated in an air-gapped environment. See [Offline Installation](../installation/offline-installation.md)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
CIS Compliance
{% /cell %}
{% cell %}
MetaDefender Sandbox can be installed on a hardened Linux system that complies with the Level 1 profile of the[ CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Retention
{% /cell %}
{% cell %}
Administrators can configure a retention period (in days).  After the retention period is over for a report, all the files which are stored in relation to that report will be deleted. It is also possible to configure if the report itself should be deleted from the system. By default, the retention period is set to 365 days and report deletion is turned off.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Capability
{% /cell %}
{% cell %}
Zero-Day / Unknown Malware Detection
{% /cell %}
{% cell %}
Due to the “adaptive dynamic analysis” technology, which can manipulate the control flow to always satisfy environment/conditional checks (e.g. geofencing, anti-analysis), MetaDefender Sandbox excels at detecting zero-day malware and extracting threat intelligence data (e.g. IOCs). Many great examples are also tweeted on the official Filescan [Twitter account](https://twitter.com/filescan_itsec).
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Memory Dump Analysis
{% /cell %}
{% cell %}
Yes, we support memory dump analysis. However, only for the initial process. For PEs, we support the following unpackers:

- [**ASPack**](http://www.aspack.com/): Advanced commercial packer with a high compression ratio
- [**FSG**](https://www.aldeid.com/wiki/Category:Digital-Forensics/Computer-Forensics/Anti-Reverse-Engineering/Packers/FSG): Freeware, fast to unpack
- [**MEW**](https://www.softpedia.com/get/Programming/Packers-Crypters-Protectors/MEW-SE.shtml): Specifically designed for small binaries
- [**MPRESS**](http://www.matcode.com/mpress.htm): Free, more complex packer
- [**PEtite**](https://www.un4seen.com/petite/): Freeware packer, similar to ASPack
- [**UPX**](https://github.com/upx/upx): Cross-platform, open source packer
- **YZPack**

The unpacked payload is then disassembled and all code branches are inspected for API call chains and threat indicators.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Sleep Reduction / Anti-Evasion
{% /cell %}
{% cell %}
Both supported. The sleep reduction is implemented within the dynamic analysis modules. Anti-evasion is implemented using adaptive dynamic analysis (see above).
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Licensing
{% /cell %}
{% cell %}
OEM
{% /cell %}
{% cell %}
Yes, we support OEM and custom logos. Please get in touch with [Hamid Karimi](hamid.karimi@opswat.com) his team for details.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Enterprise
{% /cell %}
{% cell %}
All MetaDefender Sandbox SKUs are already available and can be quoted via SFDC.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Evaluation
{% /cell %}
{% cell %}
POC
{% /cell %}
{% cell %}
Cloud (public): [filescan.io](https://www.filescan.io/scan)

[On premise](../installation/installation-introduction.md)

POC Guide: [API Workflow Guide](api-workflow-guide.md)
{% /cell %}
{% /row %}
{% /table %}
