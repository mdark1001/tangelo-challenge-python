"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 09/03/22
@name: cli
"""
# from tests.test_service import ServiceCountriesFake as RestCountriesService
import logging

import process
import store
from services import RestCountriesService


def run():
    """
    Execute whole runtime:
        - Get Countries form API
        - Create a Data frame whit [Region,City Name, Languages,Time]
        - Store DF in SQLite
        - Read SQLite and export a JSON File
    :return:
    """
    print("""Welcome please wait, we're working now....    """)
    data = RestCountriesService().get_all()
    my_process = process.ProcessResponseRestCountries()
    my_process.set_data_frame(data.response)
    my_process.transform()
    print("""
        Total Time: {}\n
        Max Time:   {}\n
        Min Time:   {}\n
        Avg Time:   {}\n
    """.format(
        my_process.get_total_time(),
        my_process.get_max_time(),
        my_process.get_min_time(),
        my_process.get_avg_time(),
    ))
    df = my_process.get_df()
    my_store = store.SaveCountries(drop=True)
    my_store.save_dataframe_in_database(df)
    my_store.save_to_json('./db/data.json', my_store.read_from_database())


run()
