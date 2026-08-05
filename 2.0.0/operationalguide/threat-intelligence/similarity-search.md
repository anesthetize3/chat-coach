---
type: page
title: Similarity Search
listed: true
description: 
index_title: Similarity Search
hidden: false
keywords: 
tags: 
---

## Portable Executable type

These features are carefully selected based on their ability to provide accurate and relevant results, and they are continuously updated to stay current with the latest malware trends and techniques.

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
Pdb path
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Path of the PDB file on the compiler machine
{% /cell %}
{% /row %}
{% row %}
{% cell %}
DetectItEasyInfo
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Information that has been extracted using DetectitEasy
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Malware config
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Malware configuration refers to the settings and parameters within malicious software that dictate its behavior,
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
Digitally Signed
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Whether the digital signature is verified or not.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Packed
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Whether the input file is packed or not
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Total exported functions
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Indicates the number of exported functions in a PE
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
Certificate is Revoked
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
Certificate is SelfSigned
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
Certificate is Expired
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
Shows whether the associated certificate is expired
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
{% cell header=true %}
Field name
{% /cell %}
{% cell header=true colwidth=[56] %}
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
Stream names
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Descriptive identifiers for data streams within a .NET application, facilitating organized data management and manipulation.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Member reference names
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Clear labels for variables, methods, and properties within a .NET assembly, enhancing code readability and maintainability.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Module names
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Identifiers for discrete components or modules within a .NET application, aiding in modular development and component reuse.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Assembly Name
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Unique identifier for a compiled .NET assembly, enabling versioning, deployment, and referencing within the .NET ecosystem.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Anti metadata
{% /cell %}
{% cell %}
List of Boolean values
{% /cell %}
{% cell %}
The "Anti metadata" feature detects various anomalies within .NET assemblies to thwart malicious attempts at obfuscation or tampering. It scrutinizes assembly tables for multiple rows, ensuring data integrity, and flags assemblies with invalid or self-referenced typeref entries. Additionally, it identifies assemblies with fake data streams and extra metadata table data, while also checking for hidden .NET data directories. This comprehensive approach aims to enhance the security and reliability of .NET applications.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Header info" %}
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
Entry point section entry point
{% /cell %}
{% cell %}
Number
{% /cell %}
{% cell %}
Value of the section where the entry point of the PE resides
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
CRC
{% /cell %}
{% cell %}
Boolean
{% /cell %}
{% cell %}
CRC (Cyclic Redundancy Check) is a boolean indicator that determines whether the CRC value calculated for a file matches the expected CRC value.
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

{% tabs %}
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

{% tab title="Rich Header Compiler Ids" %}
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

{% tab title="Strings" %}
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
Strings
{% /cell %}
{% cell %}
String
{% /cell %}
{% cell %}
Extracted strings from the file
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
