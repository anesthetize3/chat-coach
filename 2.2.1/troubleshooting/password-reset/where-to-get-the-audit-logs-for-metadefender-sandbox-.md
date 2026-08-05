---
type: page
title: Where to get the Audit Logs for MetaDefender Sandbox?
listed: true
description: 
index_title: Where to get the Audit Logs for MetaDefender Sandbox?
hidden: true
keywords: 
tags: 
---

### Approach 1: Access via UI

One of the ways to view the information of the users accessing the Sandbox is through the UI with the **Audit Logger**.

Location:  https://\[SANDBOX\_HOST\]/admin/audit-logger/auth

{% image url="https://uploads.developerhub.io/prod/XX2D/cctr1a6tzwaoqglnx74rtws4stkrhk5or0q7atg1xup121qg7zvuj3i2wj719avp.png" /%}

The information can be located here at the **AUDIT LOGGER** tabs from the Admin Panels section. With the information as many such as user logs in, user logs out, user inputs the wrong information.

### Approach 2: Access with log files

Another location that can be viewed with the information above is the log files that represent this information.

{% callout type="warning" title="Warning:" %}
This folder might require higher privileged access, Please use the required privileges to access the folder.
{% /callout %}

{% image url="https://uploads.developerhub.io/prod/XX2D/tton0oepe9uc9okthxnob6yyuars2h13nobdx6evim2g6w01dtqlcj59v50c8fd4.png" /%}

From here, you can see the file access.log, which contains all the information about the logins and logouts

{% image url="https://uploads.developerhub.io/prod/XX2D/pyqb6sbza0dbe1t8xm45pkpog2wblvx7dtxnqluub2x6acqpgjp3awt30d8ynl0q.png" %}
Location of the file
{% /image %}

{% image url="https://uploads.developerhub.io/prod/XX2D/qj637suqy2r5vdqtiw62616is8xg09wt4530x13qcz23yu3l0uiuckbgxt42mgbx.png" /%}

One of the specific command lines to help find a specific request is the grep command:

{% image url="https://uploads.developerhub.io/prod/XX2D/cptyfra9a3facvri1v2djgb7y0etm0qwfpt74nhh3gifxg67i3tcu8tolhowhv04.png" /%}

The command will fetch specific lines as follows:

{% image url="https://uploads.developerhub.io/prod/XX2D/nsxz12l45mzusudsk6v5mc6cc2pg06ggc9iimhextk1nv00hzup2bvj154bu1s92.png" /%}

The other commands to help with finding specific signout requests will be as follows:

{% image url="https://uploads.developerhub.io/prod/XX2D/mkmshijuvx8lxlzo4qoj43bqrj4vz006bkff4c8th41z9apmrcacmboqq1w35c91.png" /%}

The command will fetch specific lines as follows:

{% image url="https://uploads.developerhub.io/prod/XX2D/ftxmntu49ou0dd7pb44a7bmj4yax6249ogxuuxzpmou13eye6gxgjttq46ywkqjp.png" /%}

{% callout title="Info:" %}
Please note that the access logs will only show the information of the Api access information.
{% /callout %}

{% callout title="Support:" %}
If **Further Assistance** is required, please proceed to log a [**support case or chatting with our support engineer**](https://my.opswat.com/support).
{% /callout %}
