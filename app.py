from flask import Flask

# app = Flask("delivery")
app = Flask(__name__) # Vai o nome do pacote (delivery-flask)

@app.route("/")
def index():
    return "<h1>Hello, World</h1>"
