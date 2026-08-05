---
type: page
title: Password reset
listed: true
description: 
index_title: Password reset
hidden: true
keywords: 
tags: 
---

If you lost your Filescan admin credentials, you can follow the steps below to reset your password.

{% callout type="warning" title="Note" %}
You need the email address of your Filescan user for the password reset!
{% /callout %}

Please log in to your Filescan instance (via SSH), and start a bash shell in the `fsio` docker container:

{% code %}
```bash
docker exec -it fsio /bin/bash
```
{% /code %}

Go to the `src/scripts`  folder and check if the `set_password.py` script is already present there:

{% code %}
```bash
cd src/scripts
cat set_password.py
```
{% /code %}

If you see the following output, you can skip to the next step:

{% code %}
```python
import sys
import asyncio
from loguru import logger
from typing import Union

from layout.wrapper import script_wrapper

from fsio.lib.container.main import container
from fsio.settings import DEFAULT_GROUPS_IDS
from fsio.db import DbEngine
from apps.users.models import User
from apps.auth.lib.auth.auth import Auth
from apps.auth.lib.validation import ValidateAuth
from apps.admin.lib.settings_getter import AdminSettingsGetter

"""Make user an admin by email"""

async def set_password(email: str, password: str):
    if email is None:
        logger.error('Please provide user email')
        return

    if password is None:
        logger.error('Please provide new password')
        return

    auth: Auth = container.get(Auth)
    settings: AdminSettingsGetter = container.get(AdminSettingsGetter)
    validation: ValidateAuth = container.get(ValidateAuth)
    db: DbEngine = container.get(DbEngine)

    collection = db.get_collection(User)
    user = await collection.find_one({'email': email})
    if not user:
        logger.error('User not found')
        return

    auth_settings = await settings.get('auth')
    error = validation.validate_password(password, password, auth_settings['password'])
    if error:
        logger.error(error)
        return

    await collection.update_one(
        {'email': email},
        {'$set': {'password': auth.get_password_hash(password)}}
    )
    logger.info('New password is set')


if __name__ == '__main__':
    email = sys.argv[1]
    password = sys.argv[2]
    asyncio.run(script_wrapper(set_password, email, password))
```
{% /code %}

If the script is not present or incomplete, please copy-paste the contents above and create the file using a text editor:

{% code %}
```bash
nano set_password.py
```
{% /code %}

Save the script when you exit `nano`!

Please substitute the email address and the desired new password and execute the script like this:

{% callout type="warning" title="Warning" %}
**Keep in mind that the password should be within single quotes and it must contain NUMBERS, LOWERCASE and UPPERCASE letters!**
{% /callout %}

{% code %}
```bash
python set_password.py <email> '<password>'
```
{% /code %}

If the password does not meet the requirements, you will see an error message like this:

{% code %}
```groovy
root@92ba42286801:/app/src/scripts# python set_password.py user@company.com 'badpassword'
2023-05-23 19:01:19.982 | INFO     | layout.wrapper:script_wrapper:16 - --- Init services needed for script ---
2023-05-23 19:01:19.990 | INFO     | fsio.lib.cache.base:connect:24 - Creating pool for redis cache
2023-05-23 19:01:19.992 | INFO     | layout.wrapper:script_wrapper:18 - --- Done init services. Starting script ---
2023-05-23 19:01:19.998 | ERROR    | __main__:set_password:44 - Password should contain numbers, lowercase and uppercase letters
2023-05-23 19:01:19.998 | ERROR    | __main__:set_password:44 - Password should contain numbers, lowercase and uppercase letters
2023-05-23 19:01:19.998 | ERROR    | __main__:set_password:44 - Password should contain numbers, lowercase and uppercase letters
2023-05-23 19:01:19.998 | INFO     | layout.wrapper:script_wrapper:20 - --- Script completed. Shutdown and cleanup ---
2023-05-23 19:01:20.004 | INFO     | fsio.lib.cache.base:disconnect:38 - Disconnecting from redis cache
```
{% /code %}

If everything works fine, you will see `New password is set` :

{% code %}
```groovy
root@92ba42286801:/app/src/scripts# python set_password.py user@company.com 'BeTTerPassWord4984'
2023-05-23 19:01:37.449 | INFO     | layout.wrapper:script_wrapper:16 - --- Init services needed for script ---
2023-05-23 19:01:37.456 | INFO     | fsio.lib.cache.base:connect:24 - Creating pool for redis cache
2023-05-23 19:01:37.458 | INFO     | layout.wrapper:script_wrapper:18 - --- Done init services. Starting script ---
2023-05-23 19:01:37.705 | INFO     | __main__:set_password:51 - New password is set
2023-05-23 19:01:37.706 | INFO     | layout.wrapper:script_wrapper:20 - --- Script completed. Shutdown and cleanup ---
2023-05-23 19:01:37.707 | INFO     | fsio.lib.cache.base:disconnect:38 - Disconnecting from redis cache
```
{% /code %}
