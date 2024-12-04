from pydantic import BaseModel, Field
from typing import Optional

class UpdateProdutoDTO(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, max_length=50)
    valor: Optional[float] = Field(None, gt=0)
    eletronico: Optional[bool] = Field(None)
