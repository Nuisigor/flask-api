import os
from flask import Flask
from flasgger import Swagger
from src.config.settings.environment import Environment
from src.config.database import db
from src.application.produto import ProdutoController

def create_app():
    app = Flask(__name__)
    app.config.from_object(Environment)
    db.init_app(app)

    yaml_path = os.path.join(os.path.dirname(__file__), "swagger.yml")
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec",
                "route": "/apispec.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/",
    }
    Swagger(app, template_file=yaml_path, config=swagger_config)

    produto_controller = ProdutoController()
    app.register_blueprint(produto_controller.blueprint)

    with app.app_context():
        db.create_all()

    return app
