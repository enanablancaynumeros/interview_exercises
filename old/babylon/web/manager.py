import subprocess
import os

from web.app import manager


@manager.command
def unittests():
    from web.tests.unittests.unittests import run_unittests
    project_folder = os.path.abspath(os.path.dirname(__file__))
    run_unittests(project_folder)


@manager.command
def bdd():
    project_folder = os.path.abspath(os.path.dirname(__file__))
    steps_folder = os.path.join(project_folder, "tests/bdd/features/")
    behave_command = ["behave", steps_folder, "--no-capture"]
    subprocess.run(behave_command)


@manager.command
def runserver():
    from web.app import app, init_app, global_settings

    init_app(given_app=app)
    host = global_settings().get("app", {}).get("host")
    port = global_settings().get("app", {}).get("port")
    app.run(host=host, port=port)


if __name__ == "__main__":
    manager.run()
