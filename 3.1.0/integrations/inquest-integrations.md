---
type: page
title: InQuest Integrations
listed: false
description: 
index_title: InQuest Integrations
hidden: false
keywords: 
tags: 
---

[InQuest Sandboxapi](https://github.com/InQuest/sandboxapi) is minimal, consistent API for building integrations with malware sandboxes. Now, it has an integration with [MetaDefender Sandbox](https://github.com/InQuest/sandboxapi/tree/master?tab=readme-ov-file#metadefender-sandbox) (previously known as OPSWAT Filescan Sandbox) .

## Usage

Here is an example of how to use it. In order for this sample code to work, it is necessary to paste the API-key in the place of INSERT-YOUR-APIKEY-HERE, as well as a *bad\_file.exe* in the same directory. The default host address is the community site.

{% code %}
```python
import sys
import time
import pprint

from sandboxapi import opswat

# connect to the sandbox
sandbox = opswat.MetaDefenderSandboxAPI("INSERT-YOUR-APIKEY-HERE")

print("Does sandbox available?")
print(sandbox.is_available())

# verify connectivity
if not sandbox.is_available():
    print("sandbox is down, exiting")
    sys.exit(1)

# submit a file
with open("bad_file.exe", "rb") as handle:
    file_id = sandbox.analyze(handle, "bad_file.exe")
    print("file {f} submitted for analysis, id {i}".format(f="bad_file.exe", i=file_id))

# wait for the analysis to complete
while not sandbox.check(file_id):
    print("not done yet, sleeping 10 seconds...")
    time.sleep(10)

# print the report
print("analysis complete. fetching report...")
report = sandbox.report(file_id)
# pprint.pprint(report)
for key, onereport in report.get("reports").items():
    print(
        "Report verdict: {verdict}".format(verdict=onereport["finalVerdict"]["verdict"])
    )
print("Report Score: {score}".format(score=sandbox.score(report)))
```
{% /code %}

The output of the example code:

{% code %}
```bash
Does sandbox available?
True
file bad_file.exe submitted for analysis, id 668ff1c508c0fe0eb961b94c
not done yet, sleeping 10 seconds...
not done yet, sleeping 10 seconds...
not done yet, sleeping 10 seconds...
not done yet, sleeping 10 seconds...
not done yet, sleeping 10 seconds...
analysis complete. fetching report...
Report verdict: MALICIOUS
Report Score: 100
```
{% /code %}

If you would like to use your own host address, modify the constructor:

{% code %}
```python
sandbox = opswat.MetaDefenderSandboxAPI("INSERT-YOUR-APIKEY-HERE","INSERT-YOUR-HOST")
```
{% /code %}

To scanning a zip file, call *analyze*  in this way:

{% code %}
```python
file_id = sandbox.analyze(handle, "bad_file.exe", password="mypassword")
```
{% /code %}

If you would like to scan in a private way, use *is\_private* option:

{% code %}
```python
file_id = sandbox.analyze(handle, "bad_file.exe", is_private=True)
```
{% /code %}

## Compatibility

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[176] %}
Tag
{% /cell %}
{% cell header=true %}
Sandbox 1.9.\*
{% /cell %}
{% cell header=true %}
Sandbox 2.*.*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
v1.1.0 - v1.7.1
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% cell %}
{% badge text="Yes" type="success" /%}
{% /cell %}
{% /row %}
{% /table %}
