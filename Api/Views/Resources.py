from flask.views import MethodView
from flask import current_app as app
from flask_socketio import emit
from .. import socketio

@socketio.on('connect')
def test_connect():
    print('my response', 'dataConnected')
    emit('my response', {'data': 'Connected'})

    
class Resoucres_API(MethodView):

    def get(self):
        
        return ""