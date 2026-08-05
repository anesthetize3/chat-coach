---
type: page
title: YARA Rules
listed: true
description: 
index_title: YARA Rules
hidden: false
keywords: 
tags: 
---

The Sandbox engine contains a set of YARA rules in the `/home/sandbox/sandbox/transform/yara/rules` folder.

If Sandbox is connected to the Internet, these built-in YARA rules are periodically updated from a GitHub repository ([https://github.com/filescanio/fsYara](https://github.com/filescanio/fsYara)) maintained by OPSWAT Malware Analysts. After an update, the engine recompiles the `master_file.yarc` file that contains all rules in a compiled form. This is crucial for efficient YARA matching.

It is also possible to add custom YARA rules as `.yar` files in the `/home/sandbox/sandbox/transform/yara/rules/custom` folder, but it is necessary to modify the YARA update configuration to always generate `master_file.yarc` on Sandbox startup:

**Step #1 - Open** `/home/sandbox/sandbox/transform.cfg` **in a text editor**

**Step #2 - Modify the configuration by adding the following property:**

{% code %}
```bash {% title="transform.cfg" %}
runYaraUpdateOnStartup=true
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
runYaraUpdateOnStartup
{% /cell %}
{% cell %}
false
{% /cell %}
{% cell %}
Main switch to enable / disable YARA updates on Sandbox startup
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% /table %}

## Adding custom YARA rules

After this change, custom `.yar` files can be copied to the `/home/sandbox/sandbox/transform/yara/rules/custom` folder, and these YARA rules will be automatically loaded by the Sandbox engine.

After adding or modifying a custom rule, please always **restart** the `sandbox` service!

{% callout type="warning" title="Warning" %}
All custom changes made in the `/home/sandbox/sandbox/transform/yara/rules` folder **will be lost** during a Sandbox installation!

If you add any custom YARA rules here, please remember to save them and **restore them after upgrading Sandbox!**
{% /callout %}

## Additional Community YARA rules

If the `Sandbox_UseCommunityYaraRules` option is set to `true` in the `install.cfg` file (see [Installation Options](../../installation/quick-installation/installation-options.md)), then the Sandbox installer will clone the following GitHub repositories containing the latest YARA rules provided by the Malware Analysis community (these repositories are not controlled by OPSWAT):

{% table layout="auto" %}
{% row %}
{% cell header=true %}
List of Community YARA Repositories
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[https://github.com/Yara-Rules/rules](https://github.com/Yara-Rules/rules)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[https://github.com/Neo23x0/signature-base](https://github.com/Neo23x0/signature-base)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[https://github.com/advanced-threat-research/Yara-Rules](https://github.com/advanced-threat-research/Yara-Rules)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[https://github.com/StrangerealIntel/DailyIOC](https://github.com/StrangerealIntel/DailyIOC)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[https://github.com/AlienVault-Labs/AlienVaultLabs](https://github.com/AlienVault-Labs/AlienVaultLabs)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[https://github.com/ditekshen/detection](https://github.com/ditekshen/detection)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
[https://github.com/reversinglabs/reversinglabs-yara-rules](https://github.com/reversinglabs/reversinglabs-yara-rules)
{% /cell %}
{% /row %}
{% /table %}
