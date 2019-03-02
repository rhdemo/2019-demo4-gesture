from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from gesture_api.apiv1 import apiv1


def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    return error_response(400, message)


@apiv1.errorhandler(404)
def not_found(error):
    return error_response(404, "Not Found")