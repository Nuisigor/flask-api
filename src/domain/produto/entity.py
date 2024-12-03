from src.config.database.db import db
from sqlalchemy import Boolean, DateTime, Float, Integer, String
from datetime import datetime

class ProdutoEntity(db.Model):
    __tablename__ = "produto"
    id = db.Column(Integer, primary_key=True)
    nome = db.Column(String(50), nullable=False)
    valor = db.Column(Float, nullable=False)
    data = db.Column(DateTime, nullable=False)
    eletronico = db.Column(Boolean, nullable=False)

    def __init__(self, nome: str, valor: float, data: datetime, eletronico: bool):
        self.nome = nome
        self.valor = valor
        self.data = data
        self.eletronico = eletronico

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "valor": self.valor,
            "data": self.data.isoformat() if self.data else None,
            "eletronico": self.eletronico
        }