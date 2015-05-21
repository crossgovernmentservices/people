# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate
migrate = Migrate()

from flask_cache import Cache
cache = Cache()

from application.models import APIScaffold
api_scaffold = APIScaffold()

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

from flask_cors import CORS
cors = CORS()
