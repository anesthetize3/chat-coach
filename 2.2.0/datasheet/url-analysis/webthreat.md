---
type: page
title: Web Threat Detection Overview
listed: true
description: 
index_title: Web Threat Detection Overview
hidden: false
keywords: 
tags: 
---

MetaDefender Sandbox on-premise / standalone integrates Web threat models

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
{% cell header=true colwidth=[389] %}
Description
{% /cell %}
{% cell header=true %}
Web threat score - Minimum
{% /cell %}
{% cell header=true %}
Web threat score - Maximum
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Benign
{% /cell %}
{% cell %}
The page is highly unlikely to be  web threat. It shows no indicators of malicious activity.
{% /cell %}
{% cell %}
0\.0
{% /cell %}
{% cell %}
0\.2
{% /cell %}
{% /row %}
{% row %}
{% cell %}
No Threat
{% /cell %}
{% cell %}
The page shows no signs of  web threat  and appears safe, with moderate confidence.
{% /cell %}
{% cell %}
0\.2
{% /cell %}
{% cell %}
0\.35
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Unknown
{% /cell %}
{% cell %}
The model couldn’t confidently assess the page due to insufficient data or inconclusive indicators. Further investigation is needed.
{% /cell %}
{% cell %}
0\.35
{% /cell %}
{% cell %}
0\.5
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Suspicious
{% /cell %}
{% cell %}
The page exhibits some web threat signs but is not conclusively harmful. Further verification is needed.
{% /cell %}
{% cell %}
0\.5
{% /cell %}
{% cell %}
0\.75
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Likely Malicious
{% /cell %}
{% cell %}
The page shows clear signs of  web threat  but with minor uncertainty. Action is recommended.
{% /cell %}
{% cell %}
0\.75
{% /cell %}
{% cell %}
0\.9
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Malicious
{% /cell %}
{% cell %}
The page is highly likely to be  web threat  with strong indicators and minimal uncertainty. Immediate action is recommended.
{% /cell %}
{% cell %}
0\.9
{% /cell %}
{% cell %}
1\.0
{% /cell %}
{% /row %}
{% /table %}

## Available on the product

{% image url="https://uploads.developerhub.io/prod/XX2D/0vv3kzaxghvai07yk0yiyj9513pmn6h1tw7qi0dlotfsuokcgxaeohdkdhdzbnr4.png" /%}

## Configuration

Currently, it runs by default on every URL scan and triggers notifications to consumers if the likelihood prediction exceeds a threshold.
