from flask import Flask
from src.config.settings.environment import Environment
from src.config.database import db
from src.application.produto import ProdutoController

def create_app():
    app = Flask(__name__)
    app.config.from_object(Environment)
    db.init_app(app)

    produto_controller = ProdutoController()
    app.register_blueprint(produto_controller.blueprint)

    with app.app_context():
        db.create_all()
    
    return app