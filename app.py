import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from home.views import home


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    if os.environ.get("FLASK_ENV", None) == "development":
        app.config.from_object("config.DevelopmentConfig")
    else:
        app.config.from_object("config.ProductionConfig")

    return app


app = create_app()
app.register_blueprint(home)
