from pydantic import BaseModel, Field
from typing import Optional

class CreateProdutoDTO(BaseModel):
    nome: str = Field(..., min_length=1, max_length=50)
    valor: float = Field(..., ge=0)
    eletronico: bool = Field(...)
