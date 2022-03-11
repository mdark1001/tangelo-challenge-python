"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 10/03/22
@name: status_response
"""
SUCCESS_200 = {
    'http_code': 200,
    'code': 'success'
}
SUCCESS_201 = {
    'http_code': 201,
    'code': 'success'
}

BAD_REQUEST_400 = {
    "http_code": 400,
    "code": "badRequest",
    "message": "Bad request"
}
SERVER_ERROR_500 = {
    "http_code": 500,
    "code": "serverError",
    "message": "Server error"
}
