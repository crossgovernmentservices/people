from flask.ext.sandboy import Sandboy

from .profile import Profile
from .service import Service
from .notification import Notification


class APIScaffold(object):

    def init_app(self, app, db, auth):
        sandboy = Sandboy(app, db,
            [Profile, Service, Notification],
            decorators=[auth.login_required])
        return sandboy
