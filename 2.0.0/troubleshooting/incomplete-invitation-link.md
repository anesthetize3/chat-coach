---
type: page
title: Incomplete invitation link
listed: true
description: 
index_title: Incomplete invitation link
hidden: true
keywords: 
tags: 
---

If you generate an **Invitation link** in the *User Management* menu, the `HOST`  address might be missing after `https://`  protocol. For example:

{% image url="https://uploads.developerhub.io/prod/XX2D/xdpmt9slt5cwp14tsr4vokn0of0lk97gi33xmo2y3tkfa2zn225qoayl4bsyase6.png" /%}

Such a link will not work without the host address, so it is necessary to **add the host manually** before you send the link to the user!

Consider this incomplete link:

```
https:///auth/invite?invite_token=TOKEN
```

For example, if your Sandbox host address is `filescan.mycompany.com` , then the link should be modified as follows:

```
https://filescan.mycompany.com/auth/invite?invite_token=TOKEN
```
