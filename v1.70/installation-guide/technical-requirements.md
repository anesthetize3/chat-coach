---
type: page
title: Technical Requirements
listed: true
description: 
index_title: Technical Requirements
hidden: false
keywords: 
tags: 
---

## Minimal Technical Requirements

- Ubuntu Server 20.04 LTS ("Focal Fossa")
- 8 vCPUs (Preferably 16 vCPUs)
- 16 GB RAM (Preferably 32GB)
- 32 GB SSD Disk Space

## Example Hardware Setup

- Intel Xeon-E 2136 (12M Cache, 3.30 GHz)
- RAM 32GB DDR4 ECC 2666 MHz
- 2x SSD NVMe 256GB RAID

*Note: this is an example system that would allow processing 50K files/day with a retention period of 10 days.*

## Throughput / Hardware Requirements

The following table lists explanatory system specs with a retention period of 10 days:

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Scans Per Day
{% /cell %}
{% cell header=true %}
Required System CPUs
{% /cell %}
{% cell header=true %}
Required System RAM
{% /cell %}
{% cell header=true %}
Required Storage per Retention Period
{% /cell %}
{% /row %}
{% row %}
{% cell %}
1000
{% /cell %}
{% cell %}
4
{% /cell %}
{% cell %}
4 GB
{% /cell %}
{% cell %}
256 GB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
2500
{% /cell %}
{% cell %}
4
{% /cell %}
{% cell %}
4 GB
{% /cell %}
{% cell %}
256 GB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
5000
{% /cell %}
{% cell %}
4
{% /cell %}
{% cell %}
4 GB
{% /cell %}
{% cell %}
256 GB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
10000
{% /cell %}
{% cell %}
8
{% /cell %}
{% cell %}
8 GB
{% /cell %}
{% cell %}
256 GB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
25000
{% /cell %}
{% cell %}
16
{% /cell %}
{% cell %}
16 GB
{% /cell %}
{% cell %}
256 GB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
50000
{% /cell %}
{% cell %}
28
{% /cell %}
{% cell %}
28 GB
{% /cell %}
{% cell %}
512 GB
{% /cell %}
{% /row %}
{% /table %}
