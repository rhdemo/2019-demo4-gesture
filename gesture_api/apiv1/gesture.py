import json
import uuid

from flask import jsonify, request, abort
from gesture_api.apiv1 import apiv1, storage


@apiv1.route('/gesture', methods=['POST'])
def create_gesture():
    if not request.data:
        return jsonify({})

    body = json.loads(request.data)
    label = body.get('label') or 'unknown_gesture'
    probability = 100 if body.get('label') else 0
    object_id = str(uuid.uuid4())
    storage.write_dict(body, f'{label}/{object_id}')
    print(f'{label}/{object_id}')
    print(body)
    gesture_obj = {
        'label': label,
        'probability': probability
    }

    return jsonify(gesture_obj)

