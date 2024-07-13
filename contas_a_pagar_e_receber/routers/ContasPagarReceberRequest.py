from pydantic import BaseModel
from decimal import Decimal

class ContasPagarReceberRequest(BaseModel):
    description: str
    valor: Decimal
    tipo: str