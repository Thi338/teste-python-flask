
from fastapi import APIRouter
from typing import List
from contas_a_pagar_e_receber.routers.ContasPagarReceberResponse import ContasPagarReceberResponse
from contas_a_pagar_e_receber.routers.ContasPagarReceberRequest import ContasPagarReceberRequest

router = APIRouter(prefix='/contas-a-pagar-e-receber')


@router.get("/", response_model=List[ContasPagarReceberResponse])
def listar_contas():
    return [
        ContasPagarReceberResponse(
            id=1, 
            description="Aluguel",
            valor=1000.50,
            tipo="PAGAR"
        ),
        ContasPagarReceberResponse(
            id=2, 
            description="Salário",
            valor=5000,
            tipo="RECEBER"
        )
    ]

@router.post("/", response_model=ContasPagarReceberResponse, status_code=201)
def criar_conta(conta: ContasPagarReceberRequest):
    return ContasPagarReceberResponse(
            id=3, 
            description=conta.description,
            valor=conta.valor,
            tipo=conta.tipo
        )


criar_conta()