---
type: page
title: Web Threat Detection Overview
listed: true
description: 
index_title: Web Threat Detection Overview
hidden: true
keywords: 
tags: 
---

MetaDefender Sandbox on-premise / standalone integrates with the following Web threat models

## Introduction

The Web Threat Detection Model enhances security by analyzing a site’s structure, behavior, and content to label pages as malicious, based on sandbox verdicts. After gathering data, it makes predictions in milliseconds. It works in standalone environments but not in air-gapped systems.

## Key Advantages Over Traditional Phishing Detection:

**More Accurate Detection**: Traditional phishing detection typically relies on URL reputation or known threat patterns, which can miss new or sophisticated attacks. This model checks multiple aspects of a site (structure, behavior, content), making it far more accurate at detecting threats.

**Real-Time Evaluation**: While traditional phishing detection often uses reputation data or blacklists, this model evaluates the site’s real-time behavior and content. This allows it to catch threats that don’t match known patterns or blacklisted URLs.

**Faster Predictions**: Predictions are made in milliseconds once the data is collected, ensuring quick threat identification compared to traditional methods, which can take longer due to live checks or scanning.

## Operations

The model performs a comprehensive analysis on the collected data after sending a URL to the sandbox, including its structure, behavior, and content, to assess its safety, then generates a probability score indicating the likelihood of the URL being a web threat.

## Report

Web threat result will be displayed under URL details tab in the scan report. Key: **ML Web Threat Model**

## Confidence mappings

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Verdict
{% /cell %}
{% cell header=true colwidth=[269] %}
Description
{% /cell %}
{% cell header=true %}
Content model edges
{% /cell %}
{% cell header=true %}
Behavior model edges
{% /cell %}
{% cell header=true %}
Structure model edges
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Benign
{% /cell %}
{% cell %}
Content and structure appear normal, with no threat indicators.
{% /cell %}
{% cell %}
0\.0 - 0.2
{% /cell %}
{% cell %}
0\.0 - 0.2
{% /cell %}
{% cell %}
0\.0 - 0.1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
No Threat
{% /cell %}
{% cell %}
Slight or minor deviations detected, but overall low risk.
{% /cell %}
{% cell %}
0\.2 – 0.35
{% /cell %}
{% cell %}
0\.2 – 0.35
{% /cell %}
{% cell %}
0\.1 – 0.2
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Unknown
{% /cell %}
{% cell %}
Ambiguous or atypical features; unable to determine threat confidently.
{% /cell %}
{% cell %}
0\.35 – 0.6
{% /cell %}
{% cell %}
0\.35 – 0.5
{% /cell %}
{% cell %}
0\.2 – 0.8
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Suspicious
{% /cell %}
{% cell %}
Moderate to strong indicators suggesting potential phishing behavior.
{% /cell %}
{% cell %}
0\.6 – 0.8
{% /cell %}
{% cell %}
0\.5 – 0.75
{% /cell %}
{% cell %}
0\.8 – 0.88
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Likely Malicious
{% /cell %}
{% cell %}
Strong resemblance to known phishing patterns. High probability of being harmful.
{% /cell %}
{% cell %}
0\.8 – 0.9
{% /cell %}
{% cell %}
0\.75 – 0.9
{% /cell %}
{% cell %}
0\.88 – 0.95
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Malicious
{% /cell %}
{% cell %}
Overwhelming match to malicious signatures. Immediate mitigation recommended.
{% /cell %}
{% cell %}
0\.9 – 1.0
{% /cell %}
{% cell %}
0\.9 – 1.0
{% /cell %}
{% cell %}
0\.95 – 1.0
{% /cell %}
{% /row %}
{% /table %}

## Available on the product

{% image url="https://uploads.developerhub.io/prod/XX2D/zvav4e1ujtp11crjzpbasoluzn5r2kkbg0hmf476dbwbvgmqad38zujkpdb801r2.png" /%}

## Configuration

Currently, it runs by default on every URL scan and triggers notifications to consumers if the likelihood prediction exceeds a threshold.
