from flask.ext.pushrod import Pushrod
from flask.ext.pushrod.renderers import renderer
from flask import render_template

pushrod = Pushrod()


@renderer(name='vcard', mime_type='text/vcard')
def vcard_renderer(unrendered, vcard_template=None, **kwargs):
    if vcard_template:
        if callable(vcard_template):
            vcard_template = vcard_template()
        return unrendered.rendered(
            render_template(vcard_template, **unrendered.response),
            'text/vcard')
    else:
        return NotImplemented


pushrod.register_renderer(vcard_renderer)


def init_app(app):
    pushrod.init_app(app)
