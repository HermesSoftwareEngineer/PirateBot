import os
from flask import Flask

def create_app(teste_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    from . import chat
    app.register_blueprint(chat.bp)
    app.add_url_rule('/', endpoint='index')

    return app
