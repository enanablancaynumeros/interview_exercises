import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists, create_database, drop_database
from web.utils.utils import get_db_session_scope

from web.utils.settings import global_settings


def get_sql_url(db_type_settings, user, password, db_host_settings, port, db_name):
    host = "{}://{}:{}@{}:{}/{}".format(
        db_type_settings, user, password, db_host_settings, port, db_name
    )
    return host


def get_db_host_context_based():
    db_type_settings = global_settings().get("sql_db").get("type")
    db_host_settings = global_settings().get("sql_db").get("host")
    if db_type_settings == "sqlite":
        host = "{}:///{}".format(db_type_settings, db_host_settings)
    else:
        user = global_settings().get("sql_db").get("user")
        password = global_settings().get("sql_db").get("pass")
        port = global_settings().get("sql_db").get("port")
        db_name = global_settings().get("sql_db").get("name")

        host = get_sql_url(
            db_type_settings=db_type_settings,
            user=user,
            password=password,
            db_host_settings=db_host_settings,
            port=port,
            db_name=db_name,
        )
    return host


def build_and_get_db_session(app):
    host = get_db_host_context_based()
    app.config["SQLALCHEMY_DATABASE_URI"] = host
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])

    db = SQLAlchemy(app)
    return db


def import_apps_models():
    from web.apps.product.product_model import ProductModel


def load_db_models(db_object, app):
    import_apps_models()
    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])
    db_object.drop_all()
    db_object.create_all()
    load_initial_state(db_object)


def load_initial_state(db_object):
    from web.apps.product.product_interface import ProductInterface

    with get_db_session_scope(db_object.session) as db_session:
        ProductInterface(db_session).initial_state()


def remove_database(db_object):
    from web.app import app

    if database_exists(db_object.engine.url):
        drop_database(db_object.engine.url)
        create_database(db_object.engine.url)

    load_db_models(db_object, app)
    db_object.metadata.drop_all(db_object.engine)
    load_db_models(db_object, app)
