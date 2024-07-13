from pydantic import BaseModel
from decimal import Decimal

class ContasPagarReceberResponse(BaseModel):
    id: int
    description: str
    valor: Decimal
    tipo: str