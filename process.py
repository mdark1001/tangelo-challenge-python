"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 08/03/22
@name: process
"""

import pandas as pd
import hashlib

import time


class IProcessResponse(object):
    """
    Interface that allow extend business logic, for dataframe process.
    Inherit this class and implements the transform method.

    """

    def __init__(self):
        self.df = None

    def get_df(self):
        return self.df

    def set_data_frame(self, data):
        self.df = pd.DataFrame(data)
        return self

    def transform(self):
        raise Exception("Not implemented yet")


class ProcessResponseRestCountries(IProcessResponse):
    """
        Process the dataframe and create a custom DF like Challenge Python L1.
    """

    def __init__(self):
        super(ProcessResponseRestCountries, self).__init__()

    def transform(self) -> None:
        """
        Transform and assign new dataframe.
            | Region | City Name | Languaje | Time |
        :return: None
        """
        new_df = pd.DataFrame(columns=['region', 'city_name', 'languages', 'time'])
        for index, row in self.df.iterrows():
            start_time = time.time()  # time start
            city_name = row['name']['common']
            _languages = self.hash(self.get_languages(row))
            end_time = time.time()

            new_df = new_df.append({
                'region': row['region'],
                'city_name': city_name,
                'languages': _languages,
                'time': float("%.7f" % float(end_time - start_time)),
            }, ignore_index=True)
        self.df = new_df

    def get_total_time(self) -> float:
        return self.df['time'].sum()

    def get_avg_time(self) -> float:
        return self.df['time'].mean()

    def get_min_time(self) -> float:
        return self.df['time'].min()

    def get_max_time(self) -> float:
        return self.df['time'].max()

    @staticmethod
    def hash(string: str) -> str:
        """
        using hashlib.sha1 try to hash a string if this method fails
        we encode the original string and try it again.
        :param string:
        :return: str hashed
        """
        _str = string
        try:
            return hashlib.sha1(_str).hexdigest()
        except  Exception:
            _str = string.encode()
            return hashlib.sha1(_str).hexdigest()

    @staticmethod
    def get_languages(row: dict) -> str:
        """
        Join and return dict values, from item in df
        :param row: dict, whit key language.
        :return: str
        """
        _languages = ''
        if type(row.get('languages', None)) is not float:  # validate.
            _languages = ','.join(row['languages'].values())
        return _languages
