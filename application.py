import eventlet

eventlet.monkey_patch()

from flask import Flask

from os import environ

from lib.app import config_app
from lib.get_env import get_env, PORT, MINIM_AUTH_KEY, MINIM_FLASK_APP_SECRET_KEY
from lib.socket import get_socket


def check_requirements_config():
    if MINIM_FLASK_APP_SECRET_KEY not in environ:
        raise Exception('app config not found')
    if MINIM_AUTH_KEY not in environ:
        raise Exception('token key not found')


check_requirements_config()

app = Flask(__name__)
config_app(app)
socketio = get_socket(app)

if __name__ == '__main__':
    socketio.run(app, port=get_env(PORT) or 5000)
