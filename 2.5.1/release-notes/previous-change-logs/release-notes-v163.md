---
type: page
title: Release Notes for v1.63
listed: true
description: 
index_title: Release Notes for v1.63
hidden: true
keywords: 
tags: 
---

---

### Date: 28 November, 2022

Fixed:

- remove "null"-byte padding from Javascript, which was throwing off the emulator
- fsBroker retry attempts would only try one time (verifyAppServersAreAvailableRetryMax) breaking automatic service restarts on slow machines
