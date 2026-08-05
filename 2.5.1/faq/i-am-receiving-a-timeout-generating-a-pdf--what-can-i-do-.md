---
type: page
title: I am receiving a timeout generating a PDF, what can I do?
listed: true
description: 
index_title: I am receiving a timeout generating a PDF, what can I do?
hidden: true
keywords: 
tags: 
---

{% callout title="Check Your Version:" %}
This article applies to all MetaDefender Sandbox releases.
{% /callout %}

To prevent timeout when exporting large reports in PDF format, please follow these steps:

- Navigate to *Admin panel -\> Settings -\> Functionality Extensions -\> Report format*
- Check the REPORT\_FORMAT\_ALL\_PAGES checkbox to reveal the new settings
- Reduce the limit of extracted strings included in the generated PDF by editing the **REPORT\_FORMAT\_STRINGS\_LIMIT** - Only include this amount of extracted strings into HTML/PDF report
- You can also configure the extracted strings to only include interesting ones by changing the **REPORT\_FORMAT\_STRINGS\_MODE** - What strings to include into HTML/PDF report:
  - *All* - include all strings
  - *Prefer interesting* - include interesting strings first, and than other strings till limit is reached
  - *Interesting* - include only interesting strings

{% image url="../../assets/6e1eb40d7f574042a069071857470d9ff166da55.png" /%}

{% callout title="Support:" %}
If **Further Assistance** is required, please proceed to log a [**support case or chat with one of our support engineers**](https://my.opswat.com/support).
{% /callout %}
