---
type: page
title: How to configure SMTP server on MetaDefender Sanbox to send notification to Gmail mailbox?
listed: true
description: 
index_title: How to configure SMTP server on MetaDefender Sanbox to send notification to Gmail mailbox?
hidden: false
keywords: 
tags: 
---

To be able to send notification to your Gmail mailbox from MetaDefender Sandbox the following fields should be configured properly under MetaDefender Sandbox:

- SMTP\_PORT: smtp.gmail.com
- SMTP\_PORT: 587
- SMTP\_USER: username of the Gmail mailbox used for SMTP integration
- SMTP\_PASS: App password created for Gmail mailbox provided under “Email” field.
- SMTP\_SECURITY: starttls

In order to achieve that, the following configuration should be done on Gmail mailbox account:

1. Create App password for Gmail account

- Login to [https://myaccount.google.com/security](https://myaccount.google.com/security)
- Under "Signing in to Google":

{% image url="../../assets/778f948d3baf6a5c3c433b65c2f8685140e9d144.png" /%}

- Click on Two-Step Verification
- Scroll down to section “App passwords” and click arrow in front of “App passwords”

{% image url="../../assets/4d72dfcdae9d8f108138b4f0881006ad1a60e55c.png" /%}

{% image url="../../assets/feabcd01ed7f7396a016047d52e8d8834f245375.png" /%}

- In new page opened, write a name for your App password and click “Creates”
- Save the App password generated and click “Finished”. Further we will use the App password generated as password for mailbox used for MetaDefender Sandbox configuration as mentioned above and as in below example.

Example:

{% image url="../../assets/72c3556668b377aa4423a5cc33a5d32699ea4949.png" /%}

IMPORTANT: For field “Password” use App password created under Gmail account and not use the password which you use to login on Gmail mailbox.

{% callout title="Support:" %}
If **Further Assistance** is required, please proceed to log a [**support case or chatting with our support engineer**](https://my.opswat.com/support).
{% /callout %}
