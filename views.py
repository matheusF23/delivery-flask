
def init_app(app):
    @app.route("/")
    def index():
        return "<h1>Hello, World</h1>"

    @app.route("/contato")
    def contato():
        return "<h1>Página de contato</h1>"
