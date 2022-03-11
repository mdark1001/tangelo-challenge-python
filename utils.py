"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 10/03/22
@name: utils.py
"""
from flask import make_response, jsonify


def response_with(response, value=None, message=None,
                  error=None, headers={}, pagination=None):
    result = {}
    if value is not None:
        result.update(value)
    if response.get('message', None) is not None:
        result.update({'message': response['message']})
    result.update({'code': response['code']})
    if error is not None:
        result.update({'errors': error})
    if pagination is not None:
        result.update({'pagination': pagination})
    headers.update({'Access-Control-Allow-Origin': '*'})
    headers.update({'server': 'Flask REST API'})
    return make_response(jsonify(result), response['http_code'], headers)
