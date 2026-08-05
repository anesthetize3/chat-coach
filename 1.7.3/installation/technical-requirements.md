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

## Minimum Requirements (on premise)

- **Ubuntu Server 20.04** LTS ("Focal Fossa"):
  - Please download the Ubuntu ISO image from: [https://releases.ubuntu.com/focal/](https://releases.ubuntu.com/focal/)
- 8 vCPUs (Preferably 16 vCPUs)
- 16 GB RAM (Preferably 32GB)
- 32 GB **Free Disk Space** (SSD): Filescan requires 25 GB on the first installation (subsequent upgrades will potentially consume more disk space)
  - Please note that the **Ubuntu server installer** will configure the main disk as an LVM group by default (2 partitions mirroring each other). For example, on a 100 GB disk you will get approx. 50 GB usable storage. This provides redundancy and better data safety, so please consider doubling your disk size. Alternatively, you can uncheck the  *"Set up this disk as an LVM group"* option during the Ubuntu installation, see: [https://ubuntu.com/server/docs/install/storage](https://ubuntu.com/server/docs/install/storage)

*Note: More than 25000 scans/day requires a custom multi-server setup and needs to be scoped out with the engineering team.*

Due to the low resource requirements and cloud-native capability, OPSWAT Filescan does not require nested VMs and can be deployed and operate with its proprietary virtualization technology directly on the host system.

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

## Minimum Cloud Requirements (AWS)

- 5000 scans/day: t3a.2xlarge
- 10000 scans/day: c4.4xlarge
- 25000 scans/day: c4.8xlarge

## Network Setup

It is recommended to run the product in a segregated network segment, or to operate Filescan engine in a DMZ entirely.
