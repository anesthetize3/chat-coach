---
type: page
title: FSIO Fuzzy hash lookup
listed: true
description: 
index_title: FSIO Fuzzy hash lookup
hidden: false
keywords: 
tags: 
---

Fuzzy FSIO hashes are basically a SHA-256 of a long string that is built using a streamlined order, containing very high-level, but specific attributes of an input file. Filscan calculates FSIO Fuzzy hash for each appropriate input sample and looks for this hash in a specifically defined list.

**Fuzzy hash lookup results are displayed in OSINT Lookup section**

Please note, that you may not see result for every scanned malicious data.

The feature is enabled by default. To turn it off do the following steps:

**Step #1 - Open** `FileScanIO/fsTransform/conf/transform.properties.custom` **in a text editor**

{% code %}
```bash
enableFuzzyHashLookup=false
```
{% /code %}

Please remember to **save the file.**

**Step #3 - Restart the** `fsio` **service**

{% code %}
```bash
sudo service fsio restart
```
{% /code %}
