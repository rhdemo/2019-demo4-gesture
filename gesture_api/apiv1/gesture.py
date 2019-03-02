import json
import uuid

from flask import jsonify, request, abort
from gesture_api.apiv1 import apiv1, storage


@apiv1.route('/gesture', methods=['GET'])
def get_gesture():

    gesture_obj = {
        'label': 'floss',
        "probability": 0,
        's3WriteStatus': 'complete'
    }

    return jsonify(gesture_obj)


@apiv1.route('/gesture', methods=['POST'])
def create_gesture():
    if not request.data:
        return jsonify({})

    body = json.loads(request.data)
    label = body.get('label') or 'unknown_gesture'
    probability = 100 if body.get('label') else 0
    object_id = str(uuid.uuid4())
    storage.write_dict(body, f'{label}/{object_id}')
    gesture_obj = {
        'label': label,
        "probability": probability,
        'body': body
    }

    return jsonify(gesture_obj)

