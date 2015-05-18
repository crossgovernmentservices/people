from flask.ext.sandboy import Sandboy

from .profile import Profile

class APIScaffold(object):

    def init_app(self, app, db):
        sandboy = Sandboy(app, db,
            [Profile])
        return sandboy
