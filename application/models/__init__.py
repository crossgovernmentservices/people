from flask.ext.sandboy import Sandboy
from flask import current_app, request

from .profile import Profile
from .service import Service
from .notification import Notification
from flask.ext.pushrod import pushrod_view


class APIScaffold(object):
    def init_app(self, app, db, auth):
        """
        request.path:
            - /profile/42 == ['','profile','42']
            - /profile == ['','profile']

        """
        def get_jinja_template():
            parts = request.path.rsplit('/')
            tpl = parts[1] + '.html'

            current_app.logger.debug(
                'pushrod retrieving jinja template=%s for path=%s' %
                (tpl, request.path))
            return tpl

        def get_vcard_template():
            parts = request.path.rsplit('/')
            if len(parts) == 2:
                return NotImplemented

            tpl = parts[1] + '.vcard'

            current_app.logger.debug(
                'pushrod retrieving vcard template=%s for path=%s' %
                (tpl, request.path))
            return tpl

        decorators = [
            auth.login_required,
            pushrod_view(jinja_template=get_jinja_template, vcard_template=get_vcard_template)
        ]

        sandboy = Sandboy(app, db, [Profile, Service, Notification],
                          decorators=decorators,
                          renderer=None)
        return sandboy
