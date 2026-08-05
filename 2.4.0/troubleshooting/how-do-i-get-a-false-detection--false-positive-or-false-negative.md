---
type: page
title: How do I get a False Detection (False Positive or False Negative) corrected?
listed: true
description: 
index_title: How do I get a False Detection (False Positive or False Negative) corrected?
hidden: true
keywords: 
tags: 
---

If you are using MetaDefender Sandbox believe your file is incorrectly labeling (i.e falsely detecting) whether a file is malicious by a faulty threat indicator, you can have that file analyzed by OPSWAT’s expert analyst team simply by logging a [**support case or chatting with our support engineer**](https://my.opswat.com/support).

## Workaround

While waiting for the fix, you can optionally disable the Threat Indicator by following [this instruction](https://www.opswat.com/docs/filescan/faq/how-to-disable-a-threat-indicator-).

{% callout type="warning" title="Warning:" %}
Caution When Disabling Threat Indicator Consumers, as it may have potential impact on other submissions and scoring.

Disabling the wrong threat indicator consumer can significantly impact detection capabilities. For example, the **S040** indicator referenced in the “[How to disable a Threat Indicator?](https://www.opswat.com/docs/filescan/faq/how-to-disable-a-threat-indicator-)” article is a critical case—disabling this single consumer disables over **10 other related consumers**, most of which are tied to **phishing detection**.
{% /callout %}

{% callout title="Support:" %}
If **Further Assistance** is required, please proceed to log a [**support case or chatting with our support engineer**](https://my.opswat.com/support).
{% /callout %}
