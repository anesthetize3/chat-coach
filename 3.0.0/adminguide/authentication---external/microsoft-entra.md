---
type: page
title: Microsoft Entra
listed: true
description: 
index_title: Microsoft Entra
hidden: false
keywords: 
tags: 
---

Below you can find a step-by-step tutorial on how to integrate Microsoft Azure Active Directory with MetaDefender Aether using the OpenID Connect protocol.

{% callout title="Info" %}
**Prerequisites**: An Entra Tenant (quick guide: [https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant) )
{% /callout %}

## Prepare the MetaDefender Sandbox for the OAuth integration

Let’s prepare MetaDefender Aether SSO settings as follows:

1. Go to **Admin panel \>** **Settings \> Authentication** on the MetaDefender Aether page.
2. Click on **+ Add Service** button
3. Fill in the **Name** (e.g., "MS Entra") and **Service key** (should be **"entra**") values
4. **Do NOT click Save yet**; the remaining values will be filled in later
5. Please note down the **Redirect** **URI** at the bottom of the form

{% image url="../../../assets/56394cf11f3ce4b5535076f08c9a28ae27defdc7.png" /%}

## Register application in Microsoft Entra ID

1. Sign into Microsoft Entra ID and navigate to the admin dashboard
2. Go to **App registrations** and select **New registration**

{% image url="https://uploads.developerhub.io/prod/XX2D/s1g8e2rfah8gwztklxzcg5ac2vxss2nx6qzcv9xyb90q95ilww36imxjwoqq48ox.png" /%}

3. Let’s configure the application settings.
   1. Give the application a name. for example, “MetaDefender Aether”. In the following examples, we will use "OPSWAT Sandbox - Staging" as the application name
   2. Configure the **Redirect URI** (`https://<host>:<port>/`auth/signin/\<service\_key\>/callback) - Use the value you noted down in the previous section.

{% callout type="warning" title="Warning" %}
*Microsoft Entra ID* supports only **HTTPS** protocol for redirect URI
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/j82rpa1kddsas5m3jy3rqsq1omxg8jr992xqbnz8gq850fphrsska0o3c0nzafn6.png" /%}

4. Note down **Application (client) ID** and **Directory (tenant) ID** of the newly created application as it will be needed in a later step

## Generate Secret key for Entra ID SSO

Go to **Certificates \& Secrets** and generate a new **client secret** string (also referred to as an application password). Record the client secret.

{% callout type="warning" title="Warning" %}
You will not be able to retrieve **client secret** at a later time because it will be hidden. You need to generate a new secret in this case.
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/yiqe925ajapi03ony6ll2ru66n4h8582adxe4uc3pdvgeaweu38peedsmxy5ptnk.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/4hko1n50ow54251cyc60gdbg8d2unrge2bpzky4ry3uil7d30mgp4b29hj2rhpue.png" /%}

## Configure MetaDefender Sandbox for Entra ID SSO

Let’s finish the configuration of the MetaDefender Aether SSO settings using the information collected above:

1. Go back to the MetaDefender Aether UI
2. Fill in the form details for the newly created service using the reference below
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
MS Entra
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
Application (client) ID , comes from Entra
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
Comes from Entra
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
Base URL
{% /cell %}
{% cell %}
Service base url
{% /cell %}
{% cell %}
[**https://login.microsoftonline.com**](https://login.microsoftonline.com)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Path
{% /cell %}
{% cell %}
Service URL postfix. Format should be:

**/\<tenant\_id\>/v2.0/.well-known/openid-configuration**

Tenant id comes from Entra: Directory (tenant) id
{% /cell %}
{% cell %}
**/*12314*/v2.0/.well-known/openid-configuration**
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
entra
{% /cell %}
{% /row %}
{% /table %}

{% image url="https://uploads.developerhub.io/prod/XX2D/bf1nl22ywnbscond4lfvlbu1gupy1o514wrggy0o7iy8uawrm4my2qxwbe8krjfi.png" /%}

## Login as an Entra organization admin

Depending on Entra ID configuration, and organization admin should approve/allow a new application beforehand.

Log in to MetaDefender Aether SSO with the Entra ID administrative account and accept the newly created application:

{% image url="https://uploads.developerhub.io/prod/XX2D/5rcce5xw0fj6758zr3vneavie797zg23egty4vfadq3h6lyg4espjgvef68obu81.png" /%}

{% image url="https://uploads.developerhub.io/prod/XX2D/o4b77xymnbmtfkt7iem41o8sm3aczr8n5ay26k0dgva6a9jszmxubg5sdflphm21.png" /%}

## Testing the integration

1. Log out of MetaDefender Aether
2. You will notice that there is a new **Sign In with SSO** button on the login page

{% image url="https://uploads.developerhub.io/prod/XX2D/a4630kbg602ki819bt88hqzkwl1yp2tfr8l35q6cr4h5sr4neffcz2bel6e9k05i.png" /%}

3. Click Sign In with SSO. You should be redirected to Microsoft Entra ID to login. Once logged in, you will be redirected back to MetaDefender Aether and automatically logged in.

{% callout type="warning" title="Warning" %}
In some cases, the following warning might be displayed even though the login is successful. This is a known issue and will be fixed in the next version of the product.
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/3sr8l7pyxe46t2xhv4xqut9hbl1ukwl4kod1m9zamwjt1sbrushuqy5s2mdbouq3.png" /%}
