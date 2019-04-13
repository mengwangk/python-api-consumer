#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests


from utils import logger

class ApiException(Exception):
    """Base class for API exception"""

    def __init__(self):
        """Constructor."""
        pass


class ApiClient(object):
    """
    Base class for REST APIs client.
    """

    def __init__(self, api_key=None, user_name=None, password=None):
        """
        Constructor.
        :param api_key: API key.
        :param user_name: Login user.
        :param password:  User password.
        """
        self.api_key = api_key
        self.user_name = user_name
        self.password = password

    def request(self, method='get', url='', headers=None, data=None,
                json=None, params=None, verify=False, **kwargs):
        """Make a HTTP request."""

        if (url == ""):
            raise ValueError("Invalid URL %s" % url)

        request = getattr(requests, method.lower())
        req = request(url, headers=headers, data=data, json=json, params=params, verify=verify, **kwargs)
        return req.json()


class FakeJsonApi(ApiClient):
    """Fake APIs - for testing."""

    def get_content(self):
        pass
