from typing import List, Optional
from src.domain.produto.entity import ProdutoEntity
from src.config.database.db import db


class ProdutoRepository:
    def __init__(self):
        self.session = db.session

    def add(self, product: ProdutoEntity) -> ProdutoEntity:
        self.session.add(product)
        self.session.commit()
        return product

    def get(self, product_id: int) -> Optional[ProdutoEntity]:
        return self.session.query(ProdutoEntity).filter_by(id=product_id).first()

    def get_all(self) -> List[ProdutoEntity]:
        return self.session.query(ProdutoEntity).all()

    def update(self, product: ProdutoEntity) -> ProdutoEntity:
        self.session.merge(product)
        self.session.commit()
        return product

    def delete(self, product_id: int) -> None:
        product = self.get(product_id)
        if product:
            self.session.delete(product)
            self.session.commit()
