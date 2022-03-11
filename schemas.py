"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 10/03/22
@name: schemas
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from models import Country
from database import db


class CountrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    region = fields.String(required=True)
    city_name = fields.String(required=True)
    languages = fields.String(required=False)
    time = fields.Float()
