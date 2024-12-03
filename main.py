import os
from flask import Flask, jsonify
from src.config.database import db
import src.domain
from src.domain.produto.entity import ProdutoEntity
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    """Factory para criar e configurar a aplicação."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Rota simples para teste
    @app.route('/hello')
    def hello():
        new_object = ProdutoEntity(
            nome="obj1",
            valor=100.0,
            data=datetime.datetime.today(),
            eletronico=True
        )

        # Salvando no banco de dados
        db.session.add(new_object)
        db.session.commit()

        return jsonify({
            "message": "Novo objeto criado!",
            "object": {
                "id": new_object.id,
                "nome": new_object.nome,
                "valor": new_object.valor,
                "data": new_object.data,
                "eletronico": new_object.eletronico
            }
        })

    return app

app = create_app()
with app.app_context():
    # Criar as tabelas no banco de dados
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
