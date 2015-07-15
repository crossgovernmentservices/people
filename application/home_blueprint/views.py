from flask import (
    Blueprint,
)
from flask.ext.pushrod import pushrod_view


blueprint = Blueprint(
    'home',
    __name__,
    template_folder='templates')


@blueprint.route('/')
@pushrod_view(jinja_template='index.html')
def index():
    return {'msg':'todo home page stuff'}
