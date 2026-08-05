---
type: page
title: Installation Options
listed: true
description: 
index_title: Installation Options
hidden: false
keywords: 
tags: 
---

Before starting the installation process, you can modify certain installation options in the `install.cfg` file that is located in the same folder as `install.sh`.

{% callout type="warning" title="Warning" %}
The **default installation options are perfectly suitable** for most use cases, so it is not recommended to change these values unless you have a special use case.
{% /callout %}

**Step #1 - Open** `install.cfg` **in a text editor**

{% callout type="warning" title="Warning" %}
For **upgrade installations**, the installation options should be changed in `/home/sandbox/sandbox/install.cfg` (or in the custom Sandbox\_Directory that you configured previously).
{% /callout %}

**Step #2 - Change the installation options by modifying the following properties:**

{% code %}
```bash {% title="install.cfg" %}
Sandbox_User="sandbox"
Sandbox_Directory="/home/sandbox/sandbox"

Sandbox_ConfigureFirewall=true
Sandbox_OverwriteDockerDaemonJson=true
Sandbox_UseCommunityYaraRules=false

SandboxTransform_Install=true
SandboxTransform_APIKeySecret=

SandboxBroker_Install=true
SandboxBroker_APIKeySecret=

SandboxWebservice_Install=true
SandboxWebservice_Engine_Host=
SandboxWebservice_Engine_Secret=
```
{% /code %}

**Step #3 - Save the modified file and start the installation process**

## Property details

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[285] %}
Property Name
{% /cell %}
{% cell header=true colwidth=[137] %}
Default Value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sandbox\_User
{% /cell %}
{% cell %}
sandbox
{% /cell %}
{% cell %}
Defines the user that will run the Sandbox service. This user will be created automatically by the installer if it does not exist. For security reasons, this user should not have a password or sudo access!
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sandbox\_Directory
{% /cell %}
{% cell %}
/home/sandbox/sandbox
{% /cell %}
{% cell %}
The directory where Sandbox will be installed. It must be within the home directory of the Sandbox\_User.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sandbox\_ConfigureFirewall
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
If set to true, the installer configures the necessary firewall rules using iptables-persistent. Most importantly, it opens port 443.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sandbox\_OverwriteDockerDaemonJson
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
If set to true, the installer overwrites the existing /etc/docker/daemon.json configuration file. Set this to false if you have any custom modifications in that file.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sandbox\_UseCommunityYaraRules
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
If set to true, the installer will clone GitHub repositories containing the latest YARA rules provided by the Malware Analysis community (these repositories are not controlled by OPSWAT). More details at [YARA Rules](../../configuration/scan/yara-rules.md).
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SandboxTransform\_Install
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
If set to true, the "transform" component of Sandbox will be installed.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SandboxTransform\_APIKeySecret
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Specifies the internal API key used by transform. If left blank, a random API key will be generated.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SandboxBroker\_Install
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
If set to true, the "broker" component of Sandbox will be installed.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SandboxBroker\_APIKeySecret
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Specifies the internal API key used by broker. If left blank, a random API key will be generated.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SandboxWebservice\_Install
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
If set to true, the "webservice" component of Sandbox will be installed.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SandboxWebservice\_Engine\_Host
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Specifies the address where the webservice can connect to the broker. If left blank, it will be automatically set to "broker".
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SandboxWebservice\_Engine\_Secret
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Specifies the internal API key used by webservice to connect to broker. If left blank, it will be set to SandboxBroker\_APIKeySecret.
{% /cell %}
{% /row %}
{% /table %}
