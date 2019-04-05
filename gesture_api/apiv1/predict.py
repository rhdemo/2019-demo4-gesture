import json
import random

from flask import jsonify, request, abort
from gesture_api.apiv1 import apiv1, storage


@apiv1.route('/predict', methods=['POST'])
def predict_gesture():
    if not request.data:
        return jsonify({})

    body = json.loads(request.data)
    return jsonify(classify_gesture(body))


def classify_gesture(body):
    prediction = {
        "shake": 0.0,
        "circle": 0.0,
        "x": 0.0,
        "roll": 0.0,
        "fever": 0.0,
        "floss": 0.0
    }

    gesture = body.get('gesture')
    if gesture:
        prediction[gesture] = random.uniform(0.7, 1)

    return prediction

