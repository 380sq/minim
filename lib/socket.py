import time
from threading import Thread

from flask_socketio import SocketIO

thread = None
socketio = None


def get_socket(app):
    global socketio
    socketio = SocketIO(app, async_mode="eventlet")

    @socketio.on('connect')
    def handle_message():
        socketio.emit("message", "connect")

    return socketio


def send_io_message(message):
    global socketio
    print("emitting")
    socketio.sleep(0)
    socketio.emit("message", "hello")
