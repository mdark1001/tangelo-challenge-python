"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 09/03/22
@name: test_storege_sqlite
"""

from unittest import TestCase

from models import Country
from process import ProcessResponseRestCountries
from tests.test_service import ServiceCountriesFake


class TestStoreSQLite(TestCase):

    def setUp(self):
        super(TestStoreSQLite, self).setUp()

    def test_create_country(self):
        country = Country(
            region='America',
            city_name='Mexico',
            languages='AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724',
            time=0.0002
        )
        country.create()
