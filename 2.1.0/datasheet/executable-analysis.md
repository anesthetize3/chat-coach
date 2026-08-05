---
type: page
title: Executable Analysis (PE)
listed: true
description: 
index_title: Executable Analysis (PE)
hidden: false
keywords: 
tags: 
---

Executable analysis is a fundamental aspect of cybersecurity software, involving the in-depth examination of executable files to uncover concealed malicious code and extract relevant TTPs.

We tackle Portable Executable (PE) file analysis from various angles. We employ **deep structure analysis**, **adaptive threat analysis**, and incorporate up-to-date **threat intelligence**. This comprehensive approach ensures top-notch protection against modern cyber threats, giving our clients peace of mind in today's digital landscape. Some of the most useful features are:

- Both generic and specific packer unpacking
- Intelligent full binary disassembly
- Certificate analysis \& validation
- Detect compiler, linker, packer used
- 150+ dedicated threat indicators
- Wide-spread usage of MITRE TTPs
- Extract malware configs

You can find our three main categories of features in the tables below:

{% tabs %}
{% tab title="Adaptive Threat Analysis" %}
{% callout type="success" title="Adaptive Threat Analysis" %}
On the following link you can find a sample showcasing most of the features shown below:

[https://www.filescan.io/uploads/65097f0bf1b40cb0d61e8340/reports/77accaa9-5d0e-4f97-a4d7-2119c7121cf7/overview](https://www.filescan.io/uploads/650974554a9bd894f5990723/reports/88f2e4e7-13a3-4c43-9dfb-de3b97a3ca01/details)
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[189] %}
Feature
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Unpacking
{% /cell %}
{% cell %}
Malware is often packed to make it more difficult to analyze. The unpacking feature uses a variety of techniques to unpack malware, including targeted unpackers and generic solutions. Targeted unpackers are designed to unpack specific types of malware, while generic solutions can unpack a wider range of malware.
{% /cell %}
{% cell %}
[Learn more](executable-analysis/supported-packers-for-unpacking.md)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Malware configuration extraction
{% /cell %}
{% cell %}
The malware configuration extraction feature extracts the configuration of malware files. This information can include the malware's command and control server, its target systems, and its payload. The configuration information can be used to understand how the malware works and how it can be neutralized.
{% /cell %}
{% cell %}
[Learn more](executable-analysis/supported-malwares-for-config-extraction.md)
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Automated tagging
{% /cell %}
{% cell %}
The automated tagging feature automatically tags malware files with signatures, behavior patterns, and similarity search. Signatures are patterns of bytes that are unique to a particular malware family. Behavior patterns are the actions that a malware file performs. Similarity search is used to find malware files that are similar to each other. The tagged information can be used to classify malware and identify new threats.
{% /cell %}
{% cell %}
{% p /%}
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Deep Structure Analysis" %}
{% callout type="success" title="Constants Analysis" %}
On the following link you can find a sample showcasing most of the features shown below:

[https://www.filescan.io/uploads/650966b8935d595cf275bf94/reports/486d8898-2be9-41e0-96b0-cd931c1e08c9/overview](https://www.filescan.io/uploads/650974554a9bd894f5990723/reports/88f2e4e7-13a3-4c43-9dfb-de3b97a3ca01/details)

(Head to the `Analysis overview` **-\>** `Unknown` Tab **-\>** `Detected cryptographic algorithms` indicator)
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[188] %}
Constants Analysis
{% /cell %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
String Identification
{% /cell %}
{% cell %}
This feature enables the identification and highlighting of potentially suspicious or critical strings within a software program, including both ASCII and UTF16 encoded strings. It aids in pinpointing data that may be indicative of malicious activities.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Cryptographic Constant Detection
{% /cell %}
{% cell %}
The system has the capability to identify and flag constants commonly utilized in cryptographic functions. By detecting these constants, it helps in recognizing potential cryptographic operations within the code.
{% /cell %}
{% /row %}
{% /table %}

{% callout type="success" title="Compilation Analysis" %}
On the following link you can find a sample showcasing most of the features shown below:

[https://www.filescan.io/uploads/650974554a9bd894f5990723/reports/88f2e4e7-13a3-4c43-9dfb-de3b97a3ca01/details](https://www.filescan.io/uploads/650974554a9bd894f5990723/reports/88f2e4e7-13a3-4c43-9dfb-de3b97a3ca01/details)
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[187] %}
**Compilation Analysis**
{% /cell %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Packer and Protector Detection
{% /cell %}
{% cell %}
This functionality is designed to identify the usage of third-party packing and protection tools within software applications. This is essential in uncovering attempts to obscure code, thereby enhancing transparency and security analysis.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
.NET Obfuscator Detection
{% /cell %}
{% cell %}
This feature is dedicated to detecting the presence of obfuscation techniques employed in .NET applications. It assists in revealing attempts to conceal code logic and intent, aiding security experts in thorough code examination.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Compiler, Linker, and Framework Identification
{% /cell %}
{% cell %}
This tool is adept at identifying the specific compilers, linkers, and development frameworks that were utilized during the compilation of the analyzed program. This information helps in understanding the software's origin and dependencies.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Parsing PE Compiler Metadata
{% /cell %}
{% cell %}
By parsing the "RICH" headers within Portable Executable (PE) files, this feature provides valuable insights into the compilation process. It assists analysts in gaining a deeper understanding of the software's development history and evolution.
{% /cell %}
{% /row %}
{% /table %}

{% callout type="success" title="Signature and Hash Calculations" %}
On the following link you can find a sample showcasing most of the features shown below:

[https://www.filescan.io/uploads/65098776988a26b6d96e9249/reports/412f590d-3bd3-4f67-b790-f6a09898cc24/details](https://www.filescan.io/uploads/65098776988a26b6d96e9249/reports/412f590d-3bd3-4f67-b790-f6a09898cc24/details)

(Head to the `Extended details` **-\>** `Certificates` and open the various certificates)
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[193] %}
**Signature and Hash Calculations**
{% /cell %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
.NET GUID Calculation
{% /cell %}
{% cell %}
This capability involves the calculation of .NET Globally Unique Identifiers (GUIDs) and their correlation to Module Versions and Type Library Identifiers (TypeLib Id). It facilitates the tracking of versioning and compatibility aspects within .NET assemblies.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Digital Certificate Calculation and Verification
{% /cell %}
{% cell %}
This feature is responsible for the computation and validation of digital certificates, including Authentihash and Authenticode signatures. It ensures the authenticity and integrity of software components, offering robust security assessment.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Digital Certificate Status
{% /cell %}
{% cell %}
This feature rigorously evaluates digital certificates by checking their revocation status, assessing their validity, and monitoring expiration dates. It ensures the integrity and trustworthiness of certificates, reducing the risk of compromised software execution and enhancing overall security.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Entropy and Hash Generation
{% /cell %}
{% cell %}
The system can calculate a variety of entropy and hash values for different elements of the Portable Executable (PE) file, encompassing resources and sections. This multi-faceted hashing capability enhances the granularity of security analysis.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Fuzzy Hash Calculation
{% /cell %}
{% cell %}
Fuzzy hashing techniques such as imphash, ssdeep, and the proprietary Fsiofuzzyhash are employed to generate unique hash values. These fuzzy hashes aid in identifying similarities and differences between software binaries, enhancing threat detection and classification.
{% /cell %}
{% /row %}
{% /table %}

{% callout type="success" title="PE File Analysis" %}
On the following links you can find a samples showcasing most of the features shown below:

PDB: [https://www.filescan.io/uploads/64f7d05467511af1a1b51180...](https://www.filescan.io/uploads/64f7d05467511af1a1b51180/reports/e59d3d9a-f644-4fcf-a658-a0626d78a3b2/details)

Version Info: [https://www.filescan.io/uploads/65098ef832ffdb7a7a0b9e95...](https://www.filescan.io/uploads/65098ef832ffdb7a7a0b9e95/reports/2db786c0-1978-4e74-8530-ac6e3b4bb9c4/details)

SFX: [https://www.filescan.io/uploads/6508ffe02d5fc006cad6b3af...](https://www.filescan.io/uploads/6508ffe02d5fc006cad6b3af/reports/3f7b43b7-4105-4762-a4f0-4b968bcf123b/details)

Disassembly: [https://www.filescan.io/uploads/6509858d988a26b6d96e912b...](https://www.filescan.io/uploads/6509858d988a26b6d96e912b/reports/b2fc6b77-30ef-4537-b1ec-d6d17db05223/disassembly)

Extraction: [https://www.filescan.io/uploads/65071846b448abc35b2d17e8...](https://www.filescan.io/uploads/65071846b448abc35b2d17e8/reports/1b53fd22-490a-4f58-aae8-ff59857de41f/overview)
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[197] %}
**PE File Analysis**
{% /cell %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Categorization of PE Libraries and Imported Functions
{% /cell %}
{% cell %}
This feature provides a comprehensive categorization of PE libraries and their imported functions while simultaneously offering the capability to blacklist specific libraries and functions. This categorization and control mechanism enhance security by allowing the fine-tuning of software behavior and mitigating potential risks associated with untrusted components.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Parsing PDB Information
{% /cell %}
{% cell %}
This functionality involves parsing and extracting information from Program Database (PDB) files associated with PE executables. PDB files are essential for debugging and reverse engineering. By parsing PDB information, security analysts gain valuable insights into the structure and evolution of the software, aiding in vulnerability assessment and code analysis.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Parsing Version Information of the PE
{% /cell %}
{% cell %}
Parsing version information embedded within the PE file provides critical contextual data about the software's build, origin, and compatibility. This information is crucial for determining the software's legitimacy and assessing its trustworthiness, making it an essential aspect of security analysis.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Parsing and Detecting TLS Callbacks
{% /cell %}
{% cell %}
This feature is designed to identify and analyze Thread Local Storage (TLS) callbacks within PE files. TLS callbacks are often utilized as an anti-debugging mechanism by malicious software. Detecting these callbacks is essential for security experts to understand and counteract evasion tactics employed by potential threats.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Parsing Self-Extracting Installer Metadata
{% /cell %}
{% cell %}
Self-extracting installers (SFX) are executable archives that can unpack their contents when executed. This feature not only identifies the presence of SFX but also extracts relevant metadata. Supporting both 7z and RAR formats ensures comprehensive coverage, enhancing security analysts' ability to scrutinize and validate the integrity of such archives.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Intelligent Disassembly of PE Files:
{% /cell %}
{% cell %}
This intelligent disassembly process prioritizes the analysis of significant code blocks while efficiently dismissing less relevant sections. This approach optimizes performance without compromising detection accuracy, allowing for rapid and effective assessment of PE files.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extraction of Embedded Files
{% /cell %}
{% cell %}
The system offers heuristic detection for embedded files within PE executables, including PEs, resources, and certificates, among others. This capability allows for the extraction and analysis of potentially concealed or encrypted content, contributing to a more comprehensive security evaluation.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Extraction of Files from Installers
{% /cell %}
{% cell %}
While currently supporting only the MSI format, this feature facilitates the extraction of files from installer packages. MSI files are commonly used for software installation, and this functionality allows for the examination of their contents, helping security analysts identify potential vulnerabilities or malicious components during the installation process.
{% /cell %}
{% /row %}
{% /table %}

{% callout type="success" title="Whitelisting" %}
On the following link you can find a sample showcasing most of the features shown below:

[https://www.filescan.io/uploads/65098b9a988a26b6d96e9460/reports/447be3ab-2974-42a3-96d0-da6b01b0da66/details](https://www.filescan.io/uploads/65098b9a988a26b6d96e9460/reports/447be3ab-2974-42a3-96d0-da6b01b0da66/details)
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[198] %}
Whitelisting
{% /cell %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Digital Certificate Whitelisting
{% /cell %}
{% cell %}
This functionality empowers users to create and manage a whitelist of trusted digital certificates. By incorporating digital certificate whitelisting, the system allows for the identification and validation of software components signed by trusted entities.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Custom Hash Whitelisting
{% /cell %}
{% cell %}
Users have the capability to establish a custom hash-based whitelist, enabling the recognition and validation of files with specific hash values. Custom hash whitelisting provides a flexible and tailored approach to verifying the integrity of files, enabling the exclusion of known good files from security scrutiny.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Integrated Whitelists Support
{% /cell %}
{% cell %}
The system seamlessly integrates with pre-existing whitelists, allowing organizations to leverage their established trust repositories. This integration ensures continuity and minimizes disruptions while enhancing the security posture by extending trust to approved software and components.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
National Software Reference Library (NSRL) Support
{% /cell %}
{% cell %}
This feature facilitates integration with the National Software Reference Library (NSRL), a comprehensive repository of known software and file signatures. By supporting the NSRL, the system streamlines the identification and validation of files that match known and legitimate software components. This significantly reduces the risk of false positives in security assessments and accelerates the verification process for widely recognized software.
{% /cell %}
{% /row %}
{% /table %}

{% callout type="success" title="Others" %}
On the following link you can find a sample showcasing most of the features shown below:

[https://www.filescan.io/uploads/65098776988a26b6d96e9249/reports/412f590d-3bd3-4f67-b790-f6a09898cc24/details](https://www.filescan.io/uploads/65098776988a26b6d96e9249/reports/412f590d-3bd3-4f67-b790-f6a09898cc24/details)

(Check the `Visualization` image on the linked page and you can also head to the `Indicators of Compromise` subpage to find the related `UUIDs`)
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true colwidth=[199] %}
Others
{% /cell %}
{% cell header=true %}
{% p /%}
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Identify and Map UUIDs
{% /cell %}
{% cell %}
This feature identifies and links Universally Unique Identifiers (UUIDs) to known associated files and metadata. It simplifies the process of recognizing and establishing connections between UUIDs and their relevant elements, facilitating efficient tracking and analysis.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Visualize PE Data
{% /cell %}
{% cell %}
This feature offers visualizations of Portable Executable (PE) data using BytePlot and entropy-based representations. It provides intuitive graphical insights into the structure and characteristics of PE files, aiding in the rapid identification of patterns, anomalies, and potential security concerns.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Decompile  .NET Files:
{% /cell %}
{% cell %}
This feature includes the capability to decompile .NET files, converting compiled code into human-readable source code. It simplifies the analysis and comprehension of software behavior.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Threat Intelligence" %}
{% callout type="success" title="Threat Intelligence" %}
On the following link you can find a sample showcasing most of the features shown below:

[https://www.filescan.io/uploads/65098d4286207ed6281f611c/reports/4702ce9a-2b5b-4853-b24f-8bddca8f5311/osint](https://www.filescan.io/uploads/65098d4286207ed6281f611c/reports/4702ce9a-2b5b-4853-b24f-8bddca8f5311/osint)
{% /callout %}

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Feature
{% /cell %}
{% cell header=true %}
Description
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ML-Based Similarity Search (300+ Features)
{% /cell %}
{% cell %}
This feature employs Machine Learning (ML) techniques to conduct a similarity search using over 300 distinct features. It enables the identification of similarities and patterns within data, facilitating effective threat detection and classification.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Integration with Open Source Intelligence Vendors
{% /cell %}
{% cell %}
The system seamlessly integrates with various open-source intelligence vendors, including MetaDefender Cloud and VirusTotal. This integration enhances threat intelligence by leveraging external resources and data, augmenting the breadth and depth of security analysis.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Malware Family Detection Based on MISP Galaxy Keywords
{% /cell %}
{% cell %}
This feature employs MISP Galaxy keywords to detect specific malware families. By associating threats with known categories and attributes, it enhances the accuracy of malware identification and enables targeted response strategies.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
Auto-Updating YARA Rules for OSINT Detection
{% /cell %}
{% cell %}
The system continuously updates YARA rules to provide an additional layer of Open Source Intelligence (OSINT) detection. This dynamic rule management ensures that the system remains current and effective in identifying emerging threats and vulnerabilities.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}
{% /tabs %}
