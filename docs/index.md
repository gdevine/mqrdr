---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
---

# MQRDR

_MQRDR_ is a Python 3 library allowing you to programmatically interact with the Macquarie University [Research Data Repository](https://mq.figshare.com){:target="\_blank"}. It leverages the Figshare API (Give link) to provide basic interfacing with the data repository as well as some more bespoke endpoints in line with the more advanced features of the RDR.

# Getting started

## Installation

1. 13 Ensure you have _Python 3_ and the package manager _pip_ installed. Run the following command at the terminal to install _MQRDR_

{% highlight shell %}
$ pip install mqrdr
{% endhighlight %}

## Import

Within your python script import the _MQRDR_ library

{% highlight python %}
import mqrdr
{% endhighlight %}

# API key

To use MQRDR, you must first have an active account on the Macquarie University Research Data Repository. To authenticate when using the MQRDR library you must provide your API token, which can be found within the settings page of your data repository account. MQRDR expects Store your token in a file called token.txt, or ideally set it in the Python session

# Structure

MQRDR is made up of a number of modules:

1.

# Projects

### List projects

{% highlight python %}
projects = mqrdr.projects.list_private_projects(token)

{% endhighlight %}

```python
projects = mqrdr.projects.list_private_projects(token)
```
