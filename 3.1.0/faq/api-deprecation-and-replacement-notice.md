---
type: page
title: API Deprecation and Replacement Notice
listed: true
description: 
index_title: API Deprecation and Replacement Notice
hidden: false
keywords: 
tags: 
---

**Effective Date: 2026-01-26**

To streamline our API and improve performance, we have removed several deprecated API endpoints. All developers should update their applications to use the new corresponding endpoints as soon as possible.

### API Endpoint Updates

The following table lists the deprecated API endpoints and their replacements.

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[338] %}
Deprecated API Endpoint New API Endpoint
{% /cell %}
{% cell header=true %}
Replacement
{% /cell %}
{% /row %}
{% row %}
{% cell %}
/api/feed/atom
{% /cell %}
{% cell %}
/api/feed/reports
{% /cell %}
{% /row %}
{% row %}
{% cell %}
/api/feed/info
{% /cell %}
{% cell %}
/api/feed/reports/info
{% /cell %}
{% /row %}
{% row %}
{% cell %}
/api/feed/archives
{% /cell %}
{% cell %}
/api/archives/samples
{% /cell %}
{% /row %}
{% row %}
{% cell %}
/api/feed/archives/\{publicity\}/\{type\}/\{date\}
{% /cell %}
{% cell %}
/api/archives/samples/\{publicity\}/\{type\}/\{date\}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
/api/admin/reports/\{report\_id\}
{% /cell %}
{% cell %}
/api/users/reports/\{report\_id\}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
/api/users/uploads
{% /cell %}
{% cell %}
/api/reports
{% /cell %}
{% /row %}
{% row %}
{% cell %}
/api/users/me/uploads
{% /cell %}
{% cell %}
/api/me/reports
{% /cell %}
{% /row %}
{% /table %}

### Additional Removals

The backend application and the associated `/api/backend/reputation` endpoint have been removed. This API was unused and had been marked as deprecated.

### Action Required

Please review your code and replace any instances of the deprecated API endpoints with their new counterparts. Continued use of the old endpoints will result in errors.

### Support

If you have any questions or require assistance with these changes, please contact our support team.
