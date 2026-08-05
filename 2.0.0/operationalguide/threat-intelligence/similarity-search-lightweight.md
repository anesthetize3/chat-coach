---
type: page
title: Similarity Search reduced feature list
listed: false
description: 
index_title: Similarity Search reduced feature list
hidden: true
keywords: 
tags: 
---

{% callout type="success" title="Upgrade" %}
Enhancements to Similarity Search now include support for all file types, improved speed, accuracy, and additional features for PE, resulting in an overall enhanced analysis experience.
{% /callout %}

## Portable Executable type

These features are carefully selected based on their ability to provide accurate and relevant results, and they are continuously updated to stay current with the latest malware trends and techniques.

{% callout type="warning" title="Info" %}
Similarity search is applicable in numerous fields(close to 90 for PE-s), but due to security reasons, we prefer not to disclose all of them. However, here are a few examples:
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[392] %}
**Feature group**
{% /cell %}
{% cell header=true %}
**Number of features**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Binary metadata
{% /cell %}
{% cell %}
16
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Certificates
{% /cell %}
{% cell %}
5
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Characteristic
{% /cell %}
{% cell %}
2
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Disassembly sections
{% /cell %}
{% cell %}
2
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DotnetInfo
{% /cell %}
{% cell %}
17
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Header info
{% /cell %}
{% cell %}
11
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted
{% /cell %}
{% cell %}
10
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Threat indicators
{% /cell %}
{% cell %}
2
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Pdb guid
{% /cell %}
{% cell %}
1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Resources
{% /cell %}
{% cell %}
4
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Rich header compiler Ids
{% /cell %}
{% cell %}
1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sections
{% /cell %}
{% cell %}
3
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Strings
{% /cell %}
{% cell %}
1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Imports
{% /cell %}
{% cell %}
2
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Version info
{% /cell %}
{% cell %}
7
{% /cell %}
{% /row %}
{% /table %}

### Some of the features are:

{% tabs %}
{% tab title="Binary metadata" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[270] %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Language
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
What speaking language does the binary target
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Entry point section name
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Name of the section where the entry point of the PE resides. It’s a calculated value, based on the supplied entry point address \& section details.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Total imported functions
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Indicates the number of imported functions in a PE
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Digital signature verification
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Whether the digital signature is verified or not.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Certificates" %}
{% table layout="auto" %}
{% row %}
{% cell header=true %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Certificate is Valid
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Shows whether the associated certificate is valid or not
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Characteristic" %}
{% table layout="auto" %}
{% row %}
{% cell header=true %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
File characteristic
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Characteristics defining the behavior of the PE
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DLL characteristic
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Features which make a PE actually portable in memory
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Disassembly sections" %}
{% table layout="auto" %}
{% row %}
{% cell header=true %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Disassembly Human descriptor
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Indicates a Human description of a disassembly part of a PE
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Disassembly  Instruction Count
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Indicates  the number of instruction of a disassembly part of a PE
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Dotnet info" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[160] %}
Field name
{% /cell %}
{% cell header=true colwidth=[120] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Dotnet
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Whether the executable file is using the .NET framework
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Stream names
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Descriptive identifiers for data streams within a .NET application, facilitating organized data management and manipulation.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Header info" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[160] %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Image base
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
“Base” address used if relocation doesn’t happen
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Nxcompat
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Indicator whether NX compatibility (Data Execution Prevention *\[No eXecute\]*) is enabled at compilation time.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SEH
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Indicator whether SEH (Structured Exception Handler) is enabled at compilation time.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Extracted" %}
{% table layout="auto" %}
{% row %}
{% cell header=true %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted Urls
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted URLs from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted MD5 Hashes
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted MD5 from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted SHA-1 Hashes
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted SHA-1 from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted SHA-256 Hashes
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted SHA-256 from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted SHA-512 Hashes
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted SHA-512 from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted E-mails
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted Emails from the file
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Threat Indicators" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[265] %}
Field name
{% /cell %}
{% cell header=true colwidth=[3] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Threat Indicators
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
An identifier to show what kind of rules (Threat indicator) Metadefender Sandbox itself matched on the target file. It can contain more info than what is present in the actual report
{% /cell %}
{% /row %}
{% row %}
{% cell %}
MITRE Techniques
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
An identifier to show what kind of rules (MITRE) Metadefender Sandbox itself matched on the target file. It can contain more info than what is present in the actual report
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}
{% /tabs %}

## All file type

{% callout type="warning" title="Info" %}
Similarity search is applicable in numerous fields(close to 120 for all file types), but due to security reasons, we prefer not to disclose all of them. However, here are a few examples:
{% /callout %}

These features are carefully selected based on their ability to provide accurate and relevant results, and they are continuously updated to stay current with the latest malware trends and techniques.

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[400] %}
Feature group
{% /cell %}
{% cell header=true %}
**Number of features**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Apk
{% /cell %}
{% cell %}
22
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Biffopcodes
{% /cell %}
{% cell %}
1
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Emulation
{% /cell %}
{% cell %}
14
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted
{% /cell %}
{% cell %}
10
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extended data
{% /cell %}
{% cell %}
24
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Metadata
{% /cell %}
{% cell %}
15
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Segments
{% /cell %}
{% cell %}
6
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sections
{% /cell %}
{% cell %}
6
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Strings
{% /cell %}
{% cell %}
5
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Threat indicators
{% /cell %}
{% cell %}
2
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Yara
{% /cell %}
{% cell %}
3
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Triggered consumer Ids
{% /cell %}
{% cell %}
1
{% /cell %}
{% /row %}
{% /table %}

### Some of the features are:

{% tabs %}
{% tab title="Apk" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[200] %}
Field name
{% /cell %}
{% cell header=true colwidth=[100] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Metadata version code
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Version code of the APK
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
APK signers path
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Path to APK signers
{% /cell %}
{% /row %}
{% row %}
{% cell %}
API events class name
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Class name of API events
{% /cell %}
{% /row %}
{% row %}
{% cell %}
API events function name
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Function name of API events
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Biffopcodes" %}
{% table layout="auto" %}
{% row %}
{% cell header=true %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Biffopcodes
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Shows basic arithmetic, logic, or data movement operations executed by a processor.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Emulation" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[300] %}
Field name
{% /cell %}
{% cell header=true colwidth=[100] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Emulation exit code
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Emulation exit code
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Additionalinformation compilerconstants
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Additional information about the compiler constants
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Metadata reason
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Reason for emulation metadata
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Overview modules
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Overview of modules in emulation metadata
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Extracted" %}
{% table layout="auto" %}
{% row %}
{% cell header=true %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted Urls
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted URLs from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted SHA-512 Hashes
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted SHA-512 from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted E-mails
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted Emails from the file
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="ExtendedData" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[300] %}
Field name
{% /cell %}
{% cell header=true colwidth=[100] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Header file size
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Size of the header file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Symbols static
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Static symbols
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Streams ole stream
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
OLE stream
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Streams subfiles no xml
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Subfiles with no XML
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="MetaData" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[300] %}
Field name
{% /cell %}
{% cell header=true colwidth=[100] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Content type
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Type of content
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Appversion
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Application version
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
To
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Recipient information
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Subject
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Subject of the metadata
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Cc
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
CC metadata
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Segments" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[300] %}
Field name
{% /cell %}
{% cell header=true colwidth=[100] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Segments entropy
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Entropy of segments
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Segments flags
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Flags of segments
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Sections" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[300] %}
Field name
{% /cell %}
{% cell header=true colwidth=[100] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sections entropy
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Entropy of sections
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sections virtualsize
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Virtual size of sections
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Strings" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[300] %}
Field name
{% /cell %}
{% cell header=true colwidth=[100] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Strings in binary content parse
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Strings parsed from binary content
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Threat Indicators" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[265] %}
Field name
{% /cell %}
{% cell header=true colwidth=[3] %}
Type
{% /cell %}
{% cell header=true %}
Example
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Threat Indicators
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
An identifier to show what kind of rules (Threat indicator) Filescan itself matched on the target file. It can contain more info than what is present in the actual report
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Yara" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[265] %}
Field name
{% /cell %}
{% cell header=true colwidth=[3] %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Yara Matched strings
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Yara matched strings
{% /cell %}
{% /row %}
{% row %}
{% cell %}
*....(Other features )*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% cell %}
*.....*
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Yara Rule name
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Yara rule name
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}
{% /tabs %}

## Similarity Search Filters

In addition to advanced technology, Similarity Search provides multi filtering search parameters. This feature offers greater flexibility and ensures that users receive the most accurate and relevant results for their specific needs.

{% tabs %}
{% tab title="Query filters" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[170] %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Possible values
{% /cell %}
{% cell header=true %}
Example
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% cell header=true %}
Required
{% /cell %}
{% /row %}
{% row %}
{% cell %}
SHA-256
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Yes
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Submission data
{% /cell %}
{% cell %}
Date
{% /cell %}
{% cell %}
2023-01-17T12:17:20.000Z
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Optional
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Final Verdict
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
MALICIOUS, LIKELY\_MALICIOUS, INFORMATIONAL, SUSPICIOUS, BENIGN, UNKNOWN
{% /cell %}
{% cell %}
MALICIOUS
{% /cell %}
{% cell %}
Verdict of a file
{% /cell %}
{% cell %}
Optional
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Tags
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
peexe,xml
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% cell %}
Tags of a file
{% /cell %}
{% cell %}
Optional
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Threshold
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
1 to 100 any integer
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Similarity threshold 0% to 100%

Higher score means higher similarity
{% /cell %}
{% cell %}
Optional
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Limit
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
1 to 100 any integer
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Number of returns
{% /cell %}
{% cell %}
Optional
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Non Query filters" %}
{% table layout="auto" %}
{% row %}
{% cell header=true %}
Field name
{% /cell %}
{% cell header=true %}
Type
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
File size
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Size of the input file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Entropy
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Entropy of the whole file(\*)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Architecture
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
A string describing what target of architecture (eg. 32 or 64bit) the binary was compiled for(\*)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
IsDotnet
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Whether the executable file is using the .NET framework(\*)
{% /cell %}
{% /row %}
{% /table %}

- \*Query filters only supported if the file type is PE
{% /tab %}
{% /tabs %}
