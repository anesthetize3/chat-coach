---
type: page
title: Supported packers for unpacking
listed: true
description: 
index_title: Supported packers for unpacking
hidden: true
keywords: 
tags: 
---

Our engine can unpack a wide range of packers, including both specific and generic ones. This is important because packers are often used by malware to evade detection. By unpacking them we can analyze it and identify any threats embedded.

**Specifically supported packers:**

- ASPack
- FSG
- MEW
- MPRESS
- PEtite
- UPX
- YZPack

{% callout type="success" title="Unpacking" %}
On the following link you can find the sample from the screenshot below:

[https://www.filescan.io/uploads/6502117c9bae8a378555f25f/reports/a50dfc89-c1e4-4dfc-8721-f7c151c14d5f/files](https://www.filescan.io/uploads/6502117c9bae8a378555f25f/reports/a50dfc89-c1e4-4dfc-8721-f7c151c14d5f/files)
{% /callout %}

The following screenshot from the linked analysis shows the unpacked PE is available to be downloaded.

{% image url="https://uploads.developerhub.io/prod/XX2D/3rhmui89e4cg0mdezp8skufr6ry5tn1tls9e2cwk8c6zop2hf68zanmzp587rife.png" /%}

Additionally, we also support extraction and decompilation of scripting code that has be wrapped as an executable. This technique is commonly found in malware and can be effective to deviate the focus of the analysis from the relevant payload. Hence we detect, extract, and decompile such implementation in order to be able to focus on the relevant payload.

**Supported compiled scripting languages:**

- PyInstaller
- Py2Exe
- Nuitka
- AutoIT
- JPHP

{% callout type="success" title="Compiled script unpacking" %}
On the following link you can find the sample from the screenshot below:

[https://www.filescan.io/uploads/66fbacc03aaac9834b817ad2/reports/7418f790-69ae-4366-9e90-7a85cf02cdef/files](https://www.filescan.io/uploads/6502117c9bae8a378555f25f/reports/a50dfc89-c1e4-4dfc-8721-f7c151c14d5f/files)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/lwglbmkuw1ss53czlepdankpl2uq1uqs3400g4usg6l5gadduafzmxipkoa1irqq.png" /%}
