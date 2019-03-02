import os
from gesture_api import create_app

application = create_app(__name__)


if __name__ == "__main__":
    port = os.getenv('SERVER_PORT') or '8080'
    application.run(host='0.0.0.0', port=port)


@application.shell_context_processor
def make_shell_context():
    return {}

