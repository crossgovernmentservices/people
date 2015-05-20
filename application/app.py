# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
from flask import Flask

from application.settings import ProdConfig
from application.extensions import (
    cache,
    db,
    migrate,
    api_scaffold,
    auth,
    cors,
)
from application import (
    auth_blueprint,
)

def create_app(config_object=ProdConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    api_scaffold.init_app(app, db, auth)
    cors.init_app(app)
    return None

def register_blueprints(app):
    auth_blueprint.views.blueprint.app = app
    app.register_blueprint(auth_blueprint.views.blueprint)
    return None
