from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from database import get_db
from models import ContratoAluguel
from schemas import ContratoAluguel as ContratoAluguelSchema

router = APIRouter(prefix="/contratos_aluguel", tags=["Contrato Aluguel"])

# -------------------- Schema de entrada --------------------
class ContratoAluguelIn(BaseModel):
    fk_id_usuario: int
    fk_id_imovel: int
    data_inicio: str  # ou datetime.date se quiser validar datas
    data_fim: str
    valor: float
    # adicione outros campos obrigatórios do modelo ContratoAluguel

# -------------------- CRUD Contrato Aluguel --------------------
@router.post("/", response_model=ContratoAluguelSchema)
def create_contrato_aluguel(contrato: ContratoAluguelIn, db: Session = Depends(get_db)):
    db_contrato = ContratoAluguel(**contrato.dict())
    db.add(db_contrato)
    db.commit()
    db.refresh(db_contrato)
    return db_contrato

@router.get("/", response_model=List[ContratoAluguelSchema])
def read_contratos_aluguel(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(ContratoAluguel).offset(skip).limit(limit).all()

@router.get("/{contrato_id}", response_model=ContratoAluguelSchema)
def read_contrato_aluguel(contrato_id: int, db: Session = Depends(get_db)):
    contrato = db.query(ContratoAluguel).filter(ContratoAluguel.id_contrato_alug == contrato_id).first()
    if not contrato:
        raise HTTPException(status_code=404, detail="Contrato de aluguel não encontrado")
    return contrato

@router.put("/{contrato_id}", response_model=ContratoAluguelSchema)
def update_contrato_aluguel(contrato_id: int, contrato_update: ContratoAluguelIn, db: Session = Depends(get_db)):
    contrato = db.query(ContratoAluguel).filter(ContratoAluguel.id_contrato_alug == contrato_id).first()
    if not contrato:
        raise HTTPException(status_code=404, detail="Contrato de aluguel não encontrado")
    for key, value in contrato_update.dict().items():
        setattr(contrato, key, value)
    db.commit()
    db.refresh(contrato)
    return contrato

@router.delete("/{contrato_id}")
def delete_contrato_aluguel(contrato_id: int, db: Session = Depends(get_db)):
    contrato = db.query(ContratoAluguel).filter(ContratoAluguel.id_contrato_alug == contrato_id).first()
    if not contrato:
        raise HTTPException(status_code=404, detail="Contrato de aluguel não encontrado")
    db.delete(contrato)
    db.commit()
    return {"mensagem": "Contrato de aluguel deletado com sucesso"}
