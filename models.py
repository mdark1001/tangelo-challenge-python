"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 09/03/22
@name: models
"""

from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import declarative_base

from database import db

Base = declarative_base()


class Country(Base):
    """
        Create a Model that represent a Country of dataframe item.
    """
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    region = Column(String(150))
    city_name = Column(String(150))
    languages = Column(String(255))
    time = Column(Float(precision=10))

    def __init__(self, region, city_name, languages, time):
        self.region = region  # TODO region should be a foreignKey,
        self.city_name = city_name
        self.languages = languages
        self.time = time

    def __repr__(self):
        return "Country<region:{}><city_name:{}>".format(self.region, self.city_name)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def to_dict(self):
        return dict(
            id=self.id,
            region=self.region,
            city_name=self.city_name,
            languages=self.languages,
            time=self.time,
        )

    @classmethod
    def select(cls, start=0, limit=0, filter={}):
        query = db.session.query(cls)
        if limit:
            query = query.slice(start, limit)
        if filter:
            return query.filter_by(**filter)
        return query.all()


Base.metadata.create_all(db.engine)
