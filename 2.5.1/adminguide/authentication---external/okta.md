---
type: page
title: Okta
listed: true
description: 
index_title: Okta
hidden: false
keywords: 
tags: 
---

Below you can find a step by step tutorial on how to integrate Okta with MetaDefender Sandbox using the OpenID Connect protocol.

## [Prepare the MetaDefender Sandbox for the OAuth integration](https://www.opswat.com/docs/filescan/adminguide/microsoft-entra#prepare-the-metadefender-sandbox-for-the-oauth-integration)

Let’s prepare the SSO settings in MetaDefender Sandbox as follows:

1. Go to **Admin panel \>** **Settings \> Authentication** on MetaDefender Sandbox page.
2. Click on **+ Add Service** button
3. Fill in the **Name** (e.g. "Okta") and **Service key** (should be **"okta**") values
4. **Do NOT click Save yet**, the remaining values will be filled in later
5. Please note down the **Redirect** **URI** at the bottom of the form

{% image url="https://uploads.developerhub.io/prod/XX2D/ucra8e5artdiiqmupwvlbzs47juio199o4tpmgsd2d973vswvzzcofp2cgi76m4a.png" /%}

## [Register application in Okta](https://www.opswat.com/docs/filescan/adminguide/microsoft-entra#register-application-in-microsoft-entra-id)

1. Sign into Okta and navigate to admin dashboard
2. Go to **Applications** and select **Create App Integration**

{% image url="https://uploads.developerhub.io/prod/XX2D/5bfvx23pe6196cccix8bxj788zbr8ybige1hn65p4hh7l9j543una6uz5luhfht4.png" width=1000 /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/2o9bfaa3o56wveqktmqrqponha4ubzf18f7vmxshl7k288kiejpswksc31f6bhzy.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/sxa35fzi74wim06ksv9m7kdd22i9v7mlyk1hpxr58nkava5cjj1msuice2f9r0ic.png" /%}

Please copy the Client ID and client secrets from the newly created application.

{% image url="https://uploads.developerhub.io/prod/XX2D/3plcc7j2nqlsgz79p12n60jo6zoqdul9oclyd7fv9eihcluyac76oiyw3ewee4jm.png" /%}

## [Configure MetaDefender Sandbox for Okta SSO](https://www.opswat.com/docs/filescan/adminguide/microsoft-entra#configure-metadefender-sandbox-for-entra-id-sso)

Let’s finish the configuration of the MetaDefender Sandbox SSO settings using the information collected above:

1. Go back to the MetaDefender Sandbox UI
2. Fill the form details for the newly created service using the reference below
3. **Save the form**

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[162] %}
Field
{% /cell %}
{% cell header=true colwidth=[351] %}
Description
{% /cell %}
{% cell header=true %}
Example
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Name
{% /cell %}
{% cell %}
Integration name
{% /cell %}
{% cell %}
Okta
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Home page
{% /cell %}
{% cell %}
First page after log in
{% /cell %}
{% cell %}
[https://sandbox.mycompany.com](https://sandbox.mycompany.com)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Client ID
{% /cell %}
{% cell %}
Application (client) ID , comes from Okta
{% /cell %}
{% cell %}
1234-5678-90123-4567
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Client secret
{% /cell %}
{% cell %}
Comes from Okta
{% /cell %}
{% cell %}
abcd1234!%#
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Order
{% /cell %}
{% cell %}
The order of authentication can be specified
{% /cell %}
{% cell %}
1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Active
{% /cell %}
{% cell %}
Enable or disable the authentication
{% /cell %}
{% cell %}
on
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Use state
{% /cell %}
{% cell %}
**Generate and validate OIDC state parameter - must be enabled for Okta**
{% /cell %}
{% cell %}
**on**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Base URL
{% /cell %}
{% cell %}
Service base url
{% /cell %}
{% cell %}
[**https://mycompany.okta.com**](https://login.microsoftonline.com)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Path
{% /cell %}
{% cell %}
Service URL postfix. Format should be:
{% /cell %}
{% cell %}
/.well-known/openid-configuration
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Service Key
{% /cell %}
{% cell %}
Is used internally in our app and in redirect URI
{% /cell %}
{% cell %}
okta
{% /cell %}
{% /row %}
{% /table %}

{% image url="https://uploads.developerhub.io/prod/XX2D/46fw3zd3jztz7vppfzokjgruo5jj5avv0ttbtzru3ktyny0m5inpk5yk5uu9xcii.png" /%}

## [Testing the integration](https://www.opswat.com/docs/filescan/adminguide/microsoft-entra#testing-the-integration)

1. Log out of MetaDefender Sandbox
2. You will notice that there is a new **Sign In with Okta** button on the login page

{% image url="https://uploads.developerhub.io/prod/XX2D/ir8k1v2b38i30xvguq0a8ukrb1hry7ibbwcdaooeebhtzhpi6glo9synh2lcxsh6.png" /%}
