---
type: page
title: URL Reputation Methodology
listed: false
description: 
index_title: URL Reputation Methodology
hidden: true
keywords: 
tags: 
---

## Features

{% tabs %}
{% tab title="Basic URL Features" %}
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
number of parameters
{% /cell %}
{% cell %}
Represents the count of parameters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of anchors
{% /cell %}
{% cell %}
Indicates the quantity of anchor tags in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
url length
{% /cell %}
{% cell %}
Contains the length of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
calculate dash frequency
{% /cell %}
{% cell %}
Measures the frequency of dash characters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
calculate lowdash frequency
{% /cell %}
{% cell %}
Signifies the frequency of underscore characters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
count numbers in url
{% /cell %}
{% cell %}
Reveals the number of numeric characters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
calculate dots frequency
{% /cell %}
{% cell %}
Indicates the frequency of dot characters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
calculate slashes frequency
{% /cell %}
{% cell %}
Captures the frequency of slash characters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has ip address
{% /cell %}
{% cell %}
Checks if the URL contains an IP address.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
url shortened
{% /cell %}
{% cell %}
Indicates whether the URL has been shortened.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="URL Structure Features" %}
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
count subdomains
{% /cell %}
{% cell %}
Contains the count of subdomains in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has redirect or double slash
{% /cell %}
{% cell %}
Checks for the presence of redirects or double slashes in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
path depth
{% /cell %}
{% cell %}
Represents the depth of the path in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
average domain token length
{% /cell %}
{% cell %}
Contains the average length of domain tokens.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
suspicious tld
{% /cell %}
{% cell %}
Indicates whether the URL has a suspicious top-level domain.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
length of file
{% /cell %}
{% cell %}
Contains the length of the file portion in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
length of arguments
{% /cell %}
{% cell %}
Indicates the maximum allowable length of the query string portion of a URL
{% /cell %}
{% /row %}
{% row %}
{% cell %}
urls having at symbol
{% /cell %}
{% cell %}
Reveals whether the URL contains the @ symbol.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Domain and Path Features" %}
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
port
{% /cell %}
{% cell %}
Contains the port number in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has https token in domain
{% /cell %}
{% cell %}
Checks for the presence of an https token in the domain.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
ccTLDs
{% /cell %}
{% cell %}
Contains the count of country code top-level domains (ccTLDs) in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of special characters
{% /cell %}
{% cell %}
Represents the count of special characters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of uppercase letters
{% /cell %}
{% cell %}
Indicates the count of uppercase letters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of lowercase letters
{% /cell %}
{% cell %}
Contains the count of lowercase letters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of vowels
{% /cell %}
{% cell %}
Reveals the count of vowels in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of consonants
{% /cell %}
{% cell %}
Contains the count of consonants in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
query letter count
{% /cell %}
{% cell %}
Contains the count of letters in the query parameters of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
longest path token length
{% /cell %}
{% cell %}
Represents the length of the longest token in the URL path.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
domain longest word length
{% /cell %}
{% cell %}
Indicates the length of the longest word in the domain.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
path longest word length
{% /cell %}
{% cell %}
Contains the length of the longest word in the URL path.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
subdirectory longest word length
{% /cell %}
{% cell %}
Captures the length of the longest word in subdirectories.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
arguments longest word length
{% /cell %}
{% cell %}
Indicates the length of the longest word in URL arguments.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
url contains sensitive word
{% /cell %}
{% cell %}
Checks for the presence of sensitive words in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number rate url
{% /cell %}
{% cell %}
Represents the rate of numeric characters in the URL.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Content Analysis Features" %}
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
number of unique characters
{% /cell %}
{% cell %}
Represents the count of unique characters in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has subdirectory
{% /cell %}
{% cell %}
Checks for the presence of a subdirectory in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has parameters
{% /cell %}
{% cell %}
Indicates whether the URL has parameters.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has numbers in path
{% /cell %}
{% cell %}
Reveals if the URL path contains numeric characters.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
domain entropy
{% /cell %}
{% cell %}
Contains the entropy of the domain portion in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
path entropy
{% /cell %}
{% cell %}
Indicates the entropy of the URL path.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
parameter entropy
{% /cell %}
{% cell %}
Captures the entropy of URL parameters.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
anchor entropy
{% /cell %}
{% cell %}
Represents the entropy of anchor tags in the URL.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="URL Security Features" %}
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
has ip address like strings
{% /cell %}
{% cell %}
Checks for IP address-like strings in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has hexadecimal strings
{% /cell %}
{% cell %}
Indicates the presence of hexadecimal strings in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has suspicious keywords
{% /cell %}
{% cell %}
Checks for suspicious keywords in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has javascript keywords
{% /cell %}
{% cell %}
Indicates the presence of JavaScript-related keywords in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
is obfuscated url
{% /cell %}
{% cell %}
Indicates whether the URL is obfuscated.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has url encoding
{% /cell %}
{% cell %}
Checks for URL encoding in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has non latin characters
{% /cell %}
{% cell %}
Reveals whether the URL contains non-Latin characters.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has typosquatting patterns
{% /cell %}
{% cell %}
Detects typosquatting patterns in the URL.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Length and Ratio Features" %}
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
average parameter length
{% /cell %}
{% cell %}
Contains the average length of URL parameters.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of path tokens
{% /cell %}
{% cell %}
Represents the count of tokens in the URL path.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has non standard ports
{% /cell %}
{% cell %}
Indicates whether the URL uses non-standard ports.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
length of subdomain
{% /cell %}
{% cell %}
Contains the length of the subdomain in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
length of top level domain
{% /cell %}
{% cell %}
Represents the length of the top-level domain (TLD) in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
has non alphanumeric characters in domain
{% /cell %}
{% cell %}
Checks for non-alphanumeric characters in the domain.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
length of url path query combined
{% /cell %}
{% cell %}
Contains the length of the combined URL path and query.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of vowels in domain
{% /cell %}
{% cell %}
Indicates the count of vowels in the domain.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Character Composition Features" %}
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
number of consonants in domain
{% /cell %}
{% cell %}
Contains the count of consonants in the domain.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of vowels in path
{% /cell %}
{% cell %}
Reveals the count of vowels in the URL path.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of consonants in path
{% /cell %}
{% cell %}
Contains the count of consonants in the URL path.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of vowels in parameters
{% /cell %}
{% cell %}
Indicates the count of vowels in URL parameters.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of consonants in parameters
{% /cell %}
{% cell %}
Contains the count of consonants in URL parameters.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of fragments
{% /cell %}
{% cell %}
Represents the count of fragments in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number of get special characters
{% /cell %}
{% cell %}
Contains the count of special characters in GET parameters.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
path url ratio
{% /cell %}
{% cell %}
Indicates the ratio of URL path length to the full URL length.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Digit and Letter Count Features" %}
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
arg url ratio
{% /cell %}
{% cell %}
Represents the ratio of argument length to the full URL length.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
arg domain ratio
{% /cell %}
{% cell %}
Captures the ratio of arguments length to the domain length.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
domain url ratio
{% /cell %}
{% cell %}
Indicates the ratio of domain length to the full URL length.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
path domain ratio
{% /cell %}
{% cell %}
Contains the ratio of URL path length to the domain length.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
arg path ratio
{% /cell %}
{% cell %}
Represents the ratio of arguments length to the URL path length.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
is executable url
{% /cell %}
{% cell %}
Indicates whether the URL is executable.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
character continuity rate
{% /cell %}
{% cell %}
Captures the rate of character continuity in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
host digit count
{% /cell %}
{% cell %}
Contains the count of digits in the host portion of the URL.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Word and Token Length Features" %}
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
directory digit count
{% /cell %}
{% cell %}
Indicates the count of digits in the directory portion of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
filename digit count
{% /cell %}
{% cell %}
Represents the count of digits in the filename portion of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
extension digit count
{% /cell %}
{% cell %}
Captures the count of digits in the extension of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
query digit count
{% /cell %}
{% cell %}
Contains the count of digits in the query parameters of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
host letter count
{% /cell %}
{% cell %}
Indicates the count of letters in the host portion of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
directory letter count
{% /cell %}
{% cell %}
Contains the count of letters in the directory portion of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
filename letter count
{% /cell %}
{% cell %}
Captures the count of letters in the filename portion of the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
extension letter count
{% /cell %}
{% cell %}
Indicates the count of letters in the extension of the URL.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}

{% tab title="Rate and Entropy Features" %}
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
number rate domain
{% /cell %}
{% cell %}
Indicates the rate of numeric characters in the domain.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number rate directory name
{% /cell %}
{% cell %}
Contains the rate of numeric characters in directory names.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number rate file name
{% /cell %}
{% cell %}
Captures the rate of numeric characters in file names.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number rate extension
{% /cell %}
{% cell %}
Indicates the rate of numeric characters in file extensions.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
number rate after path
{% /cell %}
{% cell %}
Contains the rate of numeric characters after the URL path.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
entropy directory name
{% /cell %}
{% cell %}
Represents the entropy of directory names in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
entropy filename
{% /cell %}
{% cell %}
Indicates the entropy of file names in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
entropy extension
{% /cell %}
{% cell %}
Captures the entropy of file extensions in the URL.
{% /cell %}
{% /row %}
{% row %}
{% cell %}
entropy after path
{% /cell %}
{% cell %}
Indicates the entropy of characters after the URL path.
{% /cell %}
{% /row %}
{% /table %}
{% /tab %}
{% /tabs %}

## Prediction flow

{% image url="https://uploads.developerhub.io/prod/XX2D/x3m9lizbdohwoxogl8tsxi6plvg23g0dha5tsw59qcfh4w77l9tgpidkojb0kyua.png" /%}

To enable this integration, please walk through the following steps:

## Reliability and Accuracy:

Our offline URL detector model demonstrates exceptional reliability and accuracy across multiple validation sets, supported by significant sample sizes.

**First Round of Validation:** With 3,976 instances, highlights the model's proficiency in detecting malicious URLs, correctly identifying 3,887 out of 3,976 instances.

**Second Round of Validation:** In the second round, the model accurately identifies 22,276 out of 24,271 benign URLs and 7,078 out of 7,881 malicious URLs, resulting in an overall accuracy of 91%.

**Third Round of Validation:** In the third round, comprising 6,069 instances, the model accurately detects 5,802 out of 6,069 malicious URLs, resulting in a 96% accuracy. This suggests a potential limitation in benign URL classification in this specific validation set.

**Fourth Round of Validation** In the fourth round of validation, the model accurately identifies 99% of benign URLs out of a total of 23,981 instances. However, its detection rate for malicious URLs is lower, at 18%. Despite this class imbalance, the overall accuracy remains high at 98%.

**Adjusting the threshold range might allow the model to classify more aggressively or conservatively, depending on the desired outcome for threat detection**.

The table displays the classification results and instances, highlighting the percentage of accuracy for each validation results.

{% table layout="auto" %}
{% row %}
{% cell header=true %}
Validation
{% /cell %}
{% cell header=true %}
All Instances
{% /cell %}
{% cell header=true %}
Detected Benign (0)
{% /cell %}
{% cell header=true %}
Misclassified Benign (False Negative)
{% /cell %}
{% cell header=true %}
Detected Malicious (1)
{% /cell %}
{% cell header=true %}
Misclassified Malicious (False Positive)
{% /cell %}
{% cell header=true %}
Accuracy
{% /cell %}
{% /row %}
{% row %}
{% cell %}
1st
{% /cell %}
{% cell %}
3976
{% /cell %}
{% cell %}
0
{% /cell %}
{% cell %}
89 (2.24%)
{% /cell %}
{% cell %}
3887 (97.76%)
{% /cell %}
{% cell %}
0
{% /cell %}
{% cell %}
**98%**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
2nd
{% /cell %}
{% cell %}
32152
{% /cell %}
{% cell %}
22276 (69.28%)
{% /cell %}
{% cell %}
803 (2.50%)
{% /cell %}
{% cell %}
7078 (22.01%)
{% /cell %}
{% cell %}
1995 (6.1%)
{% /cell %}
{% cell %}
**91%**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
3rd
{% /cell %}
{% cell %}
6069
{% /cell %}
{% cell %}
0
{% /cell %}
{% cell %}
267 (4.40%)
{% /cell %}
{% cell %}
5802 (95.6%)
{% /cell %}
{% cell %}
0
{% /cell %}
{% cell %}
**96%**
{% /cell %}
{% /row %}
{% row %}
{% cell %}
4th
{% /cell %}
{% cell %}
23981
{% /cell %}
{% cell %}
23477 (97.89%)
{% /cell %}
{% cell %}
69 (0.29%)
{% /cell %}
{% cell %}
420 (1.75%)
{% /cell %}
{% cell %}
15 (0.07%)
{% /cell %}
{% cell %}
**98%**
{% /cell %}
{% /row %}
{% /table %}
