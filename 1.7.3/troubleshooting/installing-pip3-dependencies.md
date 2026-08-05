---
type: page
title: Failed to install pip3 dependencies
listed: true
description: 
index_title: Failed to install pip3 dependencies
hidden: false
keywords: 
tags: 
---

If you encounter the following issue when running the Filescan installation script:

{% code %}
```bash
Fatal error: failed to install additional pip3 dependencies. Exiting...
```
{% /code %}

then very likely, the `pip`  package manager is broken on your Ubuntu installation due to a bug in the `pyopenssl` Python package.

You can find more details in this question: [https://stackoverflow.com/questions/73830524/attributeerror-module-lib-has-no-attribute-x509-v-flag-cb-issuer-check](https://stackoverflow.com/questions/73830524/attributeerror-module-lib-has-no-attribute-x509-v-flag-cb-issuer-check)

First of all, run this command to check if `pip` is in a broken state:

{% code %}
```bash
pip3 --version
```
{% /code %}

When `pip` is broken, the output will be similar to this:

{% code %}
```bash
Traceback (most recent call last):
  File "/usr/bin/pip3", line 11, in <module>
    load_entry_point('pip==20.0.2', 'console_scripts', 'pip3')()
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 490, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2854, in load_entry_point
    return ep.load()
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2445, in load
    return self.resolve()
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2451, in resolve
    module = __import__(self.module_name, fromlist=['__name__'], level=0)
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/main.py", line 10, in <module>
    from pip._internal.cli.autocompletion import autocomplete
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/autocompletion.py", line 9, in <module>
    from pip._internal.cli.main_parser import create_main_parser
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/main_parser.py", line 7, in <module>
    from pip._internal.cli import cmdoptions
  File "/usr/lib/python3/dist-packages/pip/_internal/cli/cmdoptions.py", line 24, in <module>
    from pip._internal.exceptions import CommandError
  File "/usr/lib/python3/dist-packages/pip/_internal/exceptions.py", line 10, in <module>
    from pip._vendor.six import iteritems
  File "/usr/lib/python3/dist-packages/pip/_vendor/__init__.py", line 82, in <module>
    vendored("requests")
  File "/usr/lib/python3/dist-packages/pip/_vendor/__init__.py", line 36, in vendored
    __import__(modulename, globals(), locals(), level=0)
  File "/usr/lib/python3/dist-packages/requests/__init__.py", line 95, in <module>
    from urllib3.contrib import pyopenssl
  File "/usr/lib/python3/dist-packages/urllib3/contrib/pyopenssl.py", line 46, in <module>
    import OpenSSL.SSL
  File "/usr/lib/python3/dist-packages/OpenSSL/__init__.py", line 8, in <module>
    from OpenSSL import crypto, SSL
  File "/usr/lib/python3/dist-packages/OpenSSL/crypto.py", line 1553, in <module>
    class X509StoreFlags(object):
  File "/usr/lib/python3/dist-packages/OpenSSL/crypto.py", line 1573, in X509StoreFlags
    CB_ISSUER_CHECK = _lib.X509_V_FLAG_CB_ISSUER_CHECK
AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'
```
{% /code %}

## Fixing the issue

To fix the broken `pip`, run these commands to remove the `python3-pip`apt\`\` package and install the latest `pip`  from `pypa.io` :

{% code %}
```bash
sudo apt remove python3-pip 
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```
{% /code %}

Please **reboot** your system (or log out and log in again), then check if `pip` is working.

You should see a `pip` version number like this:

{% code %}
```bash
pip3 --version
pip 23.0.1 from /usr/local/lib/python3.8/dist-packages/pip (python 3.8)
```
{% /code %}

It is also recommended to upgrade the `pyopenssl`  package to avoid this issue in the future:

{% code %}
```bash
sudo pip3 install pyopenssl --upgrade
```
{% /code %}

---

If you encounter the following issue when running the Filescan installation script:

{% code %}
```bash
ERROR: Failed building wheel for yara-python
```
{% /code %}

To fix the the issue, run the following command to install yara-python library:

{% code %}
```bash
sudo pip3 install yara-python==4.2.3 --use-pep517
```
{% /code %}
