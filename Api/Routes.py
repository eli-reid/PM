from Api.Resouce_Monitor.ResourceMonitor import ResourceMonitor
from Api.Resouce_Monitor.RmThread import RmThread
from os import replace
from flask import current_app as app, jsonify
from flask_socketio import  emit
from .Views import Menus_API
from .Views import Themeoptions_API 
from .Resouce_Monitor import Resources
from . import socketio

r = ResourceMonitor()

def routes():
    print("**********************************************************************************")


# menu routes
app.add_url_rule('/menus/', view_func = Menus_API.as_view('menus'), methods=['GET'])
# Theme Route
app.add_url_rule('/themes/', view_func = Themeoptions_API.as_view('themes'), methods=['GET'])

# TEST ROUTEs
rr= Resources()

@app.route("/")
def hh():
     return  str(rr.disk.usage)

@app.route("/start")
def hsh():
    r.start()
    return  "Started"

@app.route("/stop")
def whsh():
    r.stop()
    return  f"Stopped! <br> {r[0].getThreads}"

