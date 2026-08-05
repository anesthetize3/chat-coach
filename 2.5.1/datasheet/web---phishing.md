---
type: page
title: Web & Phishing
listed: true
description: 
index_title: Web & Phishing
hidden: false
keywords: 
tags: 
---

## #1 Phishing detection

**Detection Spotlight:** {% badge text="AI detection" /%}

- **Brand Detection:** By rendering suspicious websites and subjecting them to our advanced machine learning engine we're capable of identifying nearly 300 brands. In the example provided below, you can witness a website masquerading as a streaming company known as Netflix. Our solution excels in comparing the site's content to the genuine URL, swiftly identifying such fraudulent attempts to safeguard your digital assets and personal information. [Learn more about this feature by clicking here.](../faq/brand-detection.md)
- **AI-driven analysis:** We have an AI-driven solution analyzing the **network traffic, structural and textual content** of the rendered page. Verdict of the joint model outcome can be seen after *'ML Web Threat Model'.*

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/686e4b6f61f15fb42a36916f/reports/34d28904-2462-4a27-a37a-ca5328223a34/url\_details](https://www.filescan.io/uploads/686e4b6f61f15fb42a36916f/reports/34d28904-2462-4a27-a37a-ca5328223a34/url_details)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/3ya9hcyt8x77g7egdg9u4g1yk59vdiybkiktg0g0wdvic0xogcfsxjmnn9664umv.png" /%}

---

## #2 Offline URL Reputation

**Detection Spotlight:** {% badge text="deep static" /%}{% badge text="emulation" /%}{% badge text="AI detection" /%}

The offline URL detector ML model provides a new layer of defense by effectively detecting suspicious URLs, offering a robust means to identify and mitigate threats posed by malicious links.  It leverages a dataset containing hundreds of thousands of URLs, meticulously labeled as either no threat or malicious by reputable vendors, to assess the feasibility of accurately detecting suspicious URLs through machine learning techniques.

It is important to note that this feature is particularly useful in air-gapped environments where online reputation lookups are not available.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/6696cf5a3d7227f9379408e2/reports/30c313a7-40ac-46e8-a473-661f0e17dddd/osint](https://www.filescan.io/uploads/6696cf5a3d7227f9379408e2/reports/30c313a7-40ac-46e8-a473-661f0e17dddd/osint)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/yxr3s89ofvfgxoy6mf0g225889q79e903xwrltm7xt6po3glp3lbxlvmtvyuormg.png" /%}

[Learn more about the Suspicious URL Detection in Offline Mode by clicking here.](/metadefender-sandbox/2.1.0/datasheet/offline-url-detector)

---

## #3 Google DKIM Replay Attack Detection

**Detection Spotlight:** {% badge text="deep static" /%}

Email authentication mechanisms like SPF, DKIM, and DMARC are essential, but sophisticated attackers can sometimes bypass them. This example showcases a scenario where an email, despite being authentically signed by Google and passing standard checks, was identified as malicious by MetaDefender Sandbox.

MetaDefender Sandbox detected several anomalies along with other indicators:

- DKIM Boundary Violation: Identified content added beyond the scope of the DKIM signature.
- Obfuscation Techniques: Detected excessive whitespace used to hide malicious intent.
- Phishing Patterns: Recognized urgent calls-to-action characteristic of phishing attempts.
- Header Analysis: Flagged anomalies in email headers associated with OAuth application abuse.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/680a306e46fe05453ca613e8/reports/4053f0c3-c70f-48f2-ba0d-62d705d4e427/overview](https://www.filescan.io/uploads/680a306e46fe05453ca613e8/reports/4053f0c3-c70f-48f2-ba0d-62d705d4e427/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/bg94492d9c2k3fiyeqppf8r6qwrmbrbczjxx04w3nlcakr00mkdgmpv8cg4rlo1a.png" %}
Advanced threat indicator detections for the phishing email
{% /image %}

---

## #4 ClickFix, a trending social engineering technique

**Detection Spotlight:** {% badge text="AI detection" /%} {% badge text="emulation" /%}

ClickFix is an emerging web-based threat that leverages social engineering to silently trick users into executing malicious commands. Unlike traditional phishing, ClickFix operates through deceptive UX elements and clipboard manipulation rather than file downloads or credential theft.

The ClickFix website presents a fake reCAPTCHA or "bot protection" screen to appear legitimate. The user is then asked to verify themselves—often through a harmless-looking interaction—while, in the background, obfuscated JavaScript code silently runs. This script dynamically decodes a malicious command and copies it directly to the system clipboard. Next, the user is presented with misleading instructions and guide to execute the malware, unaware of the danger.

ClickFix highlights how simple web techniques, combined with user deception, can effectively bypass traditional security layers—making sandbox analysis critical for uncovering stealthy, low-footprint attacks like this one.

MetaDefender Sandbox analyses this threat end-to-end. The sandbox begins by rendering the malicious URL and applying phishing detection models to identify suspicious content. It then extracts and emulates the JavaScript, simulating user actions to reach the critical moment when the clipboard is modified. Once the hidden command is captured, it is emulated, allowing the sandbox to fully trace the malicious execution flow. This not only exposes the clipboard-based tactic but also reveals the payload’s behavior and infection chain.

{% callout title="URL for the sample" %}
[https://www.filescan.io/uploads/686fb12180b46be06e9dc277/reports/b1ff6c4c-1fe3-4001-b0f9-a113a282ae9f/overview](https://www.filescan.io/uploads/686fb12180b46be06e9dc277/reports/b1ff6c4c-1fe3-4001-b0f9-a113a282ae9f/overview)
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/igzm9g3ozph923ijxpjpsne3qk7qtyp5qmek1zyzwv5fmmt4f4sj3pqf2d8cqdx4.png" %}
URL Rendering \& Phishing detected by ML model.
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/15g5jukwtd0z7ooecuji0xbrx2p9g4oj7s0aunlqv1xcdi26ahj1yr1nefu5a6h3.png" %}
ClickFix Attack Pattern Detected
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/evtvnauthna58ny1fp2zdlu3tsmjoeu43lof23v3jypb30hs7hut9b3ep0ajdin9.png" %}
Emulation of ClickFix JavaScript code that reveals malicious copied command to the clipboard.
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/q9vrkxlpfw4f65xjj9iz3u7j7afkbcpby2mdw65lcqeo22rmdb9vysqrrgq8l8ve.png" %}
Emulation of PowerShell code copied silently in the clipboard.
{% /image %}

---
