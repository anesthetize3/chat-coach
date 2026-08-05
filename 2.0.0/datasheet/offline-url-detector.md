---
type: page
title: Offline URL Reputation Overview
listed: true
description: 
index_title: Offline URL Reputation Overview
hidden: true
keywords: 
tags: 
---

MetaDefender Sandbox on-premise / standalone integrates an Offline URL detector ML model.

{% callout title="Info" %}
URL offline reputation will now auto-apply in air-gapped / offline environments (in case of lack of internet connection), but be disabled by default
{% /callout %}

## Introduction

The offline URL detection ML model enhances security by effectively identifying suspicious URLs. Unlike traditional methods, it utilizes machine learning on a dataset of labelled URLs to accurately detect threats without relying on web rendering or code analysis. **Meaning malicious URL detection can still be carried out in air-gapped sandbox environment.**

Key differences

- **Real-time vs. Offline Analysis:** Online reputation depends on real-time data and active web interactions, whereas offline URL reputation relies on pre-existing datasets and machine learning models to evaluate URLs without needing live access.
- **Resource Intensity:** Online reputation methods can be resource-intensive due to the need for real-time rendering and analysis. Offline URL reputation is less resource-demanding, as it uses pre-trained models to make assessments.
- **Adaptability:** Offline URL detection is more adaptable in environments with limited or no internet access, providing a consistent layer of security regardless of connectivity.

## Operations

The model performs a comprehensive analysis of key attributes from a new URL to assess its safety. It then generates a probability score indicating the likelihood of the URL being malicious or benign

## Example

Its adaptability to offline environments makes it versatile for various security scenarios, such as preventing malware from exfiltrating data through disguised URLs or thwarting phishing attempts by flagging fraudulent links in emails.

## Data

The Suspicious URL detector Machine Learning model was trained on close to 1 million URLs from various sources, including reputation vendors and feeds.

## Report

Offline Reputation result will be displayed under **OSINT Lookups** in the scan report.

#### The item details

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[118] %}
{% p /%}
{% /cell %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Resource**
{% /cell %}
{% cell %}
Identifies the certain URL being analyzed
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Type**
{% /cell %}
{% cell %}
Specifies the nature of the entity
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Origin**
{% /cell %}
{% cell %}
Methods to assess the reputation of the URL (e.g. **VBA Emulation**: In this example, VBA emulation helps in identifying if the code performs any malicious activities, such as downloading malware or manipulating system files, which could impact the reputation of the associated URL..)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Provider**
{% /cell %}
{% cell %}
Indicates the dataset providers: OPSWAT (Online) Reputation or OfflineURLReputation.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
**Verdict**
{% /cell %}
{% cell %}
The trained model is then applied to the extracted features, enabling it to predict whether the URL is benign or suspicious
{% /cell %}
{% /row %}
{% /table %}

[Please find the Showcase Report here.](https://docs.opswat.com/filescan/datasheet/showcase-reports#3-offline-url-reputation)

{% inline-image url="../../assets/38411c7805448bf05d612fdc49c61333b55bd157.png" /%}

## Configuration

{% callout title="Info" %}
The following setting is only required to manually enable the URL model in online mode. However, the feature is enabled automatically in offline mode.
{% /callout %}

The URL model can only provide an assessment of whether a URL is suspicious, without offering a more definitive judgment. To enable the model the following line has to be added to the appropriate configuration:

{% code %}
```bash {% title="transform.cfg" %}
enableOfflineUrlReputation=true
```
{% /code %}
