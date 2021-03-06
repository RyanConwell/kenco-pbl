import os

from flask import Flask

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='developmentsecretisnotgoodsecret',
        DATABASE=os.path.join(app.instance_path, 'backend.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    from backend import db
    db.init_app(app)

    # apply blueprints to the app (and init mail)
    from backend import api, monitor
    app.register_blueprint(api.bp)
    app.register_blueprint(monitor.bp)
    api.mail.init_app(app)

    return app
