---
type: page
title: Scan API Endpoint
listed: true
description: 
index_title: Scan API Endpoint
hidden: true
keywords: 
tags: 
---

This API endpoint allows users to submit a file or archive that will get converted into one or multiple (in the case of archives with multiple files) tasks. The list of accepted files for processing are returned in the "acceptedFiles" array, files with unsupported file type (or rejected for another reason, e.g. because they are too large) will be found in the "rejectedFiles" array. The call is asynchronous and will return immediately. Using the submission ID, the execution status and results can be retrieved later via the /submit-result or /task endpoints.

#### Syntax

`POST https://<ip>:<port>/submit`

#### Parameters

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[179] %}
Name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Required?
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
secret
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Y
{% /cell %}
{% cell %}
Authentication secret
{% /cell %}
{% /row %}
{% row %}
{% cell %}
priority
{% /cell %}
{% cell %}
Integer
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Processing priority (0 = default, 100 = highest)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
password
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Archive password
{% /cell %}
{% /row %}
{% row %}
{% cell %}
skipWhitelistedFiles
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Reject submitted files, if their hash (MD5/SHA-256) is on an internal or external whitelist
{% /cell %}
{% /row %}
{% row %}
{% cell %}
transformOpt.\[option\]
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
Set custom transform options that differ from the default backend configuration.

Available options:

- rapidMode
- runOSINTLookups
- runExtendedOSINTLookups
- runOSINTLookupsOnExtractedFiles
- runFileVisualizer
- runFileDownloaders
- runDomainResolver
- runYaraRulesOnInputFile
- runYaraRulesOnExtractedFiles
- runWhoisRecordLookups
- runIPStackLookupOnExectractedHosts
- runTesseractOCRForImages

*Note: rapidMode sets an even extended set of options to fully optimize for speed. It will override any other option, if enabled*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
$\_FILE
{% /cell %}
{% cell %}
Octet-Stream
{% /cell %}
{% cell %}
Y
{% /cell %}
{% cell %}
File/Archive as form-data body
{% /cell %}
{% /row %}
{% row %}
{% cell %}
url
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
N
{% /cell %}
{% cell %}
URL to file
{% /cell %}
{% /row %}
{% /table %}

#### Example Response

{% code %}
```json
{
    "acceptedFiles":
    [
        {
            "ID": "fff5ae43-5008-4e40-8574-eab7e201434b",
            "submitName": "EMOTET.doc",
            "sha256": "c52f09e474c5d9b316e0b8e5e839282e52268a79b03bef1cefaaee4c2cec793e",
            "mediaType":
            {
                "string": "application/x-tika-msoffice",
                "slash": 11,
                "semicolon": 27,
                "parameters":
                {}
            },
            "priority": 1,
            "positionInQueue": 0
        }
    ],
    "rejectedFiles":
    [],
    "submitWarnings":
    []
}
```
{% /code %}

*Note: if a file gets rejected, appropriate data will be presented in the "rejectedFiles" array including a "rejectedReason" field.*

{% code %}
```json
{
    "processTime": 18,
    "acceptedFiles":
    [],
    "rejectedFiles":
    [
        {
            "submitName": "9db9ff48cf728fdfd86e627e313869c81ca2d8a36800e88078817aa88794a4a9_5d-16d29c-cddf-46ee-8f4d-76718608e408",
            "priority": 0,
            "positionInQueue": -1,
            "rejectedReason": "ARCHIVE_ZIPBOMB",
            "isSourceFile": false
        },
        {
            "ID": "5d16d29c-cddf-46ee-8f4d-76718608e408",
            "submitName": "filename",
            "sha256": "9db9ff48cf728fdfd86e627e313869c81ca2d8a36800e88078817aa88794a4a9",
            "mediaType":
            {
                "string": "application/zip",
                "slash": 11,
                "semicolon": 15,
                "parameters":
                {}
            },
            "priority": 100,
            "positionInQueue": -1,
            "rejectedReason": "ARCHIVE",
            "isSourceFile": true
        }
    ],
    "submitWarnings":
    []
}
```
{% /code %}

Possible values for “rejectedReason”:

- EMPTY\_FILE
- TOO\_LARGE\_FILE
- DIRECTORY
- ARCHIVE\_UNPACKED
- ARCHIVE\_INVALID
- ARCHIVE\_ENCRYPTED
- ARCHIVE\_ZIPBOMB
- INVALID\_PASSWORD
- UNSUPPORTED\_FILE\_FORMAT
- SERVER\_FULL
- INTERNAL\_ERROR
- WHITELISTED

---

**fsTransform Scan API Endpoint**

This API endpoint allows users to submit a file that will get converted into one task. The call is asynchronous and will return immediately. Using the task ID, the execution status and results can be retrieved later via the /task endpoint.

#### Syntax

`POST https://<ip>:<port>/scan`

#### Example Response

{% code %}
```json
{
    "processTime": 899,
    "scanTasks":
    [
        {
            "taskReference":
            {
                "name": "transform-file",
                "additionalInfo":
                {
                    "submitName": "file",
                    "digests":
                    {
                        "SHA-256": "99f8505240fff0831382ddf692f83750844887047ef90f59034d34d857271608"
                    },
                    "callbackDeleteAfter": false
                },
                "ID": "1fd6d36c-5909-498e-9351-ba8080e5c530",
                "state": "IN_PROGRESS",
                "opcount": 0,
                "processTime": 0
            },
            "opcount": 0,
            "processTime": 0,
            "taskWarnings":
            [],
            "allTags":
            [],
            "allSignalGroups":
            [],
            "resources":
            {}
        }
    ]
}
```
{% /code %}
