from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import JSONB

from application.extensions import db


class Profile(db.Model):
    "A people profile."

    __tablename__ = 'profile'

    id = db.Column('id', db.Integer(), primary_key=True)
    data = db.Column('data', JSONB, nullable=False)
    created_ts = db.Column(db.DateTime(timezone=True), server_default=text('NOW()'))
