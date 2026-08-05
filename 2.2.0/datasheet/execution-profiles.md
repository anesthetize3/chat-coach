---
type: page
title: Execution Profiles
listed: true
description: 
index_title: Execution Profiles
hidden: false
keywords: 
tags: 
---

**Execution Profiles** allow users to control the file analysis process by selecting predefined or custom settings that influence how a file is scanned. Profiles define the depth of analysis, processing speed, and the level of detail in the generated report.

{% callout type="success" title="Pro Tip" %}
Use **Speed Profile** for bulk scanning or in automated environments to process files faster.
{% /callout %}

## Built-in Profiles

There are two built-in profiles available:

### Analysis Profile

Provides **in-depth** analysis by generating a very detailed report suitable for malware analysts. Executes all available analysis steps to provide the most comprehensive results, but usually takes longer to complete due to its thoroughness.

### Speed Profile

Optimized for **fast execution** in automated environments, focuses on higher throughput, reducing the time needed for scans. Uses early termination: the scan stops immediately once a strong verdict (malicious or benign) is determined. This profile produces  less detailed results compared to the Analysis Profile.

## Custom Profiles

Users can create custom profiles by defining their own analysis settings. This allows fine-tuning the scanning process to match specific requirements.

## Profile settings

{% callout title="Info" %}
These settings are **user-specific**: changes made by one user do not affect others.
{% /callout %}

### Creating a Custom Profile

Navigate to: **User -\> My Settings -\> Scan Profiles** and click the **Add profile** button

{% image url="https://uploads.developerhub.io/prod/XX2D/kly9jcf9zuy7scg1v8tzywozt5qdh1syqgkmoojmfmstvrvpe1fd9tx2o5sqvtg3.png" /%}

Chose a name and description for your new profile and select the desired features. Hover your mouse over the **information icons** next to each feature for more details. Optionally, select the profile as **Default** for all scans, and click the **Save** button.

{% image url="https://uploads.developerhub.io/prod/XX2D/u0stb0ul1dh75n5ssk8h0s26m2o51668y4lb9q9q9x4dfafydkulrkjlq0b4v3gi.png" /%}

### Editing or removing a Profile

Navigate to: **User -\> My Settings -\> Scan Profiles** and click the **Meatballs menu** next to the profile.

{% callout title="Info" %}
Built in profiles cannot be removed and options are not editable, only the **Default** flag can be modified.
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/7zognuhkzkprm5ki29qqz2sk2wshj404sg548y36sy90gcd1t02craxlqgs9lj25.png" /%}

## Scanning files with Profiles

Use the **File selector** on the main page and open the **Advanced Options** tab to select a profile and override the default profile selection for a new scan.

{% image url="https://uploads.developerhub.io/prod/XX2D/l5wr9wne56qtc702fts4gojzhk338f5px48h8kkz4g22apri40rmuhfspwxk6xvk.png" /%}

## Scanning a file with custom settings

Use **Custom options** on the profile selector and select the desired options. This will be applied to the current scan, only.

{% image url="https://uploads.developerhub.io/prod/XX2D/ff49qoybbpjayitalrxrl91vb8sosdwsgsl46fwsl2l48w0ed03ib3u5qudm023a.png" /%}
