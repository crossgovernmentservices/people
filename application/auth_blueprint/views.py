"""
Login, and for Flask-HTTPAuth hooks.

"""

from flask import (
    Blueprint,
    request,
    jsonify,
    abort
)
from ..extensions import auth, db


blueprint = Blueprint(
    'auth',
    __name__)#,
#    url_prefix='/')

@blueprint.route('/session', methods=['POST'])
def session():
    email = request.get_json()['email']

    db.session.execute('CREATE SCHEMA IF NOT EXISTS "%s"' % email)
    db.session.execute('SET search_path TO "%s"' % email)
    db.session.commit()

    with blueprint.app.app_context():
        db.create_all()
        db.session.commit()

    # short-circuit
    return jsonify({'msg': 'success', 'status_code': 201}), 201

@auth.get_password
def get_password(username):
    """
    Return the password for *username*.
    Since DB reads/writes are only allowed for logged-in or potential
    users, it's OK to set the search_path here.

    """
    if not username:
        abort(401)

    # this works, because all Sandboy models are decorated,
    db.session.execute('SET search_path TO "%s"' % username)

    # short-circuit - we don't have auth yet.
    return 'hunter2'
