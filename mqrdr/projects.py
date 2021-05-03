# ----------------------------------------------------------------------------------------------------------------------
# Projects
# ----------------------------------------------------------------------------------------------------------------------


import requests
from mqrdr import settings, utils


BASE_URL = settings.BASE_URL


def list_private_projects(token, page=1, page_size=10, impersonated_id=None):
    ''' List all private projects

    token: Repository authorization token (string)
    page: Page number. Used for pagination with page_size
    page_size: The number of results included on a page. Used for pagination with page
    impersonated_id: Account ID of user being impersonated (optional, integer)
    '''

    headers = utils.create_token_header(token)
    
    if impersonated_id:
        request_url = f"{BASE_URL}/account/projects?page={page}&page_size={page_size}&impersonate={impersonated_id}"
    else:
        request_url = f"{BASE_URL}/account/projects?page={page}&page_size={page_size}"

    response = requests.get(request_url, headers=headers)

    return response.json()


def search_private_projects(token, data):
    ''' Search private projects

    token: Repository authorization token (string)
    data: Dictionary object containing project filters
    '''

    headers = utils.create_token_header(token)

    request_url = f"{BASE_URL}/account/projects/search"
    response = requests.post(request_url, json=data, headers=headers)

    return response.json()


def create_private_project(token, data, impersonated_id=None):
    ''' Create a new private project

    token: Repository authorization token (string)
    data: Dictionary object containing new project attributes
    impersonated_id: Account ID of user being impersonated (optional, integer)
    '''

    headers = utils.create_token_header(token)
    
    if impersonated_id:
        data["impersonate"] = impersonated_id
    
    request_url = f"{BASE_URL}/account/projects"
    response = requests.post(request_url, json=data, headers=headers)

    return response.json()


def view_private_project(token, project_id, impersonated_id=None):
    ''' View a private project

    token: Repository authorization token (string)
    project_id: ID of the project (integer)
    impersonated_id: Account ID of user being impersonated (optional, integer)
    '''

    headers = utils.create_token_header(token)
    
    if impersonated_id:
        request_url = f"{BASE_URL}/account/projects/{project_id}?impersonate={impersonated_id}"
    else:
        request_url = f"{BASE_URL}/account/projects/{project_id}"

    response = requests.get(request_url, headers=headers)

    return response.json()


def invite_private_project_collaborator(token, project_id, data, impersonated_id=None):
    ''' Create a new private project article

    token: Repository authorization token (string)
    project_id: ID of the project (integer)
    data: Dictionary object containing project collaborator attributes
    impersonated_id: Account ID of user being impersonated (optional, integer)
    '''

    headers = utils.create_token_header(token)

    if impersonated_id:
        data["impersonate"] = impersonated_id

    request_url = f"{BASE_URL}/account/projects/{project_id}/collaborators"

    response = requests.post(request_url, json=data, headers=headers)

    return response.json()


def update_private_project(token, project_id, data):
    ''' Update a private project

    token: Repository authorization token (string)
    project_id: ID of the project (integer)
    data: Dictionary object containing updated project attributes
    '''

    headers = utils.create_token_header(token)

    request_url = f"{BASE_URL}/account/projects/{project_id}"
    response = requests.put(request_url, json=data, headers=headers)

    return response


def delete_private_project(token, project_id):
    ''' Delete a private project

    token: Repository authorization token (string)
    project_id: ID of the project (integer)
    '''

    headers = utils.create_token_header(token)

    request_url = f"{BASE_URL}/account/projects/{project_id}"
    response = requests.delete(request_url, headers=headers)

    return response


def list_private_project_articles(token, project_id):
    ''' List a private project's articles

    token: Repository authorization token (string)
    project_id: ID of the project (integer)
    '''

    headers = utils.create_token_header(token)

    request_url = f"{BASE_URL}/account/projects/{project_id}/articles"
    response = requests.get(request_url, headers=headers)

    return response.json()


def create_private_project_article(token, project_id, data):
    ''' Create a new private project article

    token: Repository authorization token (string)
    project_id: ID of the project (integer)
    data: Dictionary object containing new project article attributes
    '''

    headers = utils.create_token_header(token)

    request_url = f"{BASE_URL}/account/projects/{project_id}/articles"

    response = requests.post(request_url, json=data, headers=headers)

    return response.json()