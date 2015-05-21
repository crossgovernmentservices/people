from sqlalchemy.sql.expression import text

from application.extensions import db


class Notification(db.Model):
    "A notification."

    __tablename__ = 'notification'

    id = db.Column('id', db.Integer(), primary_key=True)
    message = db.Column('message', db.Text(), nullable=False)
    transport = db.Column('transport', db.Text(), nullable=False)
    created_ts = db.Column(db.DateTime(timezone=True), server_default=text('NOW()'))
