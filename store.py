"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 09/03/22
@name: store
"""
import json

from models import Country
from database import db


class SaveCountries:
    def __init__(self, drop):
        if drop:
            Country.__table__.delete()

    @staticmethod
    def save_dataframe_in_database(df):
        """
        Iterate through a df and Create a Country instance to save in database.
        :param df:
        :return: None
        """
        for index, country in df.iterrows():
            c = Country(**country)
            c.create()

    @staticmethod
    def read_from_database():
        return Country.select()

    @staticmethod
    def save_to_json(filename, items):
        result = []
        for item in items:
            result.append(item.to_dict())
        with open(filename, 'w+', encoding='UTF-8') as file:
            json.dump(result, file)
