from delivery.ext.db import db
from delivery.ext.site import models


def init_app(app):
    @app.cli.command()
    def create_db():
        """Inicializa o db"""
        db.create_all()
