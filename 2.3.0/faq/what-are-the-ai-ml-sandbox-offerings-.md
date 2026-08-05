---
type: page
title: What are the AI/ML Sandbox offerings?
listed: false
description: 
index_title: What are the AI/ML Sandbox offerings?
hidden: true
keywords: 
tags: 
---

## Introduction

The AI/ML Sandbox offerings enhance threat detection and analysis through a suite of advanced machine learning technologies integrated into the sandbox environment. These solutions are designed to uncover sophisticated threats, including zero-day malware, phishing sites, and malicious URLs, which often evade traditional defenses.

## AI/ML features:

**Similarity Search**: Similarity Search leverages advanced feature extraction techniques to identify and correlate unknown threats with known malware families. By analyzing behavioral patterns, code structures, and static attributes, our machine learning models detect even evasive or zero-day threats that traditional signature-based methods may miss.

More Info: [Similarity Search - Introduction](../datasheet/advanced-reputation/similarity-search.md)

**Offline URL model:** The offline URL detection ML model enhances security by effectively identifying suspicious URLs

More Info: [Offline URL Reputation Overview](../datasheet/url-analysis/offline-url-reputation.md)

**ML Brand Detection**: Web Threat Detection Model enhances security by analyzing a site’s structure, behavior, and content to label pages as malicious, based on sandbox verdicts. After gathering data, it makes predictions in milliseconds. It works in standalone environments but not in air-gapped systems.

More Info: [ML Brand Detection](../datasheet/url-analysis/url-capabilities.md)

**Web-threat**: Utilizing full Chrome-based webpage rendering combined with machine learning-driven image analysis, the platform detects phishing attempts by scrutinizing visuals for impersonations of over 338 major brands.

More Info: [Web Threat Detection Overview](../datasheet/url-analysis/webthreat.md)

**ChatGPT integration**: The primary aim of this executive summary is to make threat analysis easier to understand by highlighting the most significant aspects of the malware report.

More Info: [Chat GPT](../configuration/communication-and-integration/chat-gpt.md)

## Sandbox offerings

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[79] %}
AI/ML services
{% /cell %}
{% cell header=true colwidth=[3] %}
MetaDefender Sandbox (Online)
{% /cell %}
{% cell header=true colwidth=[2] %}
Adaptive Sandbox for MD Cloud
{% /cell %}
{% cell header=true colwidth=[2] %}
MetaDefender Sandbox (Offline)
{% /cell %}
{% cell header=true colwidth=[540] %}
Adaptive Sandbox for MD Core (Offline / Online)
{% /cell %}
{% cell header=true %}
Enabled by default
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Similarity Search**
{% /cell %}
{% cell %}
{% badge text="Yes" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Offline URL model**
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**ML Brand Detection**
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Web-threat**
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**ChatGPT integration**
{% /cell %}
{% cell %}
{% badge text="Yes" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="No" type="error" /%}
{% /cell %}
{% /row %}
{% /table %}
