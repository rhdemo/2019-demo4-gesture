import time
from flask import jsonify
from gesture_api.apiv1 import apiv1


@apiv1.route('/status', methods=['GET'])
def status():
    status_obj = {
        'version': '0.1',
        'status': 'ok',
        'time': time.strftime('%A %B, %d %Y %H:%M:%S')
    }

    return jsonify(status_obj)
