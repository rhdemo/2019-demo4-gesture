import json
import time

from flask import jsonify, request, abort
from gesture_api.apiv1 import apiv1, storage


@apiv1.route('/gesture', methods=['POST'])
def create_gesture():
    if not request.data:
        return jsonify({})

    body = json.loads(request.data)
    return jsonify(classify_gesture(body))


def classify_gesture(body):
    return {
        'gesture': body.get('gesture') or 'unknown_gesture',
        'probability': 100 if body.get('gesture') else 0
    }

