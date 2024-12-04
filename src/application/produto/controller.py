from flask import Blueprint, jsonify, request
from src.config.settings.middleware.auth import ApiKeyMiddleware
from src.application.produto.service import ProdutoService
from src.application.produto.dtos import CreateProdutoDTO, UpdateProdutoDTO

class ProdutoController:
    def __init__(self):
        self.service = ProdutoService()
        self.middleware = ApiKeyMiddleware()

        self.blueprint = Blueprint("produto", __name__, url_prefix="/produto")

        self.blueprint.add_url_rule("/", methods=["GET"], view_func=self.get_all)
        self.blueprint.add_url_rule("/<int:id>", methods=["GET"], view_func=self.get_by_id)
        self.blueprint.add_url_rule("/", methods=["POST"], view_func=self.middleware(self.create), endpoint="create_produto")
        self.blueprint.add_url_rule("/<int:id>", methods=["PATCH"], view_func=self.middleware(self.update), endpoint="update_produto")
        self.blueprint.add_url_rule("/<int:id>", methods=["DELETE"], view_func=self.middleware(self.delete), endpoint="delete_produto")

    def get_all(self):
        try:
            products = self.service.get_all()
            
            return jsonify(products), 200
        except Exception as e:
            return jsonify({"message": f"Erro: {str(e)}"}), 400

    def get_by_id(self, id):
        product = self.service.get_by_id(id)
        if not product:
            return jsonify({"message": "Produto não encontrado"}), 404
        
        return jsonify(product.to_dict()), 200

    def create(self):
        try:
            data = request.get_json()
            product_dto = CreateProdutoDTO(**data)
            new_product = self.service.create(product_dto)
            
            return jsonify({
                "message": "Produto criado com sucesso!",
                "data": new_product.to_dict()
            }), 201   
        except Exception as e:
            return jsonify({"message": f"Erro: {str(e)}"}), 400

    def update(self, id):
        try:
            data = request.get_json()
            product_update_dto = UpdateProdutoDTO(**data)
            updated_product = self.service.update(id, product_update_dto)
            
            if updated_product is None:
                return jsonify({"message": "Produto não encontrado"}), 404
            
            return jsonify({
                "message": "Produto atualizado com sucesso!",
                "produto": updated_product.to_dict()
            }), 200
        except Exception as e:
            return jsonify({"message": f"Erro: {str(e)}"}), 400

    def delete(self, id):
        if self.service.delete(id):
            return jsonify({"message": "Produto deletado com sucesso!"}), 200
        return jsonify({"message": "Produto não encontrado"}), 404
