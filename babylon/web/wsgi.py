#!/usr/bin/env python3.5
from web.app import init_app
from web.app import app
from web.utils.settings import global_settings


init_app(given_app=app)


if __name__ == "__main__":
    host = global_settings().get("app", {}).get("host")
    port = global_settings().get("app", {}).get("port")
    app.run(host=host, port=port)
