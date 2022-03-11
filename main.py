"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 08/03/22
@name: services
"""

from flask import Flask, request
from flask_cors import CORS

from models import Country
from schemas import CountrySchema
from store import SaveCountries
import status_response as status
from utils import response_with

app = Flask(__name__)

CORS(app)
my_store = SaveCountries(drop=False)


@app.route('/city', methods=['GET'])
def list_cities():
    cities = Country
    start = 0
    if request.args.get('limit', 10):
        limit = int(request.args.get('limit'))
    if request.args.get('start', 0):
        start = int(request.args.get('start', 0))
    result = CountrySchema(many=True, only=['id', 'region', 'city_name', 'languages']).dump(cities.select(start=start,
                                                                                                          limit=limit))
    return response_with(status.SUCCESS_200, value={'cities': result})


@app.route('/city/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = Country.select(filter={'id': city_id})
    if not city:
        return response_with(status.BAD_REQUEST_400)

    result = CountrySchema()
    print(result.dump(city))
    return response_with(status.SUCCESS_200, value=result.dump(city))


if __name__ == '__main__':
    app.run(debug=True)
