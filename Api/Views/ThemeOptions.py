from Api import Resouce_Monitor
from flask import jsonify, Flask
from flask.views import MethodView
from flask_cors import cross_origin


class Themeoptions_API(MethodView):

    def get(self):
        
        res = jsonify(themes = [
            {
                'value': 'default',
                'jsonLabel':{ 
                    'value':'Default',
                    'icon':{
                        'name': 'droplet',
                        'options':{
                            'fill':'#a6c1ff' 
                        }
                    }
                }
            },
            {
                'value': 'dark',
                'jsonLabel':{ 
                    'value':'Dark',
                    'icon':{
                        'name': 'droplet',
                        'options':{
                            'fill':'#192038'
                        }
                    }
                }
            },
            {
                'value': 'cosmic',
                'jsonLabel':{ 
                    'value':'Cosmic',
                    'icon':{
                        'name': 'droplet',
                        'options':{
                            'fill':'#5a37b8' 
                        }
                    }
                }
            },
           {
                'value': 'corporate',
                'jsonLabel':{ 
                    'value':'Corporate',
                    'icon':{
                        'name': 'droplet',
                        'options':{
                            'fill':'#3366ff' 
                        }
                    }
            }
           }
        ])

        
        return res

