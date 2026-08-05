---
type: page
title: How to set a custom API Key for the user profile
listed: true
description: 
index_title: How to set a custom API Key for the user profile
hidden: false
keywords: 
tags: 
---

{% callout title="Check Your Version:" %}
This article applies to MetaDefender Aether (Sandbox) version 3.0.0 and below.
{% /callout %}

Using the same API key across two or more MetaDefender Aether (Sandbox) servers can be beneficial in several scenarios:

- **Simplifies integration** – clients and automation tools only need to manage a single credential
- **Supports load balancing / failover** – enables seamless switching between servers
- **Reduces configuration overhead** – simplifies deployment and ongoing maintenance

This approach is most appropriate when all servers belong to the same environment and operate within the same trust boundary.

## Instructions

**Step 1:**

Log in to the MetaDefender Aether Web UI and create an API Key for the current user.

**User Icon \> My Settings \> API Key \> Create API Key**

{% image url="../../assets/e96949a4d4e4f8735930062d8e2ceab6a62a49a8.png" /%}

Copy the generated API Key.

**Step 2:**

Through the REST API Interface of MetaDefender Aether, using a tool or a library of your choice, send a **POST** request to the **/api/users/api-key/set** endpoint, including the generated key in the **X-Api-Key** Header (for authentication), and the new API Key in the Request Body.

**cURL**:

```plaintext {% showLineNumbers=true %}
curl --request POST \
 --url 'https://<sandbox_url>/api/users/api-key/set' \
 --header 'X-Api-Key: ...aHcbU' \
 --data '{
  "api_key": "...aHcbU0"
}'
```

**Step 3:**

Verify that the change has been successfully applied.

{% image url="../../assets/ef72f2444d7ec1a4778a51a458b4c4cbf64c5c41.png" /%}

{% callout title="Support:" %}
If **Further Assistance** is required, please proceed to log a [**support case or chatting with our support engineer**](https://my.opswat.com/support).
{% /callout %}
