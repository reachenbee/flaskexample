import os
import sys
import json

import flask
from flask import request, Response
from flask_restplus import Api, Resource

# Default config vals
THEME = 'default' if os.environ.get('THEME') is None else os.environ.get('THEME')
FLASK_DEBUG = 'false' if os.environ.get('FLASK_DEBUG') is None else os.environ.get('FLASK_DEBUG')

# Create the Flask app
application = flask.Flask(__name__)

# Load config values specified above
application.config.from_object(__name__)

# Load configuration vals from a file
application.config.from_pyfile('application.config', silent=True)

# Only enable Flask debugging if an env var is set to true
application.debug = application.config['FLASK_DEBUG'] in ['true', 'True']

app = Api(app=application)
name_space = app.namespace('main', description='Main APIs')


@name_space.route("/")
class MainClass(Resource):
    def get(self):
        return {
            "status": "Got new data"
        }

    def post(self):
        return {
            "status": "Posted new data"
        }


# @application.route('/')
# def welcome():
#     theme = application.config['THEME']
#     return flask.render_template('index.html', theme=theme, flask_debug=application.debug)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
