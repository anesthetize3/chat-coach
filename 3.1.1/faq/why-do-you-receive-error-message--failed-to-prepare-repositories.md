---
type: page
title: Why do you receive error message "Failed to prepare repositories"?
listed: true
description: 
index_title: Why do you receive error message "Failed to prepare repositories"?
hidden: false
keywords: 
tags: 
---

{% callout title="Info:" %}
This article applies to all Sandbox versions
{% /callout %}

Issue: While installing the Sandbox, the installer fails at the “prepare repositories” step with:

{% code showLineNumbers=true %}
```html
......
grub2-tools-extra.x86_64        1:2.06-90.el9
grub2-tools-efi.x86_64          1:2.06-90.el9
libldb.x86_64                   2.4.1-1.el9
libldb.x86_64                   2.6.1-1.el9
[FAIL] Failed to prepare repositories.
Exiting
```
{% /code %}

Even though the system has internet access and the repos are functional.

### Cause

The script **install.sh** uses `dnf check-update` to verify repositories. However, this command returns:

- `0`: No updates available (success)
- `100`: Updates available (still success)
- `>1`: Real error

The script only treats `0` as success, so it fails when updates are available (`100`).

### Solution

## **Ensure that you have followed these steps before running the installer:**

### Step 1: Install EPEL (if needed)

{% code showLineNumbers=true %}
```html
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm -y
```
{% /code %}

### Step 2: (Optional) Create sandbox user

{% code showLineNumbers=true %}
```html
sudo useradd --create-home sandbox
sudo passwd -l sandbox
```
{% /code %}

### Step 3: Install tools like 7zip

{% code showLineNumbers=true %}
```html
sudo dnf update -y
sudo dnf install p7zip -y
```
{% /code %}

## **(Optional) Fix the script logic to allow both 0 and 100:**

{% code showLineNumbers=true %}
```html
dnf check-update ${DNF_OPTIONS}
result=$?

if [ "$result" -eq 0 ] || [ "$result" -eq 100 ]; then
    success "Successfully prepared repositories"
else
    fatal "Failed to prepare repositories."
fi
```
{% /code %}

## Result:

{% image url="https://uploads.developerhub.io/prod/XX2D/z4887kg0ma0m9ygk49quo3jv6zhy9tffdxw66oyekrjq95bepepqifj12s40bf9t.png" /%}

{% callout title="Support:" %}
If you require further assistance, please follow these instructions on [How to Create Support Package?](https://www.opswat.com/docs/mdcore/troubleshooting/how-to-create-support-package-), before [creating a support case or chatting with our support engineer](https://my.opswat.com/support).
{% /callout %}
