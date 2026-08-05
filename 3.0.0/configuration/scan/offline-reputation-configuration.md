---
type: page
title: Offline Reputation Service
listed: true
description: 
index_title: Offline Reputation Service
hidden: false
keywords: 
tags: 
---

The **Offline** **Reputation Service** allows your organization to influence threat decisions by managing known good and bad files and indicators. You can supply your own local reputation data, and our system also includes managed reputation entries out of the box.

{% callout title="Info" %}
This feature is available since version `2.3.0`.
{% /callout %}

{% callout type="success" title="Pro Tip" %}
Use comments in your reputation files to keep track of sources—just add a description after a comma!
{% /callout %}

## Supported Data Types

Sandbox supports reputation entries for the following data types:

- `md5` – File hash (32-character)
- `sha256` – File hash (64-character)
- `ip` – IPv4 or IPv6 addresses
- `domain` – Network domain names
- `url` – Full URLs
- `digicert_owner` – Digital Certificate owners (common name / organization)

Each entry can be part of either an **allow list** or a **block list**, to determine whether files or indicators (IOCs) should be trusted or flagged.

{% callout title="Note" %}
Only **allowed** entries are supported for Digital Certificate owners.
{% /callout %}

{% callout type="warning" title="Warning" %}
Sandbox cannot verify **certificates** in **offline environments**, therefore the certificate allowlist is ignored for allow listing.
{% /callout %}

## Directory Structure

Reputation data is stored in the following directories:

- **System-managed data**: has been removed from directory structure, it is a part of the detection package
- **Customer-provided data**: `<sandbox>/transform/data/reputation/external`(Customers can edit and manage this at any time)

{% callout title="Note" %}
Customer managed data takes precedence on conflict.
{% /callout %}

## File Naming Convention

Customers can provide their reputation data in files following this naming format:

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Data Type
{% /cell %}
{% cell header=true %}
Allow list file
{% /cell %}
{% cell header=true %}
Block list file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MD5
{% /cell %}
{% cell %}
md5\_allowed.txt
{% /cell %}
{% cell %}
md5\_blocked.txt
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SHA256
{% /cell %}
{% cell %}
`sha256_allowed.txt`
{% /cell %}
{% cell %}
sha256\_blocked.txt
{% /cell %}
{% /row %}
{% row %}
{% cell %}
IP
{% /cell %}
{% cell %}
ip\_allowed.txt
{% /cell %}
{% cell %}
ip\_blocked.txt
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Domain
{% /cell %}
{% cell %}
domain\_allowed.txt
{% /cell %}
{% cell %}
domain\_blocked.txt
{% /cell %}
{% /row %}
{% row %}
{% cell %}
URL
{% /cell %}
{% cell %}
url\_allowed.txt
{% /cell %}
{% cell %}
url\_blocked.txt
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Digital Certificate owner
{% /cell %}
{% cell %}
digicert\_owner\_allowed.txt
{% /cell %}
{% cell %}
*(no block list supported)*
{% /cell %}
{% /row %}
{% /table %}

## File Format

Each file - except `digicert_owner_allowed.txt` - can contain single line entries as comma separated data and optional description pairs.

{% code %}
```csv
<data>,<optional description>
```
{% /code %}

Examples:

{% code %}
```csv {% title="md5_allowed.txt" %}
d41d8cd98f00b204e9800998ecf8427e,Known good from internal tool, empty file
d41d8cd98f00b204e9800998ecf8427d
```
{% /code %}

{% callout type="warning" title="Warning" %}
For `digicert_owner_allowed.txt`, description is not supported.
{% /callout %}

Example:

{% code %}
```csv {% title="digicert_owner_allowed.txt" %}
CN="Trusted .Inc", O="Trusted, Inc.", L=San Francisco, ST=California, C=US
```
{% /code %}

## Import Behavior

- Data is **imported at application startup**, **if a file has changed**.
- If a file changes, **existing data for that type and list is replaced entirely**.
- All internal (system-managed) reputation data is updated after installation.
- External (customer) reputation data can be modified and re-imported at any time.

{% callout title="Note" %}
Restart Sandbox to trigger the data import
{% /callout %}

{% code %}
```bash
sudo service sandbox restart
```
{% /code %}

## Validation and Logs

- All entries are **validated** during import based on type.
- **Invalid entries are skipped silently**.
- To ensure full effectiveness, customers advised to **check the logs** for any skipped entries or formatting errors.

Example transform logs for successful import and migration with an invalid data entry:

{% callout type="warning" title="Warning" %}
It is advised to **check the logs** for any skipped entries or formatting errors.
{% /callout %}

```plaintext {% title="Import log" %}
INFO Starting reputation data migration...
INFO External reputation data migration completed successfully
INFO Reloading reputation data from file: /home/akos/workspace/sandbox/fstransform/data/reputation/internal/md5_allowed.txt
INFO Reloaded 1736511 entries from changed file: md5_allowed.txt
 ...
INFO Reloading reputation data from file: <sandbox>/fstransform/data/reputation/internal/ip_blocked.txt
ERROR Failed to parse reputation data line: Invalid IP format. Must be a valid IPv4 or IPv6 address: 212.111.1.212.226
INFO Reloaded 455823 entries from changed file: ip_blocked.txt
INFO Reloading reputation data from file: <sandbox>/fstransform/data/reputation/internal/url_allowed.txt
INFO Reloaded 18 entries from changed file: url_allowed.txt
```

## Migration of Old External Data

- Legacy external reputation data is **automatically migrated** during the first startup after the installation of `version 2.3.0` or later.
- A **migration marker file** indicates completion of the migration step: \<sandbox\>/transform/data/reputation/external/.reputation\_migration\_completed

## Additional Allow List Behavior

- **URL Matching**: A URL is allowed or blocked based on its **domain's** presence in the allow/block list.
- **IP Matching**: An IP is considered **allowed** if it:
  - Matches exactly
  - Is a **network address** - see transform configuration setting `ignoreNetworkIPs`
  - Is a **broadcast** **address** - see transform configuration setting `ignoreBroadcastIPs`
  - Falls within an **allowed subnet** - see transform configuration setting `whitelistHostsCIDR`
