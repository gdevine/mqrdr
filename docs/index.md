---
layout: home
nav_order: 1
---

# Introduction

_MQRDR_ is a Python 3 library allowing you to programmatically interact with the Macquarie University [Research Data Repository](https://mq.figshare.com){:target="\_blank"}. It leverages the [Figshare API](https://docs.figshare.com){:target="\_blank"} to provide basic interfacing with the data repository as well as some more bespoke endpoints in line with the more advanced features of the Macquarie RDR.

# Getting started

## Installation

Ensure you have _Python 3_ and the package manager _pip_ installed. Run the following command at the terminal to install _MQRDR_

{% highlight shell %}
$ pip install mqrdr
{% endhighlight %}

## Import

Within your python script import the _MQRDR_ library

{% highlight python %}
import mqrdr
{% endhighlight %}

## API key authentication

To use MQRDR, you must first have an active account on the Macquarie University Research Data Repository. To authenticate when using the MQRDR library you must provide your API token, which can be found within the settings page of your data repository account. For security purposes it is highly recommended that you do not write your API key directly into your script. Instead create a file called _credentials.py_ and write your token there. E.g:

```
token = "<MyToken>"
```

replacing `<MyToken>` with your token string

**Make sure that the credentials.py file is kept private and is not shared with others or uploaded into public repositories for example.**

Now, in your main script, import the token as follows:

{% highlight python %}
import credentials
token = credentials.token
{% endhighlight %}

# Structure

MQRDR is made up of a number of modules, each referring to the type of resource within the repository. Follow the links below to view the endpoints for each resource type:

- [Projects](/mqrdr/projects)
- [Articles](/mqrdr/articles)
- [Accounts](/mqrdr/accounts)
- [Groups](/mqrdr/groups)
