from flask import Blueprint
from flask_restful import Api

from .resources import PersonResource, SendMessageResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(PersonResource, "/persons/")
    api.add_resource(SendMessageResource, "/send/message")
    app.register_blueprint(bp)
