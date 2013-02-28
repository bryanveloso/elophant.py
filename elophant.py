# -*- coding: utf-8 -*-

import requests

DEFAULT_ELOPHANT_URL = 'http://api.elophant.com/v2/'
DEFAULT_ELOPHANT_REGION = 'NA'


class Elophant(object):
    """
    The API wrapper for Elophant(.com).

    """
    ELOPHANT_URL = DEFAULT_ELOPHANT_URL
    ELOPHANT_REGION = DEFAULT_ELOPHANT_REGION

    def __init__(self, api_key=None):
        self.api_key = api_key

