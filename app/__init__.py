import flask

from .config import Config

app = flask.Flask("__name__", static_folder='/static')


from app import routes








