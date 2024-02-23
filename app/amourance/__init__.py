from flask import Flask
from flask import render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello(name=None):
        return render_template('hello.html', name=name)
    return app