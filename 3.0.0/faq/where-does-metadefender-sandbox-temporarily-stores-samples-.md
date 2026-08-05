---
type: page
title: Where does MetaDefender Sandbox temporarily stores samples?
listed: true
description: 
index_title: Where does MetaDefender Sandbox temporarily stores samples?
hidden: false
keywords: 
tags: 
---

{% callout title="Check Your Version:" %}
This article is applied to MetaDefender Sandbox releases deployed on Linux.
{% /callout %}

#### **Question:**

Where does MetaDefender Sandbox temporarily store sample files during analysis?

#### **Solution:**

🔹 For version **2.0.0 and later**:

Submitted sample files are stored in the following directory:

`/home/sandbox/sandbox/webservice/src/storage/files`

🔹 For versions **prior to 2.0.0**:

`/home/filescanio/FileScanIO/webservice/src/storage/files`

#### **Note:**

Ensure you have the appropriate permissions to access these directories. Modifying or deleting files during analysis may impact results or system stability.

{% callout title="Support:" %}
If **Further Assistance** is required, please proceed to log a [**support case or chatting with our support engineer**](https://my.opswat.com/support).
{% /callout %}
