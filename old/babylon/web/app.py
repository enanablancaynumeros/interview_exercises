from flask import Flask, jsonify
from flask_swagger import swagger
from flask_script import Manager

from web.db_manager.sql_manager import build_and_get_db_session, load_db_models
from web.utils.logger import get_logger
from web.utils.settings import global_settings


def create_app():
    new_app = Flask(__name__)
    new_db = build_and_get_db_session(new_app)
    new_manager = Manager(new_app)

    return new_app, new_db, new_manager


def init_app(given_app):
    load_db_models(db_object=db, app=app)
    register_general_endpoints(given_app)
    if global_settings().get("log", {}).get("requests"):
        handler = get_logger("werkzeug")
        given_app.logger.addHandler(handler)


def register_general_endpoints(given_app):
    @given_app.route("/_internal_/health")
    def health():
        return jsonify({"status": True})

    @given_app.route("/spec")
    def swagger_spec():
        swag = swagger(given_app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Babylon test"
        swag['info']['basePath'] = "/v1"
        swag['info']['produces'] = "application/json"
        return jsonify(swag)

    from web.apps.product.product_view import product_app_v1
    given_app.register_blueprint(product_app_v1, url_prefix='/v1')


app, db, manager = create_app()
