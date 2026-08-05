---
type: page
title: Basic Features
listed: true
description: 
index_title: Basic Features
hidden: false
keywords: 
tags: 
---

**Step #1 - Open** `/home/sandbox/sandbox/transform.cfg` **in a text editor**

**Step #2 - Modify the configuration by adding or modifying the properties on this page**

**Step #3 - Save the file and restart the** `sandbox` **service**

## Second Stage Malware Detection

Enable file downloads to detect 2nd stage malware downloaded from the Internet

{% code %}
```bash {% title="transform.cfg" %}
runFileDownloaders=true
runFileDownloaderDistributedTimeoutMs=60000
fileDownloaderMaxFileDownloads=10
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runFileDownloaders
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Main switch to enable file downloads
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runFileDownloaderDistributedTimeoutMs
{% /cell %}
{% cell %}
1 minute
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
fileDownloaderMaxFileDownloads
{% /cell %}
{% cell %}
10
{% /cell %}
{% cell %}
Download limit, '0' means no limit.
{% /cell %}
{% /row %}
{% /table %}

## Malware Config Extraction

Enable [malware config extraction](https://docs.opswat.com/filescan/datasheet/supported-malwares-for-config-extraction)

{% code %}
```bash {% title="transform.cfg" %}
malwareConfigExtractionEnabled=true
malwareConfigExtractionMaxInputFileSize=100
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
malwareConfigExtractionEnabled
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable malware config extraction
{% /cell %}
{% /row %}
{% row %}
{% cell %}
malwareConfigExtractionMaxInputFileSize
{% /cell %}
{% cell %}
100 MB
{% /cell %}
{% cell %}
File size limit
{% /cell %}
{% /row %}
{% /table %}

## Certificate Extraction

Enable certificate extraction for executable files and PDF documents

{% code %}
```bash {% title="transform.cfg" %}
extractCertificates=true
osslExecutionTimeout=30
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
extractCertificates
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch do enable / disable certificate extraction
{% /cell %}
{% /row %}
{% row %}
{% cell %}
osslExecutionTimeout
{% /cell %}
{% cell %}
30 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}

## YARA

Enable YARA rule matching

{% code %}
```bash {% title="transform.cfg" %}
runYaraRulesOnInputFile=true
runYaraRulesOnExtractedFiles=true
yaraExecutionTimeout=30
runYaraRulesOnInputFileMaxFileSizeInMb=100
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runYaraRulesOnInputFile
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable YARA rule matching
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runYaraRulesOnExtractedFiles
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Execute YARA also on extracted files
{% /cell %}
{% /row %}
{% row %}
{% cell %}
yaraExecutionTimeout
{% /cell %}
{% cell %}
30 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runYaraRulesOnInputFileMaxFileSizeInMb
{% /cell %}
{% cell %}
100 MB
{% /cell %}
{% cell %}
File size limit, '0' means no limit
{% /cell %}
{% /row %}
{% /table %}

## Image Text Extraction (OCR)

Enable text extraction from images

{% code %}
```bash {% title="transform.cfg" %}
runTesseractOCRForImages=true
tesseractExecutionTimeout=10
tesseractLimitPerTransform=5
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runTesseractOCRForImages
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable OCR
{% /cell %}
{% /row %}
{% row %}
{% cell %}
tesseractExecutionTimeout
{% /cell %}
{% cell %}
10 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% row %}
{% cell %}
tesseractLimitPerTransform
{% /cell %}
{% cell %}
5
{% /cell %}
{% cell %}
Limit: number of images to process
{% /cell %}
{% /row %}
{% /table %}

## QR Code Scan

Enable QR code scan for images

{% code %}
```bash {% title="transform.cfg" %}
runQRCodeScanForImages=true
qrCodeScanLimitPerTransform=20
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runQRCodeScanForImages
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable QR code scanning
{% /cell %}
{% /row %}
{% row %}
{% cell %}
qrCodeScanLimitPerTransform
{% /cell %}
{% cell %}
20
{% /cell %}
{% cell %}
Limit: number of images to process
{% /cell %}
{% /row %}
{% /table %}

## Text Metrics

{% code %}
```bash {% title="transform.cfg" %}
generateTextMetrics=true
generateTextMetricsNGramSize=5
generateTextMetricsIncludeTopNGrams=20
```
{% /code %}

Enable text metrics generation like entropy, average word size, etc.

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
generateTextMetrics
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Enable / disable text metrics generation
{% /cell %}
{% /row %}
{% row %}
{% cell %}
generateTextMetricsNGramSize
{% /cell %}
{% cell %}
5
{% /cell %}
{% cell %}
Size of collected ngrams
{% /cell %}
{% /row %}
{% row %}
{% cell %}
generateTextMetricsIncludeTopNGrams
{% /cell %}
{% cell %}
20
{% /cell %}
{% cell %}
Number of considered ngrams
{% /cell %}
{% /row %}
{% /table %}

## Visualization

Enable image rendering of input file (file preview pages)

{% code %}
```bash {% title="transform.cfg" %}
runFileVisualizer=true
runFileVisualizerDistributedTimeoutMs=10000
```
{% /code %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Property name
{% /cell %}
{% cell header=true %}
Default value
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runFileVisualizer
{% /cell %}
{% cell %}
true
{% /cell %}
{% cell %}
Switch to enable / disable visualization
{% /cell %}
{% /row %}
{% row %}
{% cell %}
runFileVisualizerDistributedTimeoutMs
{% /cell %}
{% cell %}
10 seconds
{% /cell %}
{% cell %}
Execution timeout
{% /cell %}
{% /row %}
{% /table %}
