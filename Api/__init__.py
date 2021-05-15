from Api import Resouce_Monitor
from Api.Resouce_Monitor.ResourceMonitor import ResourceMonitor
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_socketio import send, emit
socketio = SocketIO(logger=True, engineio_logger=True)
def create_app(testing=False):
    
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    
   
    CORS(app)

    with app.app_context():
        from .Routes import routes
        socketio.init_app(app, cors_allowed_origins="*")
        #app test block#

        ###############


        return socketio, app