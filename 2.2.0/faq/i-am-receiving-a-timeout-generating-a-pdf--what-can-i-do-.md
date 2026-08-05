---
type: page
title: I am receiving a timeout generating a PDF, what can I do?
listed: false
description: 
index_title: I am receiving a timeout generating a PDF, what can I do?
hidden: true
keywords: 
tags: 
---

To prevent timeout when exporting large reports in PDF format, please follow these steps:

- Go to *Admin panel -\> Settings -\> Configuration -\> General -\> Jobs*

{% image url="https://uploads.developerhub.io/prod/XX2D/fpyhfpd2hfvc61cn5uhygsyyczbnxe1bzfm3bpzez20rxjfenplkm9jv8s2p4ab8.png" /%}

- Reduce the limit of extracted strings included in the generated PDF by editing the following setting:
  - **REPORT\_FORMAT\_STRINGS\_LIMIT** - Only include this amount of extracted strings into HTML/PDF report
- You can limit the extracted strings to only include interesting ones by changing the following field:
  - **REPORT\_FORMAT\_STRINGS\_MODE** - What strings to include into HTML/PDF report
  - *All* - include all strings
  - *Prefer interesting* - include interesting strings first, and than other strings till limit is reached
  - *Interesting* - include only interesting strings

{% image url="https://uploads.developerhub.io/prod/XX2D/4fvldkh8m1x04ktuxpwuog6625npqrchhzi1lt8pydj1t2wh3i0jvgfzadpxio5l.png" /%}
