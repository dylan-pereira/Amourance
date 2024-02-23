from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return f"<p>Hello, World!</p>"

    return app




 
 # Path: app/amourance/__init__.py