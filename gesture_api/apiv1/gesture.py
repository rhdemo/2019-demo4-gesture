import json
import time

from flask import jsonify, request, abort
from gesture_api.apiv1 import apiv1, storage


@apiv1.route('/gesture', methods=['POST'])
def create_gesture():
    if not request.data:
        return jsonify({})

    body = json.loads(request.data)
    store_data(body)
    return jsonify(classify_gesture(body))


def store_data(body):
    label = body.get('gesture') or 'unknown_gesture'
    if not label:
        return  # don't store

    time_num = int(round(time.time() * 1000))
    player_id = body.get('playerId') or 'unknown_player'
    storage.write_dict(body, f'{label}/{time_num}-{player_id}')


def classify_gesture(body):
    return {
        'gesture': body.get('gesture') or 'unknown_gesture',
        'probability': 100 if body.get('label') else 0
    }

