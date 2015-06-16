#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask_script import Manager, Shell, Server
from flask_migrate import MigrateCommand

from application.app import create_app
from application.settings import DevConfig, ProdConfig
from application.extensions import db


if os.environ.get("APPLICATION_ENV") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)

def _make_context():
    """Return context dict for a shell session so you can access
    app, db by default.
    """
    return {'app': app, 'db': db}

@manager.command
def test():
    """Run the tests."""
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code

@manager.option('-e', '--email', help='Email address of new user')
def create_user(email):
    """
    One can also create a user via the API:
    curl -XPOST http://people.xgs.local/session -d '{"email":"a@b.c"}' -H 'Content-Type: application/json'

    """
    db.session.execute('CREATE SCHEMA IF NOT EXISTS "%s"' % email)
    db.session.execute('SET search_path TO "%s"' % email)
    db.session.commit()
    with app.app_context():
        db.create_all()
        db.session.commit()

manager.add_command('server', Server(
    host='0.0.0.0', port=int(os.environ.get('PORT', '32435'))))
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
