"""
This script runs the Condo_Co_Op_Web application using a development server.
"""
import sys
from os import environ

from Api import create_app
if  len(sys.argv) > 2:
    socketio, app = create_app()
else :
    socketio, app = create_app()
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 5555
    try:
        socketio.run(HOST, PORT)
    except OSError:
        socketio.run(HOST, 5500)