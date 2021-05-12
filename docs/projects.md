---
layout: home
nav_order: 2
---

# Projects

- [List user projects](#list-my-projects)
- [Search user projects](#search-my-projects)

## List user projects

{% highlight python %}
mqrdr.projects.list_user_projects(token, page=1, page_size=10, impersonated_id=None)
{% endhighlight %}

Returns a list of projects belonging to the current user, including published and private projects

**Options**

- _token_ : Repository authorization token (string, required)
- _page_ : Page number. Used for pagination with page_size (integer, optional, default = 1)
- _page_size_ : The number of results included on a page. Used for pagination with page (integer, optional, default = 10)
- _impersonated_id_ : Account ID of user being impersonated (integer, optional, only usable by admin accounts)

**Example**

{% highlight python %}
projects = mqrdr.projects.list_user_projects(token)
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

## Search user projects

{% highlight python %}
mqrdr.projects.search_user_projects(token, data)
{% endhighlight %}

Searches projects belonging to the current user, including published and private projects

**Options**

- _token_ : Repository authorization token (string, required)
- _data_ : object containing search parameters

**An example of a _data_ object**

{
"order": "published_date",
"search_for": "figshare",
"page": 1,
"page_size": 10,
"limit": 10,
"offset": 0,
"order_direction": "desc",
"institution": 2000013,
"published_since": "2017-12-22",
"modified_since": "2017-12-22",
"group": 2000013
}

**Impersonation**

The impersonate option must be included in the body (_data_ object) when using the search_user_projects function.

**Example**

{% highlight python %}
data = {
"search_for": 'Sample',
}
found_projects = mqrdr.projects.search_user_projects(token, data)
print(found_projects)

[
{'modified_date': '2021-05-12T02:02:16Z',
'title': 'PB01 Sample Project for RDR Testing Normal Title Normal Description (v5 23/04/21 13:22 update)',
'url': 'https://api.figshare.com/v2/account/projects/111356',
'published_date': None,
'storage': 'group',
'role': 'Collaborator',
'created_date': '2021-04-09T10:17:03Z',
'id': 111356}
]

{% endhighlight %}
