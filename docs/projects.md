---
layout: home
nav_order: 2
---

# Projects

- [List (my) projects](#list-my-projects)
- [Search (my) projects](#search-my-projects)

## List (my) projects

{% highlight python %}
mqrdr.projects.list_private_projects(token, page=1, page_size=10, impersonated_id=None)
{% endhighlight %}

Returns a list of projects belonging to the current user, including published and private projects

**Options**

- _token_ : Repository authorization token (string, required)
- _page_ : Page number. Used for pagination with page_size (integer, optional, default = 1)
- _page_size_ : The number of results included on a page. Used for pagination with page (integer, optional, default = 10)
- _impersonated_id_ : Account ID of user being impersonated (integer, optional, only usable by admin accounts)

**Example**

{% highlight python %}
projects = mqrdr.projects.list_private_projects(token)
print(projects)

[{'modified_date': '2021-04-20T21:30:42Z',
'title': 'A dummy project for testing the Data Repository integration with PURE',
'url': 'https://api.figshare.com/v2/account/projects/112092',
'published_date': None,
'storage': 'group',
'role': 'Owner',
'created_date': '2021-04-20T21:30:42Z',
'id': 112092},
{'modified_date': '2021-04-25T21:30:53Z',
'title': 'PB01 Sample Project for RDR Testing Normal Title Normal Description',
'url': 'https://api.figshare.com/v2/account/projects/111356',
'published_date': None,
'storage': 'group',
'role': 'Collaborator',
'created_date': '2021-04-09T10:17:03Z',
'id': 111356}]

{% endhighlight %}

## Search (my) projects

{% highlight python %}
mqrdr.projects.search_private_projects(token, data, page=1, page_size=10, impersonated_id=None)
{% endhighlight %}

Searches projects belonging to the current user, including published and private projects

**Options**

- _token_ : Repository authorization token (string, required)
- data :
- _page_ : Page number. Used for pagination with page_size (integer, optional, default = 1)
- _page_size_ : The number of results included on a page. Used for pagination with page (integer, optional, default = 10)
- _impersonated_id_ : Account ID of user being impersonated (integer, optional, only usable by admin accounts)

**Example**

{% highlight python %}
projects = mqrdr.projects.list_private_projects(token)
print(projects)

[{'modified_date': '2021-04-20T21:30:42Z',
'title': 'A dummy project for testing the Data Repository integration with PURE',
'url': 'https://api.figshare.com/v2/account/projects/112092',
'published_date': None,
'storage': 'group',
'role': 'Owner',
'created_date': '2021-04-20T21:30:42Z',
'id': 112092},
{'modified_date': '2021-04-25T21:30:53Z',
'title': 'PB01 Sample Project for RDR Testing Normal Title Normal Description',
'url': 'https://api.figshare.com/v2/account/projects/111356',
'published_date': None,
'storage': 'group',
'role': 'Collaborator',
'created_date': '2021-04-09T10:17:03Z',
'id': 111356}]

{% endhighlight %}
