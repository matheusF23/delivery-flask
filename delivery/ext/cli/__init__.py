import click
from delivery.ext.db import db


def init_app(app):
    @app.cli.command()
    def create_db():
        """Inicializa o db"""
        db.create_all()
