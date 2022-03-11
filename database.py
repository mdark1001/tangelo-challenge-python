"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 09/03/22
@name: store
"""
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


class DBConnection:
    """
        Class base to extend in different connections classes
    """
    engine = None

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def create_connection(self):
        raise Exception("Not implemented yet")


class SQLiteStore(DBConnection):
    """
    Using SQLite engine.
    """

    def __init__(self):
        super(SQLiteStore, self).__init__('test.sqlite3', 'sqlite:///db')
        self.create_connection()
        self.session = Session(bind=self.engine)

    def create_connection(self):
        self.engine = create_engine(f'{self.url}/{self.name}', echo=False, connect_args={'check_same_thread': False})


db = SQLiteStore()  # Init db class
