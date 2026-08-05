---
type: page
title: Scanning AI Models for Security Risks
listed: true
description: 
index_title: Scanning AI Models for Security Risks
hidden: true
keywords: 
tags: 
---

As AI adoption increases, machine learning (ML) models have become a potential attack vector for malware. Certain model formats, particularly those using Python’s serialization, can execute arbitrary code when loaded, making them susceptible to remote code execution (RCE) attacks. **MetaDefender Sandbox supports scanning AI model files, including** `**.pkl**` **and** `**.pt**`**, providing robust detection for the most critical attack vectors.**

## **Common AI Model Attack Vectors**

Several ML model formats can introduce security risks:

- **Pickle Files (**`**.pkl**`**,** `**.pt**`**)** – Used in PyTorch and other ML frameworks, these files allow deserialization of arbitrary objects, potentially executing embedded malicious code.
- **PyTorch Checkpoints (**`**pytorch_model.bin**`**)** – Relies on Python's `pickle` mechanism, making it vulnerable to similar RCE risks.
- **TensorFlow Models (**`**.h5**`**,** `**.pb**`**)** – Can be manipulated to trigger vulnerabilities in TensorFlow’s parsing logic.
- **ONNX Models (**`**.onnx**`**)** – While structured, certain model operators may still be exploited.
- **ZIP/TAR Archives (**`**.zip**`**,** `**.tar.gz**`**)** – Often used to package multiple files, potentially concealing malicious scripts or payloads.

## **How MetaDefender Sandbox Enhances AI Model Security**

MetaDefender Sandbox provides **comprehensive security analysis** for ML models, identifying potential threats before they can impact AI workflows.

### **Key Capabilities:**

- **Deep Static Analysis:** Extracts and analyzes serialized objects inside `.pkl` and `.pt` files.
- **Heuristic and Behavioral Detection:** Identifies suspicious execution patterns and potential exploitation attempts.

By scanning AI model files **before deployment**, organizations can mitigate the risk of malicious payloads compromising their AI infrastructure.
