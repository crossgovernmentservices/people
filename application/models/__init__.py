from flask.ext.sandboy import Sandboy
from flask import current_app

from .profile import Profile
from .service import Service
from .notification import Notification
from flask.ext.pushrod import pushrod_view


class APIScaffold(object):

    def init_app(self, app, db, auth):
        def get_jinja_template():
            current_app.logger.info('calling pushrod')
            return 'base.html'

        decorators = [
            auth.login_required,
            pushrod_view(jinja_template=get_jinja_template)
        ]

        sandboy = Sandboy(app, db,
            [Profile, Service, Notification],
            decorators=decorators,
            renderer=None)
        return sandboy
