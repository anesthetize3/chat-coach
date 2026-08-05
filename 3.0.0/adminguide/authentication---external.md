---
type: page
title: Authentication - external
listed: true
description: 
index_title: Authentication - external
hidden: true
keywords: 
tags: 
---

Under the **Admin panel \>** **Settings \> Authentication** menu, you can configure and customize the authentication methods for your application to ensure the necessary level of security. This menu provides options for both integrating external authentication services and tweaking local authentication settings.

{% image url="../../assets/49166e37dfa0c48b4b174e1f541620377a456189.png" /%}

{% image url="../../assets/a811b7e25f3f3d2a9bab63cfd499e3d2655363a1.png" /%}

## OAuth 2.0

To add a new authentication method, click the **+ Add service** button.

{% image url="../../assets/8e00f57a63a6da36d440054949a8c4e76c7e2c09.png" /%}

When adding a service, the following settings can be specified:

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[244] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Name
{% /cell %}
{% cell %}
As service will be displayed to users
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Home page
{% /cell %}
{% cell %}
You can specify which page should be the home page
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Client ID
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Client secret
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Order
{% /cell %}
{% cell %}
The order of authentication can be specified
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Active
{% /cell %}
{% cell %}
Enable or disable the authentication
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Base URL
{% /cell %}
{% cell %}
Service endpoint to get information about OAuth API
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Path
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Service Key
{% /cell %}
{% cell %}
Is used internally in our app and in redirect URI
{% /cell %}
{% /row %}
{% /table %}

{% callout type="warning" title="Note" %}
Service Key is not editable after creation!
{% /callout %}

To modify an existing authentication method, click on its name. This will display the associated settings, which can be saved after making changes by clicking the save button.

{% image url="https://uploads.developerhub.io/prod/XX2D/dmu87rvayhy1p0balgyr0bb6y2h49mhxvnzqsj4dzbefiszcdyl986jk4c0hcaf0.png" /%}

## Security

Under the Security tab, you can set the required password strength and the validation of usernames.

{% image url="https://uploads.developerhub.io/prod/XX2D/8lkqelcsw18ww8stp4l1v6eac0wiu32t95qxaswk4bigyjpeet2ekisadks8ofqm.png" /%}

The following fields can be customized regarding password strength:

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[284] %}
Field
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Minimum length
{% /cell %}
{% cell %}
Minimum password length
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Special characters
{% /cell %}
{% cell %}
Requirement for special characters
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Mixed case
{% /cell %}
{% cell %}
Requirement for mixed case
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Alphanumeric
{% /cell %}
{% cell %}
Requirement for alphanumeric characters
{% /cell %}
{% /row %}
{% /table %}

Under username validation, a regular expression can be specified to describe acceptable usernames.
