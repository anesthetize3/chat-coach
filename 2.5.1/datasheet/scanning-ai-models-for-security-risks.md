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

As AI becomes very popular in modern applications, companies are racing to integrate AI chatbots and other AI-powered utilities into their products to optimize work efficiency.

The sharing and reuse of pre-trained AI models has become a widespread practice. After training a model like ChatGPT, you need to save those weights (already trained model) somewhere. These files aren't just simple data - they're complex formats like Pickle, Pytorch and TensorFlow, each with their own serialization style.

Developers frequently download models from public repositories like Hugging Face, Kaggle, and others to accelerate innovation and avoid redundant training efforts. Attackers are now targeting the AI model supply chain by injecting malware, backdoors, and malicious logic into serialized model files. These compromised models can be difficult to detect using conventional security tools and may lead to remote code execution (RCE) attacks, data leak, or sabotage of downstream AI tasks.

MetaDefender Sandbox supports scanning AI model files, including `.pkl`, `.pt`, `.pb` and`.h5`, providing robust detection for the most critical attack vectors.

## **Common AI Model Attack Vectors**

Several ML model formats can introduce security risks:

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Format
{% /cell %}
{% cell header=true %}
Framework
{% /cell %}
{% cell header=true %}
Extension
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% cell header=true %}
Code Execution
{% /cell %}
{% cell header=true %}
Status
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Pickle
{% /cell %}
{% cell %}
Generic Python
{% /cell %}
{% cell %}
`.pkl`, `.pickle`
{% /cell %}
{% cell %}
Python’s default serialization format; allows arbitrary code execution during deserialization.
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Supported
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Pytorch
{% /cell %}
{% cell %}
Pytorch
{% /cell %}
{% cell %}
`.pt`, `pth`
{% /cell %}
{% cell %}
Uses Pickle internally to store model weights and architecture, vulnerable to embedded code execution.
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Supported
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Tensorflow
{% /cell %}
{% cell %}
TensorFlow
{% /cell %}
{% cell %}
`.pb`
{% /cell %}
{% cell %}
Protocol Buffers format used to store SavedModels. Can include Lambda Layer in KerasMetadata to allow arbitrary code execution.
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Supported
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Keras
{% /cell %}
{% cell %}
Keras / TensorFlow
{% /cell %}
{% cell %}
`.h5`
{% /cell %}
{% cell %}
HDF5 format used by Keras; Lambda layers serialized with marshal can enable code execution.
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% cell %}
Supported
{% /cell %}
{% /row %}
{% /table %}

## **How MetaDefender Sandbox Enhances AI Model Security**

MetaDefender Sandbox provides **comprehensive security analysis** for ML models, identifying potential threats before they can impact AI workflows.

### **Key Capabilities**

- **Support for Multi-Serialization Format Parsing:** Enables comprehensive detection across major AI model formats, including Pickle, Protocol Buffers, and Marshal serialization.
- **Leveraging Integrated Pickle Scanning Tools:** Integrates Fickling to parse Pickle’s structure and extract artifacts.
- **Deep Static Analysis:** Disassembles and analyzes serialized objects inside `pkl` , `pt` and `h5` files.
- **Graph-Level Threat Detection:** Identifies unsafe TensorFlow operators and custom graph nodes in `pb` models.
- **Uncovering Deliberate Evasion Techniques:** Exposes the hidden logic of complicated evasion techniques.

### **Showcase Report: Detect Stack Pickle technique and its Malicious contents**

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/68bf95d2a1a41633174df884/reports/3bd2c3bf-8aa4-47bb-8b5b-fb4b5dbd0a90/overview](https://www.filescan.io/uploads/68bf95d2a1a41633174df884/reports/3bd2c3bf-8aa4-47bb-8b5b-fb4b5dbd0a90/overview)
{% /callout %}

Stacked Pickle can be utilized as a trick to hide malicious behavior. By nesting multiple Pickle objects and injecting the payload across layers then combined with compression or encoding. Each layer looks benign on its own, therefore many scanners and quick inspections miss the malicious payload.

MetaDefender Sandbox peels those layers one at a time: it parses each Pickle object, decodes or decompresses encoded segments, and follows the execution chain to reconstruct the full payload. By replaying the unpacking sequence in a controlled analysis flow, the sandbox exposes the hidden logic without running the code in a production environment.

{% image url="../../assets/b60585296c7ce4b8116c58548eccc6ade9578c2b.png" /%}
