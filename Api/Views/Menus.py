from flask import jsonify, Flask
from flask.views import MethodView
from flask_cors import cross_origin

class Menus_API(MethodView):
    
    def get(self):
        res = jsonify(
                    menus =[
                    {
                        "title": 'Home Page',
                        "icon": { "name": 'home' },
                        "link": { "to": '/dashboard' },
                    },
                    {
                        "title": 'SYSTEM',
                        "group": True,

                    },
                    {
                        "title": 'Settings',
                        "icon": { "name": 'settings-2-outline' },
                        "children": [
                        {
                        "title": 'Localhost',
                        "link": {"to":'/dashboared'
                                    } 
                        },
                        {
                            "title": 'Actions',
                            "link": {"to":'/ALL_EXAMPLES/extra-components/actions/',"params":{"t":"ty"}},
                            
                        },
                        
                        ],
                    },
                    {
                        "title": 'Resources',
                        "icon": { "name": 'bulb-outline' },
                        "children": [
                        {
                        "title": 'Localhost',
                            "link": { "to": '/extra-components/accordion' },
                        },
                        {
                            "title": 'Actions',
                            "link": { "pathname:": "' /ALL_EXAMPLES/extra-components/actions/'"},
                        },
                        
                        ],
                    },
                    {
                        "title": 'Remote Link',
                        "icon": { "name": 'link-outline' },
                        "children": [
                        {
                            "title": 'Connected Servers',
                            "link": { "to": '/extra-components/accordion' },
                        },
                        {
                            "title": 'Add Server',
                            "link": { "to": '/extra-components/actions' },
                        },
                         {
                            "title": 'Remove Server',
                            "link": { "to": '/extra-components/actions' },
                        },
                        
                        ],
                    },


                                        {
                        "title": 'PYTHON PROCESSES',
                        "group": True,
                    },
                    {
                        "title": 'Settings',
                        "icon": { "name": 'settings-2-outline' },
                        "children": [
                        {
                        "title": 'Localhost',
                            "link": { "to": '/extra-components/accordion' },
                        },
                        {
                            "title": 'Actions',
                            "link": { "to": '/extra-components/actions' },
                        },
                        
                        ],
                    },
                    {
                        "title": 'Resources',
                        "icon": { "name": 'bulb-outline' },
                        "children": [
                        {
                        "title": 'Localhost',
                            "link": { "to": '/extra-components/accordion' },
                        },
                        {
                            "title": 'Actions',
                            "link": { "to": '/extra-components/actions' },
                        },
                        
                        ],
                    },
                    {
                        "title": 'Remote Link',
                        "icon": { "name": 'link-outline' },
                        "children": [
                        {
                            "title": 'Connected Servers',
                            "link": { "to": '/extra-components/accordion' },
                        },
                        {
                            "title": 'Add Server',
                            "link": { "to": '/extra-components/actions' },
                        },
                         {
                            "title": 'Remove Server',
                            "link": { "to": '/extra-components/actions' },
                        },
                        
                        ],
                    },
                                        {
                        "title": 'DOCKER',
                        "group": True,
                    },
                    {
                        "title": 'Settings',
                        "icon": { "name": 'settings-2-outline' },
                        "children": [
                        {
                        "title": 'Localhost',
                            "link": { "to": '/extra-components/accordion' },
                        },
                        {
                            "title": 'Actions',
                            "link": { "to": '/extra-components/actions' },
                        },
                        
                        ],
                    },
                    {
                        "title": 'Resources',
                        "icon": { "name": 'bulb-outline' },
                        "children": [
                        {
                        "title": 'Localhost',
                            "link": { "to": '/extra-components/accordion'},
                        },
                        {
                            "title": 'Actions',
                            "link": { "to": '/extra-components/actions?kty=rsusutustusrusrsursr' },
                        },
                        
                        ],
                    },
                    {
                        "title": 'Remote Link',
                        "icon": { "name": 'link-outline' },
                        "children": [
                        {
                            "title": 'Connected Servers',
                            "link": { "to": '/extra-components/accordion' },
                        },
                        {
                            "title": 'Add Server',
                            "link": { "to": '/extra-components/actions' },
                        },
                         {
                            "title": 'Remove Server',
                            "link": { "to": '/extra-components/actions' },
                        },
                       ],
                    },
                    ])
        return res