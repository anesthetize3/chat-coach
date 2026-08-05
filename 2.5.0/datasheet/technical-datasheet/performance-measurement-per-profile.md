---
type: page
title: Performance Measurement Per Profile
listed: true
description: 
index_title: Performance Measurement Per Profile
hidden: true
keywords: 
tags: 
---

This page provides an in-depth overview of the Standalone Throughput feature, including configuration settings and performance profiling for a one-hour duration. The goal is to help users optimize system throughput by understanding key configuration parameters and how different profiles impact performance over time. Whether you are troubleshooting or tuning your system, this guide offers valuable insights to maximize efficiency and streamline operations.

## Configuration

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[186] %}
{% p /%}
{% /cell %}
{% cell header=true colwidth=[186] %}
CPU
{% /cell %}
{% cell header=true colwidth=[179] %}
RAM
{% /cell %}
{% cell header=true %}
Parallel Count
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Config 1**
{% /cell %}
{% cell %}
8
{% /cell %}
{% cell %}
32
{% /cell %}
{% cell %}
5
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Config 2**
{% /cell %}
{% cell %}
16
{% /cell %}
{% cell %}
64
{% /cell %}
{% cell %}
10
{% /cell %}
{% /row %}
{% /table %}

## Throughput Results: Profiles / Filetype

This section presents throughput results for different profiles and file types, helping users understand how each configuration affects performance. It's key for optimizing system settings based on specific data handling needs.

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[152] %}
Version
{% /cell %}
{% cell header=true colwidth=[145] %}
Sample type
{% /cell %}
{% cell header=true colwidth=[178] %}
Config
{% /cell %}
{% cell header=true %}
Speed profile
{% /cell %}
{% cell header=true %}
Analysis profile
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Mixed
{% /cell %}
{% cell %}
Conifg 1
{% /cell %}
{% cell %}
1525
{% /cell %}
{% cell %}
637
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Mixed
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
2143
{% /cell %}
{% cell %}
997
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Executable
{% /cell %}
{% cell %}
Conifg 1
{% /cell %}
{% cell %}
2700
{% /cell %}
{% cell %}
904
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Executable
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
4065
{% /cell %}
{% cell %}
2036
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Media
{% /cell %}
{% cell %}
Config 1
{% /cell %}
{% cell %}
1853
{% /cell %}
{% cell %}
1857
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Media
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
3816
{% /cell %}
{% cell %}
3779
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Offices
{% /cell %}
{% cell %}
Config 1
{% /cell %}
{% cell %}
634
{% /cell %}
{% cell %}
446
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Offices
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
1189
{% /cell %}
{% cell %}
773
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Text
{% /cell %}
{% cell %}
Config 1
{% /cell %}
{% cell %}
986
{% /cell %}
{% cell %}
538
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Text
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
1569
{% /cell %}
{% cell %}
633
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Images
{% /cell %}
{% cell %}
Config 1
{% /cell %}
{% cell %}
1922
{% /cell %}
{% cell %}
1902
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Images
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
4658
{% /cell %}
{% cell %}
4544
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Adobe
{% /cell %}
{% cell %}
Config 1
{% /cell %}
{% cell %}
1124
{% /cell %}
{% cell %}
509
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v2.2.0 Standalone
{% /cell %}
{% cell %}
Adobe
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
2541
{% /cell %}
{% cell %}
1053
{% /cell %}
{% /row %}
{% /table %}

## Throughput Results: Profiles / Active content

This section compares throughput results between scanning samples with active content and without active content, highlighting the impact of chosen profile on performance. It helps users optimize system settings based on profile activity.

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[242] %}
Version
{% /cell %}
{% cell header=true %}
Sample Type
{% /cell %}
{% cell header=true %}
Config
{% /cell %}
{% cell header=true %}
Speed profile
{% /cell %}
{% cell header=true %}
Analysis profile
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**v2.2.0-Standalone**
{% /cell %}
{% cell %}
Active content
{% /cell %}
{% cell %}
Config 1
{% /cell %}
{% cell %}
664
{% /cell %}
{% cell %}
351
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**v2.2.0-Standalone**
{% /cell %}
{% cell %}
Active content
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
1353
{% /cell %}
{% cell %}
641
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**v2.2.0-Standalone**
{% /cell %}
{% cell %}
Not active content
{% /cell %}
{% cell %}
Config 1
{% /cell %}
{% cell %}
1004
{% /cell %}
{% cell %}
988
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**v2.2.0-Standalone**
{% /cell %}
{% cell %}
Not active content
{% /cell %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
1769
{% /cell %}
{% cell %}
1725
{% /cell %}
{% /row %}
{% /table %}
