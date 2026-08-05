---
type: page
title: PE Similarity Search
listed: true
description: 
index_title: PE Similarity Search
hidden: false
keywords: 
tags: 
---

## PE fields

These features are carefully selected based on their ability to provide accurate and relevant results, and they are continuously updated to stay current with the latest malware trends and techniques.

{% tabs %}
{% tab title="Numeric Fields" %}
{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[241] %}
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
Unix timestamp
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
A timestamp showing when the file was compiled
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
DLL characteristic
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Features which make a PE actually portable in memory
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Subsystem
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Defines whether the PE is made to be a Console or UI application
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
Linker version(major)
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
What version of linker what used at compilation time
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Linker version(minor)
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
What version of linker what used at compilation time
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Entry point section entropy
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Entropy of the section where the entry point resides
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Section number
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Number of sections present in the PE
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Resource number
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Number of resources present in the PE
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Resources to file ratio
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Ratio between the size of the resources \& the file itself
{% /cell %}
{% /row %}
{% row %}
{% cell %}
CFG
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Indicator whether CFG (Control Flow Guard) is enabled at compilation time.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
GS
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Indicator whether GS (Buffer Security Check *\[Guarded Stack\]*) is enabled at compilation time.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ASLR
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Indicator whether ASLR (Address space layout randomization) is enabled at compilation time.
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
{% row %}
{% cell %}
IsDotnet
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
Digitally Signed
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Whether the digital signature is verified or not.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

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
Digital signature verification
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Whether the digital signature is verified or not.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Architecture
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
A string describing what target of architecture (eg. 32 or 64bit) the binary was compiled for
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
Pdb path
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Path of the PDB file on the compiler machine
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Version info" %}
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
Verinfo: File Description
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Version information describing the file description of this application
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Verinfo: File version
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Version information describing the file version of this application
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Verinfo: Internal name
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Version information describing the internal name of this application
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Verinfo: Legal copyright
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Version information describing the legal copyright of this application
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Verinfo: Product name
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Version information describing the product name of this application
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Verinfo: Product version
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Version information describing the product version of this application
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Verinfo: Company name
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Version information describing the company name who created this application
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Pdb guid" %}
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
Pdb guid
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
GUID of the PDB associated with the binary
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Compilers" %}
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
Rich header compiler ids
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
An ID number to the specific compiler used during the compilation process
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Sections" %}
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
Memory base address of section
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
In-memory base address of the section
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Memory size of a section
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
In-memory size of the section
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Size of physical data
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Size of the physical data on-disk
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Entropy of section
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Entropy of the specific section
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Resources" %}
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
Size of resources
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Size of the resource
{% /cell %}
{% /row %}
{% row %}
{% cell %}
File type of the actual data
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
File type of the actual data
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
Intended language of the resource
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Sublanguage
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Intended language of the resource
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
Extracted Domains
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted Domains from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted Ips
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted Ips from the file
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
Extracted UUIDs
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted UUIDs from the file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extracted Registry Paths
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted Registry Paths from the file
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Imports" %}
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
DLL
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Imported DLL of the input file
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Functions
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Imported functions from a specific dll
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
Certificate Owner
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Shows the owner of the certificate
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Certificate isRevoked
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Shows whether the associated certificate is revoked
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Certificate isSelfSigned
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Shows whether the associated certificate is selfsigned
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Certificate isExpired
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Shows whether the associated certificate is expired
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
Entropy of the whole file
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
A string describing what target of architecture (eg. 32 or 64bit) the binary was compiled for
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
Whether the executable file is using the .NET framework
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}
{% /tabs %}
