---
type: page
title: Domains Contacted During Installation & Operation
listed: true
description: 
index_title: Domains Contacted During Installation & Operation
hidden: false
keywords: 
tags: 
---

During the installation and operation of **MetaDefender Aether** (previously known as MetaDefender Sandbox), the following domains will be contacted. Please note that this may change over time.

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[211] %}
Domains
{% /cell %}
{% cell header=true colwidth=[218] %}
Purpose
{% /cell %}
{% cell header=true colwidth=[97] %}
Usage Type
{% /cell %}
{% cell header=true %}
MetaDefender Aether Layer
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[api.metadefender.com](api.metadefender.com)
{% /cell %}
{% cell %}
MetaDefender Cloud Reputation API
{% /cell %}
{% cell %}
Operation
{% /cell %}
{% cell %}
Layer 1 - Threat Reputation

Layer 4 - Threat Hunting
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[opswat.com](opswat.com)

[update.dl.opswat.com](update.dl.opswat.com)

[activation.dl.opswat.com](activation.dl.opswat.com)
{% /cell %}
{% cell %}
OPSWAT Activation Server and Update Infrastructure - Used for product activation and for downloading threat database updates
{% /cell %}
{% cell %}
Operation
{% /cell %}
{% cell %}
Layer 1 - Threat Reputation

Layer 2 - Dynamic Analysis

Layer 3 - Threat Scoring
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[my.opswat.com](my.opswat.com)
{% /cell %}
{% cell %}
MyOPSWAT Portal used for OCM Integration
{% /cell %}
{% cell %}
Operation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[api.nuget.org](api.nuget.org)

[data.mcr.microsoft.com](data.mcr.microsoft.com)

[mcr.microsoft.com](http://mcr.microsoft.com/)

[packages.microsoft.com](http://packages.microsoft.com/)

[a-0016.a-msedge.net](a-0016.a-msedge.net)
{% /cell %}
{% cell %}
Microsoft Container Registry and repository for .NET packages - Used by the Powershell emulator
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[archive.ubuntu.com](http://archive.ubuntu.com)

[deb.debian.org](http://deb.debian.org)

[debian.map.fastlydns.net](debian.map.fastlydns.net)

[security.ubuntu.com](http://security.ubuntu.com)
{% /cell %}
{% cell %}
Repositories of Ubuntu and Debian packages (can be any regional or local mirror) - Used directly for Ubuntu installations and used in Docker containers for both Ubuntu and RHEL installs
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[auth.docker.io](auth.docker.io)

[docker.io](http://docker.io)

[download.docker.com](http://download.docker.com)

[registry-1.docker.io](registry-1.docker.io)

[production.cloudflare.docker.com](production.cloudflare.docker.com)
{% /cell %}
{% cell %}
Used for Docker installation and downloading base images for Sandbox components
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[bootstrap.pypa.io](http://bootstrap.pypa.io)

[files.pythonhosted.org](files.pythonhosted.org)

[pypi.org](http://pypi.org)
{% /cell %}
{% cell %}
Python package repositories - Used when building the Docker image for the Sandbox webservice component
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[codecs.fedoraproject.org](http://codecs.fedoraproject.org)

[mirrors.fedoraproject.org](http://mirrors.fedoraproject.org)
{% /cell %}
{% cell %}
Fedora’s geographically optimized mirror server that hosts Fedora packages
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[d2h67oheeuigaw.cloudfront.net](http://d2h67oheeuigaw.cloudfront.net)

[d2lzkl7pfhq30w.cloudfront.net](http://d2lzkl7pfhq30w.cloudfront.net)

[artifact.sandbox-prod.metadefender.com](http://artifact.sandbox-prod.metadefender.com/)
{% /cell %}
{% cell %}
Used for downloading phishpedia package from [artifact.sandbox-prod.metadefender.com](artifact.sandbox-prod.metadefender.com) - Required for phishing detection ML model
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[dl-ssl.google.com](http://dl-ssl.google.com)

[dl.google.com](http://dl.google.com)
{% /cell %}
{% cell %}
Used for downloading Google Chrome - Required for URL rendering in the Sandbox transform Docker container
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[github.com](http://github.com)
{% /cell %}
{% cell %}
Used for getting YARA rules from OPSWAT fsYara repository: [https://github.com/filescanio/fsYara](https://github.com/filescanio/fsYara)
{% /cell %}
{% cell %}
Operation
{% /cell %}
{% cell %}
Layer 2 - Dynamic Analysis
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[google.com](http://google.com)

[www.google.com](http://www.google.com)
{% /cell %}
{% cell %}
Used for basic connectivity check
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[ntp.ubuntu.com](ntp.ubuntu.com)

[time-a-g.nist.gov](time-a-g.nist.gov)

[time-a.nist.gov](time-a.nist.gov)
{% /cell %}
{% cell %}
NTP and time servers
{% /cell %}
{% cell %}
Operation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[pki.goog](pki.goog)
{% /cell %}
{% cell %}
Google Public Key Infrastructure
{% /cell %}
{% cell %}
Installation Operation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[playwright.azureedge.net](playwright.azureedge.net)
{% /cell %}
{% cell %}
Used for installing playwright in the Sandbox webservice docker image
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[rhui.us-west-2.aws.ce.redhat.com](rhui.us-west-2.aws.ce.redhat.com)
{% /cell %}
{% cell %}
RHEL package repository (can be any regional or local mirror)
{% /cell %}
{% cell %}
Installation
{% /cell %}
{% cell %}
N/A
{% /cell %}
{% /row %}
{% /table %}

For convenience, the same domains are also listed here:

```plaintext {% title="Domains" %}
api.metadefender.com
opswat.com
update.dl.opswat.com
activation.dl.opswat.com
my.opswat.com
api.nuget.org
data.mcr.microsoft.com
mcr.microsoft.com 
packages.microsoft.com
a-0016.a-msedge.net
archive.ubuntu.com
deb.debian.org
debian.map.fastlydns.net
security.ubuntu.com
auth.docker.io
docker.io
download.docker.com
registry-1.docker.io
production.cloudflare.docker.com
bootstrap.pypa.io
files.pythonhosted.org
pypi.org
codecs.fedoraproject.org
mirrors.fedoraproject.org
d2h67oheeuigaw.cloudfront.net
d2lzkl7pfhq30w.cloudfront.net
artifact.sandbox-prod.metadefender.com
dl-ssl.google.com
dl.google.com
github.com
google.com
www.google.com
ntp.ubuntu.com
time-a-g.nist.gov
time-a.nist.gov
pki.goog
playwright.azureedge.net
rhui.us-west-2.aws.ce.redhat.com
```
