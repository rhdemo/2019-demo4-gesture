import json
import time

from flask import jsonify, request
from gesture_api.apiv1 import apiv1, storage


@apiv1.route('/training', methods=['POST'])
def create_training():
    if not request.data:
        return jsonify({})

    body = json.loads(request.data)
    store_data(body)
    return jsonify({})


def store_data(body):
    label = body.get('gesture')
    if not label:
        return  # don't store

    time_num = int(round(time.time() * 1000))
    player_id = body.get('playerId') or 'unknown_player'
    storage.write_dict(body, f'{label}/{time_num}-{player_id}')

