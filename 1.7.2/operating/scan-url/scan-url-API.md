---
type: page
title: Scan URL with API
listed: true
description: 
index_title: Scan URL with API
hidden: false
keywords: 
tags: 
---

You can find the API reference guide: [OPSWAT Filescan API Reference v1](/1.7.2/opswat-filescan/ref). For the following examples we used [Postman](https://www.postman.com/) which is an API platform for building and using APIs.

## Using the default settings

**Step #1** - Start a new request and select "POST"

{% image url="https://uploads.developerhub.io/prod/XX2D/31fltf3qw96j6zzfpgm5dh78it8nvk0wh3j7vdz4tee97ta1vwynr5z267msf62g.png" /%}

**Step #2** - Paste the Filescan URL to the "Enter request URL" field: [https://www.filescan.io/api/scan/url](https://www.filescan.io/api/scan/url)

{% image url="https://uploads.developerhub.io/prod/XX2D/a9csq8r9kshjuzl5flptjxgwozfe4xew9ye0vyj1lyq3xs703litxhsypo7g1krq.png" /%}

**Step #3** - Add the target URL

Under Body tab select form-data.

Add the "url" key and under the value filed paste the URL you want to scan.

{% image url="https://uploads.developerhub.io/prod/XX2D/r1tozjt04w0olv4j9mvxzfd7i9vlk7blu9jmbcc8ansulfe81ktqa2fja7g5od3i.png" /%}

Give some additional parameters if you want.

{% image url="https://uploads.developerhub.io/prod/XX2D/7738qa7x0zsbw1wjaxcql8oytq7ts55md3twpq7qpzqrionux1z2s1xu31gl2wqu.png" /%}

**Step #4** - Send the request with "Send" button

**Step #5** - Copy the "flow\_id"

If your request was success, you will get a similar answer:

{% code %}
```json
{
    "flow_id": "6405c213bfec0852a68fac4b",
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

For the URL paste [*https://www.filescan.io/api/scan/63f633075dc36d90676259c6/report*](https://www.filescan.io/api/scan/63f633075dc36d90676259c6/report)*.*

{% callout type="warning" title="Important!" %}
Change the id beween scan/ and /report to your flow\_id!
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/ubey3jx6aq735rrfymi739qzmyqotqt2xwswoo8z1wxgzpuw64vhtvv6moey8at1.png" /%}

Click on Send button.

If the scan has not finished yet, you should get a similar result:

{% code %}
```json
{
    "flowId": "6405c3f993921fa04236c304",
    "allFinished": false,
    "allFilesDownloadFinished": false,
    "reportsAmount": 1,
    "priority": "max",
    "pollPause": 5,
    "reports": {
        "5e50519e-a02c-4c84-ad17-8fe12c09f5ae": {
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
                "name": "https://www.google.com",
                "hash": "ac6bb669e40e44a8d9f8f0c94dfc63734049dcf6219aac77f02edf94b9162c09",
                "type": null
            },
            "filesDownloadFinished": false,
            "created_date": "03/06/2023, 10:44:11",
            "estimatedTime": "9",
            "estimated_progress": 0.5002222326066759
        }
    }
}
```
{% /code %}

The overallState field in the reports field tells you whether the scan has been completed or not. Wait some seconds and try to get the answer again by clicking the "Send" button. Repeat it until you get "success" state.

{% code %}
```json
{
    "flowId": "6405c213bfec0852a68fac4b",
    "allFinished": true,
    "allFilesDownloadFinished": true,
    "reportsAmount": 1,
    "priority": "max",
    "pollPause": 5,
    "reports": {
        "30176f14-3202-4f38-8873-fe9340ca6c11": {
            "overallState": "success_partial",
            "positionInQueue": 0,
            "finalVerdict": {
                "verdict": "INFORMATIONAL",
                "threatLevel": 0.1,
                "confidence": 1
            },
            "vtRate": -1,
            "file": {
                "name": "https://www.google.com",
                "hash": "ac6bb669e40e44a8d9f8f0c94dfc63734049dcf6219aac77f02edf94b9162c09",
                "type": "other"
            },
            "filesDownloadFinished": true,
            "created_date": "03/06/2023, 10:36:04",
            "estimatedTime": "9",
            "estimated_progress": 1.0
        }
    }
}
```
{% /code %}
