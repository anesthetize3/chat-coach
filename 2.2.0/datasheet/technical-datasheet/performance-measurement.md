---
type: page
title: Performance Measurement
listed: true
description: 
index_title: Performance Measurement
hidden: true
keywords: 
tags: 
---

Description

Performance management in this context refers to the assessment of the system’s ability to handle various file types efficiently. The goal is to measure throughput across different configurations, ensuring optimal resource allocation and system stability. By analyzing scan rates, processing efficiency, and system bottlenecks, performance management helps in identifying improvements and maintaining consistent performance under different workloads.

### Test Configurations

{% table layout="auto" %}
{% row %}
{% cell header=true %}
**Setup**
{% /cell %}
{% cell header=true colwidth=[179] %}
**CPU Cores**
{% /cell %}
{% cell header=true %}
**Ram**
{% /cell %}
{% cell header=true %}
**Parallel Count**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Config 1
{% /cell %}
{% cell %}
8
{% /cell %}
{% cell %}
16 GB
{% /cell %}
{% cell %}
5
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Config 2
{% /cell %}
{% cell %}
16
{% /cell %}
{% cell %}
32 GB
{% /cell %}
{% cell %}
10
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Config 3
{% /cell %}
{% cell %}
20
{% /cell %}
{% cell %}
32 GB
{% /cell %}
{% cell %}
15
{% /cell %}
{% /row %}
{% /table %}

{% callout type="warning" title="Warning" %}
For optimal performance, ensure that the number of CPU cores allocated is at least equal to the configured parallel count. This helps prevent resource bottlenecks and maximizes processing efficiency.
{% /callout %}

## Data Set

{% table layout="auto" %}
{% row %}
{% cell header=true %}
File Category
{% /cell %}
{% cell header=true %}
File Type
{% /cell %}
{% cell header=true %}
Number of files
{% /cell %}
{% cell header=true %}
Total Size (MB)
{% /cell %}
{% cell header=true %}
Average Size (MB)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Adobe
{% /cell %}
{% cell %}
PDF
{% /cell %}
{% cell %}
75
{% /cell %}
{% cell %}
81
{% /cell %}
{% cell %}
0\.93
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Executable
{% /cell %}
{% cell %}
EXE
{% /cell %}
{% cell %}
6
{% /cell %}
{% cell %}
65
{% /cell %}
{% cell %}
0\.09
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
MSI
{% /cell %}
{% cell %}
3
{% /cell %}
{% cell %}
9,6
{% /cell %}
{% cell %}
0\.31
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Image
{% /cell %}
{% cell %}
BMP
{% /cell %}
{% cell %}
16
{% /cell %}
{% cell %}
108\.6
{% /cell %}
{% cell %}
0\.15
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
JPG
{% /cell %}
{% cell %}
84
{% /cell %}
{% cell %}
49\.8
{% /cell %}
{% cell %}
1\.69
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
PNG
{% /cell %}
{% cell %}
69
{% /cell %}
{% cell %}
35\.4
{% /cell %}
{% cell %}
1\.9
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Media
{% /cell %}
{% cell %}
MP3
{% /cell %}
{% cell %}
27
{% /cell %}
{% cell %}
181\.1
{% /cell %}
{% cell %}
0\.15
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
MP4
{% /cell %}
{% cell %}
10
{% /cell %}
{% cell %}
105\.9
{% /cell %}
{% cell %}
0\.09
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Office
{% /cell %}
{% cell %}
DOC
{% /cell %}
{% cell %}
45
{% /cell %}
{% cell %}
102
{% /cell %}
{% cell %}
0\.44
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
DOCX
{% /cell %}
{% cell %}
47
{% /cell %}
{% cell %}
40
{% /cell %}
{% cell %}
1\.17
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
ODS
{% /cell %}
{% cell %}
22
{% /cell %}
{% cell %}
6\.2
{% /cell %}
{% cell %}
3\.55
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
ODT
{% /cell %}
{% cell %}
18
{% /cell %}
{% cell %}
1
{% /cell %}
{% cell %}
18
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
PPT
{% /cell %}
{% cell %}
71
{% /cell %}
{% cell %}
409\.8
{% /cell %}
{% cell %}
0\.17
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
PPTX
{% /cell %}
{% cell %}
73
{% /cell %}
{% cell %}
181\.3
{% /cell %}
{% cell %}
0\.40
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
XLS
{% /cell %}
{% cell %}
67
{% /cell %}
{% cell %}
59\.7
{% /cell %}
{% cell %}
1\.12
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
XLSX
{% /cell %}
{% cell %}
68
{% /cell %}
{% cell %}
59\.6
{% /cell %}
{% cell %}
1\.14
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Text
{% /cell %}
{% cell %}
CHM
{% /cell %}
{% cell %}
11
{% /cell %}
{% cell %}
1\.9
{% /cell %}
{% cell %}
5\.79
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
CSV
{% /cell %}
{% cell %}
20
{% /cell %}
{% cell %}
49\.5
{% /cell %}
{% cell %}
0\.40
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
EML
{% /cell %}
{% cell %}
6
{% /cell %}
{% cell %}
13
{% /cell %}
{% cell %}
0\.46
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
HTML
{% /cell %}
{% cell %}
215
{% /cell %}
{% cell %}
16
{% /cell %}
{% cell %}
13\.44
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
RTF
{% /cell %}
{% cell %}
19
{% /cell %}
{% cell %}
6\.4
{% /cell %}
{% cell %}
2\.99
{% /cell %}
{% /row %}
{% row %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
TXT
{% /cell %}
{% cell %}
100
{% /cell %}
{% cell %}
44\.1
{% /cell %}
{% cell %}
2\.27
{% /cell %}
{% /row %}
{% /table %}

## Throughput Results

Adobe, Executable, Office, Text, Image, Media

### Scans Per Day

{% table layout="auto" %}
{% row %}
{% cell header=true %}
**File Type**
{% /cell %}
{% cell header=true %}
Config **1**
{% /cell %}
{% cell header=true %}
Config **2**
{% /cell %}
{% cell header=true %}
Config **3**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Adobe
{% /cell %}
{% cell %}
9,552
{% /cell %}
{% cell %}
17,280
{% /cell %}
{% cell %}
23,784
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Executable
{% /cell %}
{% cell %}
22,296
{% /cell %}
{% cell %}
35,472
{% /cell %}
{% cell %}
46,516
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Office
{% /cell %}
{% cell %}
9,312
{% /cell %}
{% cell %}
14,400
{% /cell %}
{% cell %}
18,768
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Text
{% /cell %}
{% cell %}
13,392
{% /cell %}
{% cell %}
15,384
{% /cell %}
{% cell %}
17,832
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Image
{% /cell %}
{% cell %}
42,336
{% /cell %}
{% cell %}
96,240
{% /cell %}
{% cell %}
123,120
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Media
{% /cell %}
{% cell %}
37,728
{% /cell %}
{% cell %}
74,736
{% /cell %}
{% cell %}
111,072
{% /cell %}
{% /row %}
{% /table %}

### Average processing time per file

{% callout title="Info" %}
The average processing times shown are approximations, assuming that file types with dynamic analysis support often included dynamic analysis in their processing. This may slightly influence the observed times, especially for complex file types like executables and office documents.

Processing times in MetaDefender Core may vary slightly from these values, and real-world processing times can differ depending on the specific file type mix encountered in different environments.
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
**File Type**
{% /cell %}
{% cell header=true %}
Config **1**
{% /cell %}
{% cell header=true %}
Config **2**
{% /cell %}
{% cell header=true %}
Config **3**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Adobe
{% /cell %}
{% cell %}
18\.0 sec
{% /cell %}
{% cell %}
8\.1 sec
{% /cell %}
{% cell %}
6\.6 sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Executable
{% /cell %}
{% cell %}
12\.9 sec
{% /cell %}
{% cell %}
8\.9 sec
{% /cell %}
{% cell %}
4\.8 sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Office
{% /cell %}
{% cell %}
18\.0 sec
{% /cell %}
{% cell %}
12\.2 sec
{% /cell %}
{% cell %}
8\.5 sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Text
{% /cell %}
{% cell %}
12\.5 sec
{% /cell %}
{% cell %}
8\.7 sec
{% /cell %}
{% cell %}
8\.4 sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Image
{% /cell %}
{% cell %}
4\.2 sec
{% /cell %}
{% cell %}
2\.9 sec
{% /cell %}
{% cell %}
2\.7 sec
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Media
{% /cell %}
{% cell %}
4\.6 sec
{% /cell %}
{% cell %}
4\.2 sec
{% /cell %}
{% cell %}
2\.8 sec
{% /cell %}
{% /row %}
{% /table %}
