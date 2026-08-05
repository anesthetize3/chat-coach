---
type: page
title: File / Folder Structure
listed: true
description: 
index_title: File / Folder Structure
hidden: false
keywords: 
tags: 
---

In general, any option change should be implemented by copying and placing a modified version of the option into the xxx.properties.custom file. The reason is that only those changes, which are present in the .custom files will be persisted beyond the automated upgrade process. Folders/files relevant to the user are highlighted in yellow, while the other descriptions are provided for informational purposes only.

{% html %}
<ul>
  <li><b>conf/apikeys.properties[.custom]</b></li>
  This file contains the default API auth level configuration (i.e. it specifies the minimum auth level required to utilize
certain API endpoints, such as “scan”, “task”, etc.). The auth system can be toggled using the "enableWebserviceAuthSystem" option. 
  <li><b>conf/blacklist.properties[.custom]</b></li>
  This file contains a configurable list of offline and online sources (e.g. badips, blocklist, darklist) that specify
known malicious IP addresses. It is configurable and the refresh rate can be specified as well. The downloaded
blacklist, cache and local files are stored in the "external" folder. 
  <li><b>conf/transform.properties[.custom]</b></li>
  This file contains most of the configuration options for the transform processor node. For example, proxy settings, where and how are temporary files / results stored, what integrations are enabled (e.g. YARA or Virus Total
lookups) or which features are applied.
  <li><b>conf/fslog.properties</b></li>
  This is where the logging level is specified. Please configure the log4j.category.fsLogger property value to either
ALL, TRACE, DEBUG, INFO, WARN or ERROR.
  <li><b>consumers</b></li>
  This is where a group of python scripts reside, which can consume reporting data and generate informational
signals of different severity levels. These "signals" are often referred to as behavior indicators / signatures by
different security vendors. The term "signal" is used to underline the fact that a lot of reporting contains much
"noise" (redundant information) of which the relevant signals need to be extracted. The exact procedure of
modifying/creating one’s own consumers is not published. Please get in touch with support for more information
or request an additional implementation. 
  <li><b>external</b></li>
  This folder has a variety of definitions (e.g. a list of UUIDs, MITRE techniques/tactics or local whitelists/blacklists). These files are actively maintained, and new versions are provided with each update.
  <li><b>lib</b></li>
  This folder contains a variety of third-party libraries that are used by the processor node. Do not modify this
folder.
  <li><b>parser</b></li>
  This folder contains a variety of external scripts / integrations that are used by the processor node. Do not modify
this folder. 
  <li><b>thirdparty</b></li>
  This folder contains a variety of third-party software not relevant to the core functionality. Do not modify this
folder. 
  <li><b>Yara</b></li>
  This folder contains a variety of third party and local YARA rules, which are compiled to a master index file and
used against the input file and extracted artifacts. Do not modify this folder. 
</ul>
{% /html %}
