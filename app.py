import views
from flask import Flask


def create_app():
    app = Flask(__name__)  # Vai o nome do pacote (delivery-flask)
    views.init_app(app)
    return app
