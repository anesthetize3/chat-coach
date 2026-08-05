---
type: page
title: Slow web interface in offline environment
listed: true
description: 
index_title: Slow web interface in offline environment
hidden: true
keywords: 
tags: 
---

Opening the Sandbox web interface might be slower than expected in an offline environment.

The underlying issue is that the web UI references the following external resources:

```plaintext {% title="index.html" %}
https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css
https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap
```

If the offline environment is configured correctly to immediately drop external requests, then everything works as expected.

If the offline network setup is not fully consistent, and these external requests go to a gateway/router node where they are not dropped, then a timeout will occur on the browser side (perhaps after waiting 30-40 seconds).

The recommended solution is modifying `/home/sandbox/sandbox/webservice-front/index.html` to disable these external references.

Please open that file on the Sandbox server using any text editor (e.g. nano) and locate the following section:

{% code %}
```html {% title="index.html" %}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
```
{% /code %}

Then **comment out** these 2 lines using `<!--` and `-->`. This should be the end result:

{% code %}
```html {% title="index.html" %}
<!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css" /> -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!-- <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet"> -->
```
{% /code %}

Please **save the modified index.html file** and open the Sandbox UI again in your browser!
