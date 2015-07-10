from flask.ext.sandboy import Sandboy
from flask import current_app, request

from .profile import Profile
from .service import Service
from .notification import Notification
from flask.ext.pushrod import pushrod_view


class APIScaffold(object):
    def init_app(self, app, db, auth):
        def get_jinja_template():
            """
            # /profile/42 == ['','profile','42']
            # /profile == ['','profile']
            """
            parts = request.path.rsplit('/')
            tpl = parts[1] + '.html'

            current_app.logger.debug(
                'pushrod retrieving template=%s for path=%s' %
                (tpl, request.path))
            return tpl

        decorators = [
            auth.login_required,
            pushrod_view(jinja_template=get_jinja_template)
        ]

        sandboy = Sandboy(app, db, [Profile, Service, Notification],
                          decorators=decorators,
                          renderer=None)
        return sandboy
