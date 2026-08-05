---
type: page
title: MetaDefender Core Engine
listed: true
description: 
index_title: MetaDefender Core Engine
hidden: true
keywords: 
tags: 
---

[MetaDefender Core](https://docs.opswat.com/mdcore/release-notes) now fully integrates with OPSWAT Filescan (as an engine module), and provide two separate engines:

1. **OPSWAT Filescan Embedded engine:** bundled in MetaDefender Core server, and the engine will process files locally itself.
2. **OPSWAT Filescan Remote engine**: the engine is supposed to send file requests to another remote OPSWAT Filescan system for processing. Requiring users to provide proper remote OPSWAT Filescan URL and API key.

We need separate MetaDefender Core license key for each engine option (Embedded vs. Remote).

{% callout title="Engine system requirements" %}
See the required [engine dependencies](https://docs.opswat.com/mdcore/installation) and [system requirements](https://docs.opswat.com/mdcore/filescan/system-requirements) of our Filescan engines.
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/g3evn83x56la4l9u09zjtfsyn1f0fo3csinhvbx9zu0bj8ili0p5d6t1b75n2vss.png" %}
Engine architecture
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/5m6ol6eqt9tdn2hdlxft4uxwc9b5x5o8vmo21szu2wb0dpmywp0sccbyphr899un.png" %}
Scan process result
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/yunwpkysvrouzh3wr53obdj0hwenbniyuud355srxjtjqyecg4k9lxdpere2ht4g.png" %}
Engine detailed result
{% /image %}

The integration comes with two modes:

1. **Inline:** working as a part of MetaDefender Core processing workflow (real-time processing). Allowing users to block entire processing based on OPSWAT Filescan engine's outcome and decision.
2. **Out of band:** working as a part of MetaDefender Core quarantine (post-investigation processing).Providing additional option to analyze quarantined items along with the existing Threat Intelligence technology.

OPSWAT Filescan engine (both Embedded and Remote) provides configurations under workflow rule (for inline mode), and under engine module - Inventory (for out of band mode).

{% image url="https://uploads.developerhub.io/prod/XX2D/c89t33amk5elu4fi55lgwafdtuxellsk6ik7wfc1gnj3dt6x0ctzeapo52x69mjy.png" /%}
