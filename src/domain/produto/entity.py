from src.config.database.db import db
from sqlalchemy import Boolean, DateTime, Float, Integer, String
from datetime import datetime

class ProdutoEntity(db.Model):
    __tablename__ = "produto"
    id = db.Column(Integer, primary_key=True)
    nome = db.Column(String(50), nullable=False)
    valor = db.Column(Float, nullable=False)
    eletronico = db.Column(Boolean, nullable=False)
    data_criacao = db.Column(DateTime, nullable=False)
    data_atualizacao = db.Column(DateTime, nullable=True)
    deletado = db.Column(Boolean, nullable=False)
    data_delecao = db.Column(DateTime, nullable=True)
    

    def __init__(self, nome: str, valor: float,  eletronico: bool, data_criacao: datetime):
        self.nome = nome
        self.valor = valor
        self.eletronico = eletronico
        self.data_criacao = data_criacao
        self.deletado = False


    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "valor": self.valor,
            "eletronico": self.eletronico,
            "data_criacao": self.data_criacao.isoformat() if self.data_criacao else None,
            "data_atualizacao": self.data_atualizacao.isoformat() if self.data_atualizacao else None,
            "deletado": self.deletado,
            "data_delecao": self.data_delecao.isoformat() if self.data_delecao else None
        }