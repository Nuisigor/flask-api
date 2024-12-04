

from datetime import datetime
from src.domain.produto.entity import ProdutoEntity
from src.domain.produto.repository import ProdutoRepository
from src.application.produto.dtos import CreateProdutoDTO, UpdateProdutoDTO


class ProdutoService:
    def __init__(self, produto_repository: ProdutoRepository = ProdutoRepository()):
        self.produto_repository = produto_repository

    def get_all(self):
        return [ product.to_dict() for product in self.produto_repository.get_all() if product.deletado == False]

    def get_by_id(self, id):
        product = self.produto_repository.get(id)
        if not product or product.deletado:
            return None
        return product
       

    def create(self, produto: CreateProdutoDTO):
        new_product = ProdutoEntity(
            nome=produto.nome,
            valor=produto.valor,
            eletronico=produto.eletronico,
            data_criacao=datetime.now()
        )
        return self.produto_repository.add(new_product)

    def update(self, id, produto: UpdateProdutoDTO):
        product = self.produto_repository.get(id)
        if not product:
            return None
        
        product.nome = produto.nome if produto.nome is not None else product.nome
        product.valor = produto.valor if produto.valor is not None else product.valor
        product.eletronico = produto.eletronico if produto.eletronico is not None else product.eletronico
        product.data_atualizacao = datetime.now()
        
        return self.produto_repository.update(product)

    def delete(self, id):
        product = self.produto_repository.get(id)
        if not product or product.deletado:
            return False
        
        product.deletado = True
        product.data_delecao = datetime.now()
        self.produto_repository.update(product)
        return True