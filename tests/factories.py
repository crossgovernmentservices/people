# -*- coding: utf-8 -*-
from factory.alchemy import SQLAlchemyModelFactory

from application.database import db

class BaseFactory(SQLAlchemyModelFactory):

    class Meta:
        abstract = True
        sqlalchemy_session = db.session
