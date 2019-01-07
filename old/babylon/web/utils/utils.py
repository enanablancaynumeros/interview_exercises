import base64
import os
from contextlib import contextmanager
from functools import wraps

from flask import request, Response
from web.utils.custom_exceptions import InvalidBody
from werkzeug.security import check_password_hash

from web.utils.settings import global_settings


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    :param password:
    :param username:
    """
    valid_user = username in global_settings().get("users")
    return valid_user and check_password(
        global_settings().get("users").get(username), password
    )


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        "Could not verify your access level for that URL.\n"
        "You have to login with proper credentials",
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'},
    )


def check_password(pw_hash, password):
    return check_password_hash(pw_hash, password)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


@contextmanager
def change_dir(newdir):
    """
    http://stackoverflow.com/a/24176022/3337586
    :param newdir:
    :return:
    """
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


def auth_headers(username, password):
    user_pass = base64.b64encode(
        bytes("{}:{}".format(username, password), "ascii")
    ).decode("ascii")
    return {"Authorization": "Basic " + user_pass}


@contextmanager
def get_db_session_scope(sql_db_session):
    """Provide a transactional scope around a series of operations.
    :param sql_db_session: With specific environment information defined outside
    """
    session = sql_db_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_body_from_request(specific_request):
    body = dict(specific_request.form)
    for key in body:
        if isinstance(body[key], list):
            if len(body[key]) <= 1:
                if len(body[key]):
                    body[key] = body[key][0]
                else:
                    body[key] = ""
            else:
                msg = "Field {} contained more than 1 value in the body {}"
                raise InvalidBody(msg.format(key, body))
    return body
