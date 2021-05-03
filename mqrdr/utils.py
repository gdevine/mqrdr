''' MQRDR

Utility functions for Macquarie University Research Data Repository library

'''

from mqrdr import settings


BASE_URL = settings.BASE_URL


def create_token_header(token):
    ''' Create a http header object with token embedded
    
    '''

    header =  {'Authorization': 'token ' + token}

    return header
