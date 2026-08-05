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

In order to reset the password of any user (without using the Forgot Password option) an SSH access is needed to the server which is running Filescan. **Please use this only as a last resort when the administrator password is lost. Changing the password for other users are possible from the administrator menu.** After logging into the server via SSH, the following steps are needed to set the password of an arbitrary user:

### Step 1.

Navigate to the installation directory (usually: /home/filescanio/FileScanIO) and check if you are in the correct folder by issuing the ls command. You should see that the current folder contains the launch\_webservice.sh and shutdown\_ webservice.sh files.

{% code %}
```bash
cd /home/filescanio/FileScanIO
ls
```
{% /code %}

### Step 2.

Create a simple text file called email.txt and insert the email address of the user you want to reset its password. Also create a simple text file called password.txt and insert the new password for the user. Make sure the password fulfills the requirements (you can check it on the registration page).

{% code %}
```bash
echo admin@opswat.com > email.txt
echo Newpassword:1 > password.txt
```
{% /code %}

### Step 3.

Shutdown the webservice and wait until shutdown is complete. Start the webservice.

{% code %}
```bash
./shutdown_webservice.sh
./launch_webservice.sh
```
{% /code %}

The email.txt and password.txt files should disappear and now you should be able to login with the new credentials.
