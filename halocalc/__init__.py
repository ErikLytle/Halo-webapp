""" Halo calculator webapp package initializer. """
import flask

app = flask.Flask(__name__)

app.config.from_object('halocalc.config')

import halocalc.views