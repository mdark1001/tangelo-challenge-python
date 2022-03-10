"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 08/03/22
@name: services
"""
import json

import requests


class RestCountriesService(object):
    """
        Class service that fetch data from private _url(restcountries)

    """
    _url = 'https://restcountries.com/'

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RestCountriesService, cls).__new__(cls)
        return cls.instance

    def __init__(self, version='v3.1/'):
        self.version = version
        self.response = None
        self.status_code = None

    def get_all(self):
        self._get(endpoint='all')
        return self

    def get_from_file(self, path):
        with open(path, 'r', ) as file:
            self.response = json.loads(file.read())

    def _get(self, endpoint):
        if not endpoint:
            raise Exception("Es necesario un url de acceso")
        result = requests.get(f'{self._url}{self.version}{endpoint}')
        self.status_code = result.status_code
        self.response = result.json()
