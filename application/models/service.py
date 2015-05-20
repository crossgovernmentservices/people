from sqlalchemy.sql.expression import text
from sqlalchemy.dialects.postgresql import JSONB

from application.extensions import db


class Service(db.Model):
    """
    Authorised services that are allowed (by the person)
    to interact with their data.

    Append-only, so that a log is kept.

    has_access: True/False, denothing access or not.
    created_ts: the latest value wins.
    info: JSON containing 'name' and 'description', and
    possibly other data.

    """

    __tablename__ = 'service'

    id = db.Column('id', db.Integer(), primary_key=True)
    data = db.Column('data', JSONB, nullable=False)
    has_access = db.Column('has_access', db.Boolean(), nullable=False)
    created_ts = db.Column(db.DateTime(timezone=True), server_default=text('NOW()'))
