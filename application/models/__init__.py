from flask.ext.sandboy import Sandboy

from .profile import Profile
from .service import Service


class APIScaffold(object):

    def init_app(self, app, db, auth):
        sandboy = Sandboy(app, db,
            [Profile, Service],
            decorators=[auth.login_required])
        return sandboy
