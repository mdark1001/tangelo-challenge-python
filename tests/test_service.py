"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 08/03/22
@name: test_service.py
"""
import json
from pathlib import Path
from unittest import TestCase

from services import RestCountriesService

BASE_DIR = Path(__file__).resolve().parent.parent


class ServiceCountriesFake(RestCountriesService):
    def __init__(self):
        super(ServiceCountriesFake, self).__init__()

    def get_all(self):
        self.get_from_file(path=str(BASE_DIR) + '/tests/all.json')
        return self


class TestService(TestCase):
    def setUp(self):
        super(TestService, self).setUp()
        self.service = RestCountriesService()

    def test_endpoint_all_success(self):
        """
        Validar que la función get all regrese una respuesta correcta
        :return:
        """
        self.service.get_all()
        self.assertEqual(self.service.status_code, 200)

    def test_throw_exception_endpoint_get(self):
        """
        Validar excepción del método privado de get, si no se suministra una url de acceso.
        :return:
        """
        with self.assertRaises(Exception):
            self.service._get('')

    def test_validate_response_data_type(self):
        self.service.get_all()
        # print(self.service.response)
        self.assertIsInstance(self.service.response, list)

    def test_singleton_class(self):
        new_instance = RestCountriesService()
        self.assertEqual(new_instance, self.service)
