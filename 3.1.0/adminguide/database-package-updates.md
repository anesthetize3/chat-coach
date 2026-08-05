---
type: page
title: Database package updates
listed: true
description: 
index_title: Database package updates
hidden: false
keywords: 
tags: 
---

Database packages contain threat detection updates that keep your product's detection capabilities current. These packages are updated regularly through the update infrastructure and are deployed without disrupting ongoing operations — no restarts or downtime required.

Go to **Admin Panel \> Settings \> Integration \> Engine Database Update** to see the current database package status.

{% image url="../../assets/35f83ec673852f1284440d88e4763513920c2874.png" /%}

## Automatic updates

The product can check for, download, and deploy new database packages automatically, without any manual intervention.

**How it works:**

- The system contacts the update server at regular intervals.
- If a newer database package is available, it is downloaded automatically.
- The package is deployed after download, without service interruption.

**Configuration**

To configure automatic updates, go to:

> **Admin Panel \> Settings \> Configuration \> Communication and Integration \> Engine Database Update**

{% image url="../../assets/b26dd1c579dd8706d7d46698979eeb4fb12d1797.png" /%}

{% callout type="warning" title="Warning" %}
The *ENGINE\_\_\_DATABASE\_\_\_CHECK\_FOR\_UPDATES setting must be enabled in order for the automatic update feature to run. If it is disabled, the automatic updates will not run regardless of the state of the other settings.*
{% /callout %}

## Manual updates

### Online environments

If your system has internet access, you can trigger an update on demand. The product will contact the update server and apply the update.

1. Go to **Admin Panel \> Settings \> Integration \> Engine Database Update**.
2. Review the currently installed database version.
3. Click **Check for Updates**.
4. If a new package is available, click **Update all** to apply it.

{% image url="../../assets/073d6fea7408526264f1069e13c03ce454170e2a.png" /%}

To revert to the previous database version, click **Revert all** on the same page.

{% image url="../../assets/17f3022b44bf6ef099c12feda16a123cee87527f.png" /%}

### Offline environments (air-gapped)

For environments with no internet access, use the [MetaDefender Update Downloader](https://www.opswat.com/docs/mddownloader) tool to obtain the package, then upload it manually.

{% callout title="Info" %}
Available since MetaDefender Update Downloader tool, version 3.4.0.

Available since MetaDefender Aether \[Sandbox\], version 3.1.0.
{% /callout %}

1. Download the latest package using the Offline Update Downloader Tool. See the [Offline Update Downloader Tool documentation](https://www.opswat.com/docs/mddownloader) for instructions.
2. Add your **Sandbox license** in the downloader tool.
3. The tool downloads both a database package and an engine package. **Use only the database package** — ignore the engine package, as it is intended for the MetaDefender Core product.
4. Go to Sandbox, **Admin Panel → Settings → Integration → Engine Database Update**.
5. Upload the database package descriptor (yml file) and the update package itself (zip file).

{% image url="../../assets/f943abaefe6adb00269c45b9f9bdeda16c18db48.png" /%}

{% image url="../../assets/80fbb7571b41cf1998863ae54c21f2d6cbe5864c.png" /%}

To revert to the previous database version, click **Revert all** on the same page.
