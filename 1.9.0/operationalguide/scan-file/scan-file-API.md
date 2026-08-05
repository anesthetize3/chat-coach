---
type: page
title: Scan file with API
listed: true
description: 
index_title: Scan file with API
hidden: true
keywords: 
tags: 
---

You can find the API reference guide: [OPSWAT Filescan API Reference v1](/filescan/1.8.0/opswat-filescan/ref). For the following examples we used [Postman](https://www.postman.com/) which is an API platform for building and using APIs.

## Using the default settings

**Step #1** - Start a new request and select "POST"

{% image url="https://uploads.developerhub.io/prod/XX2D/31fltf3qw96j6zzfpgm5dh78it8nvk0wh3j7vdz4tee97ta1vwynr5z267msf62g.png" /%}

**Step #2** - Paste the Filescan URL to the "Enter request URL" field: [https://www.filescan.io/api/scan/file](https://www.filescan.io/api/scan/file)

{% image url="https://uploads.developerhub.io/prod/XX2D/cq5k8i96spnzvslkntsq9xdkb1k02ozz4cyex61gl8ropm65o7i4kusvpwvijac1.png" /%}

**Step #3** - Upload the file and set parameters

Under Body tab select form-data.

Add a "file" key and change the type to "File".

Under the value filed select the target file.

{% image url="https://uploads.developerhub.io/prod/XX2D/evlicjm8dk0q96wc2rjey16x04u70ujzo8fs9pfnu0uxoszeoryllo94019vyrhg.png" /%}

Give some additional parameters if you want.

{% image url="https://uploads.developerhub.io/prod/XX2D/m5gmw9cg36dhyh7jhvgoc2c2xc42jta5cf3kgvtcwfqmhxqr4k6jvtialtjgtoqr.png" /%}

**Step #4** - Send the request with "Send" button

**Step #5** - Copy the "flow\_id"

If your request was success, you will get a similar answer:

{% code %}
```json
{
    "flow_id": "63f633075dc36d90676259c6",
    "priority": {
        "applied": 100,
        "max_possible": 100
    }
}
```
{% /code %}

Copy the "flow\_id" which is neccessary to polling the scan result.

**Step #6** - Get the result

Open a new request page and select the "GET" method (it's the default).

For the URL paste *\[\_\_[https://www.filescan.io/api/scan/\_63f633075dc36d90676259c6](https://www.filescan.io/api/scan/_63f633075dc36d90676259c6)*/report\_\]([https://www.filescan.io/api/scan/63f633075dc36d90676259c6/report](https://www.filescan.io/api/scan/63f633075dc36d90676259c6/report))*.*

{% callout type="warning" title="Important!" %}
Change the id beween scan/ and /report to your flow\_id!
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/w6ahebs4gn7qugv3uzpwskht3tina9eucpiqichclxneqcwx7wxfvjx0fvxcum4p.png" /%}

Click on Send button.

If the scan has not finished yet, you should get a similar result:

{% code %}
```json
{
    "flowId": "63f633075dc36d90676259c6",
    "allFinished": false,
    "allFilesDownloadFinished": false,
    "reportsAmount": 1,
    "priority": "max",
    "pollPause": 5,
    "fileSize": 13370880,
    "fileReadProgressBytes": 13370880,
    "reports": {
        "d59e12bb-f599-4dfa-b682-253a5dacf564": {
            "overallState": "in_progress",
            "positionInQueue": 0,
            "finalVerdict": {
                "verdict": "UNKNOWN",
                "threatLevel": 0,
                "confidence": 1
            },
            "filter_errors": [
                "Path not found: ['vtRate']"
            ],
            "file": {
                "name": "bad_file.exe",
                "hash": "834d1dbfab8330ea5f1844f6e905ed0ac19d1033ee9a9f1122ad2051c56783dc",
                "type": null
            },
            "filesDownloadFinished": false,
            "created_date": "02/22/2023, 16:01:29",
            "estimatedTime": "2",
            "estimated_progress": 1.0
        }
    }
}
```
{% /code %}

The overallState field in the reports field tells you whether the scan has been completed or not. Wait some seconds and try to get the answer again by clicking the "Send" button. Repeat it until you get "success" state.

{% code %}
```json
{
    "flowId": "63f63c57a6ba2f75a97a1f81",
    "allFinished": true,
    "allFilesDownloadFinished": true,
    "reportsAmount": 1,
    "priority": "max",
    "pollPause": 5,
    "fileSize": 13370880,
    "fileReadProgressBytes": 13370880,
    "reports": {
        "d59e12bb-f599-4dfa-b682-253a5dacf564": {
            "overallState": "success",
            "positionInQueue": 0,
            "finalVerdict": {
                "verdict": "MALICIOUS",
                "threatLevel": 1,
                "confidence": 1
            },
            "vtRate": -1,
            "file": {
                "name": "bad_file.exe",
                "hash": "834d1dbfab8330ea5f1844f6e905ed0ac19d1033ee9a9f1122ad2051c56783dc",
                "type": "pe"
            },
            "filesDownloadFinished": true,
            "created_date": "02/22/2023, 16:01:29",
            "estimatedTime": "2",
            "estimated_progress": 1.0
        }
    }
}
```
{% /code %}
