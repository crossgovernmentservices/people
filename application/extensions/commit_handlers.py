from flask import request
from sqlalchemy.event import listens_for
from flask.ext.sqlalchemy import SignallingSession
from ..services.notification import Notification
from ..models.profile import Profile


notification_service = Notification()

class NotificationHandler(object):

    def handle(self, changes, profile):
        for model, operation in changes:
            if model['table_name'] == 'notification' and operation == 'insert':
                email = request.authorization.username
                if 'tel' in profile.data:
                    phone_number = profile.data['tel']
                    # skip the default show&tell phone number
                    if '123456789' not in phone_number:
                        message = model['values']['message']
                        transport = model['values']['transport']
                        notification_service.notify(email, phone_number, message, transport)

notification_handler = NotificationHandler()

@listens_for(SignallingSession, 'after_flush')
def after_flush_handler(session, tx):
    try:
        d = session._model_changes
    except AttributeError:
        return

    if d:
        changes = []
        for model, operation in list(d.values()):
            model_dict = { 
                'values': model.to_dict(),
                'table_name': model.__table__.name
            }
            changes.append((model_dict, operation))
        session.info['my_changes'] = changes

        # load the profile, while the session is open
        profiles = Profile.query.all()
        if len(profiles) >= 1:
            profile = profiles[-1]
            session.info['profile'] = profile

        d.clear()


@listens_for(SignallingSession, 'after_commit')
def after_commit_handler(session):
    if 'my_changes' in session.info:
        notification_handler.handle(session.info['my_changes'], session.info['profile'])
