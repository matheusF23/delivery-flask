from delivery.ext.auth import models # noqa
from delivery.ext.auth.commands import add_user

def init_app(app):
    """ TODO: inicializar Flask Simple Login + JWT"""
    app.cli.command()(add_user)