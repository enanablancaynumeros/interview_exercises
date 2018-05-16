#!/usr/bin/env python3.5
from werkzeug.contrib.profiler import ProfilerMiddleware
from web.app import app


def main():
    app.config['PROFILE'] = True
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
    app.run(debug=True)

if __name__ == "__main__":
    main()
