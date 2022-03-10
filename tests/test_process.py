"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 08/03/22
@name: test_process
"""
from unittest import TestCase
import pandas as pd
from process import ProcessResponseRestCountries
from tests.test_service import ServiceCountriesFake


class TestProcess(TestCase):

    def setUp(self):
        super(TestProcess, self).setUp()
        self.service = ServiceCountriesFake()
        self.fake_time = [{'time': 0.0001, 'time': 0.2, 'time': 0.32}]

    def test_process_make_data_frame_form_response(self):
        """

        :return:
        """
        df = ProcessResponseRestCountries().set_data_frame(self.service.response).get_df()
        self.assertIsInstance(df, pd.DataFrame)
        # df.head()

    def test_sha1_languages(self):
        country_demo = [{"name": {"common": "Angola", }, "region": "Africa", "languages": {"por": "Portuguese"}}]
        process = ProcessResponseRestCountries().set_data_frame(data=country_demo)
        self.assertIsNotNone(process.df)
        process.transform()
        self.assertIsInstance(process.df, pd.DataFrame)
        _languages = process.get_languages(country_demo[0])
        self.assertEqual(process.hash(_languages), process.df['languages'][0])

    def test_get_total_time(self):
        process = ProcessResponseRestCountries().set_data_frame(data=self.fake_time)
        suma = sum(list(map(lambda item: item['time'], self.fake_time)))

        self.assertEqual(process.get_total_time(), suma)

    def test_get_avg_time(self):
        process = ProcessResponseRestCountries().set_data_frame(data=self.fake_time)
        avg = sum(list(map(lambda item: item['time'], self.fake_time))) / len(self.fake_time)

        self.assertEqual(process.get_avg_time(), avg)

    def test_get_min_time(self):
        process = ProcessResponseRestCountries().set_data_frame(data=self.fake_time)
        min_time = min(list(map(lambda item: item['time'], self.fake_time)))
        self.assertEqual(process.get_min_time(), min_time)

    def test_get_max_time(self):
        process = ProcessResponseRestCountries().set_data_frame(data=self.fake_time)
        max_time = max(list(map(lambda item: item['time'], self.fake_time)))
        self.assertEqual(process.get_min_time(), max_time)
