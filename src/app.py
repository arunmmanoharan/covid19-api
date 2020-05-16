import logging.config

import os
from flask import Flask, Blueprint
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from src.config import default
from src.api.controllers.endpoints.users import ns as users_namespace
from src.api.controllers.endpoints.statuses import ns as status_namespace
from src.api import api
from src.database import db

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = default.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = default.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = default.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = default.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = default.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = default.RESTPLUS_ERROR_404_HELP

    return flask_app


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('CovidAPI', __name__, url_prefix='/')
    api.init_app(blueprint)
    api.add_namespace(users_namespace)
    api.add_namespace(status_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

    return flask_app


app = initialize_app(app)

# def main():
#     initialize_app(app)
#     log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
#     app.run(debug=default.FLASK_DEBUG)


if __name__ == "__main__":
    log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(host='0.0.0.0')
