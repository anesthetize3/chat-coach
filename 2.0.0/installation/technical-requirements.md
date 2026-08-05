---
type: page
title: Technical Requirements
listed: true
description: 
index_title: Technical Requirements
hidden: true
keywords: 
tags: 
---

## Minimum Requirements (on premise)

- **Ubuntu Server 22.04** LTS ("Jammy Jellyfish"):
  - Support for **Ubuntu Server 20.04** LTS ("Focal Fossa") is dropped with the 2.0.0 Release
  - Please download the Ubuntu ISO image from: [https://releases.ubuntu.com/jammy/](https://releases.ubuntu.com/jammy/)
- 8 vCPUs (Preferably 16 vCPUs): a **CPU with AVX support is required** as the Sandbox includes MongoDB: [https://www.mongodb.com/docs/manual/administration/production-notes/#x86\_64](https://www.mongodb.com/docs/manual/administration/production-notes/#x86_64)
- 16 GB RAM (Preferably 32GB)
- 100 GB **Free Disc Space** (SSD): Sandbox requires 32 GB on the first installation (subsequent upgrades will potentially consume more disk space)
  - Please note that the **Ubuntu server installer** will configure the main disk as an LVM group by default (2 partitions mirroring each other). For example, on a 100 GB disk you will get approx. 50 GB usable storage. This provides redundancy and better data safety, so please consider doubling your disk size. Alternatively, you can uncheck the  *"Set up this disk as an LVM group"* option during the Ubuntu installation, see: [https://ubuntu.com/server/docs/install/storage](https://ubuntu.com/server/docs/install/storage)
- Internet access is temporarily required during the installation \& upgrade process.
- The "minimized" version of Ubuntu Server is NOT suitable for **offline installations**, since it lacks some essential packages. Please select "Ubuntu Server" here: {% inline-image url="../../assets/e9fca8758fea1b180a905b05ed25cc108fe2e297.png" /%}

*Note: More than 25000 scans/day requires a custom multi-server setup and needs to be scoped out with the engineering team.*

Due to the low resource requirements and cloud-native capability, the Sandbox does not require nested VMs and can be deployed and operate with its proprietary virtualization technology directly on the host system.

## Example Hardware Setup

- Intel Xeon-E 2488 Processor (24M Cache, 3.20 GHz, 8 cores)
- 32 GB DDR5 RAM
- 2x SSD NVMe 256 GB RAID

*Note: this is an example system that would allow processing 50K files/day with a retention period of 10 days.*

## Throughput / Minimum Requirements

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
16 GB
{% /cell %}
{% cell %}
100 GB
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
16 GB
{% /cell %}
{% cell %}
100 GB
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
16 GB
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
16 GB
{% /cell %}
{% cell %}
512 GB
{% /cell %}
{% /row %}
{% row %}
{% cell %}
25000\*
{% /cell %}
{% cell %}
16
{% /cell %}
{% cell %}
32 GB
{% /cell %}
{% cell %}
512 GB
{% /cell %}
{% /row %}
{% /table %}

\*Currently the maximum numbers of scans/day per instance

## Minimum Cloud Requirements (AWS)

- 5000 scans/day: `m6a.xlarge`
- 10000 scans/day: `c6a.2xlarge`
- 25000 scans/day: `c6a.4xlarge`

## Network Setup

It is recommended to run the product in a segregated network segment, or to operate the sandbox in a DMZ entirely.
