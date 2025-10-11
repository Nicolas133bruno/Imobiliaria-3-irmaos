from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import ContratoVenda
from schemas import ContratoVenda as ContratoVendaSchema, ContratoVendaCreate

router = APIRouter(prefix="/contratos_venda", tags=["Contrato Venda"])

@router.post("/", response_model=ContratoVendaSchema)
def create_contrato_venda(contrato: ContratoVendaCreate, db: Session = Depends(get_db)):
    db_contrato = ContratoVenda(**contrato.dict())
    db.add(db_contrato)
    db.commit()
    db.refresh(db_contrato)
    return db_contrato

@router.get("/", response_model=List[ContratoVendaSchema])
def read_contratos_venda(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contratos = db.query(ContratoVenda).offset(skip).limit(limit).all()
    return contratos

@router.get("/{contrato_id}", response_model=ContratoVendaSchema)
def read_contrato_venda(contrato_id: int, db: Session = Depends(get_db)):
    contrato = db.query(ContratoVenda).filter(ContratoVenda.id_contrato_venda == contrato_id).first()
    if not contrato:
        raise HTTPException(status_code=404, detail="Contrato de venda não encontrado")
    return contrato

@router.put("/{contrato_id}", response_model=ContratoVendaSchema)
def update_contrato_venda(contrato_id: int, contrato_update: ContratoVendaCreate, db: Session = Depends(get_db)):
    contrato = db.query(ContratoVenda).filter(ContratoVenda.id_contrato_venda == contrato_id).first()
    if not contrato:
        raise HTTPException(status_code=404, detail="Contrato de venda não encontrado")
    for key, value in contrato_update.dict().items():
        setattr(contrato, key, value)
    db.commit()
    db.refresh(contrato)
    return contrato

@router.delete("/{contrato_id}")
def delete_contrato_venda(contrato_id: int, db: Session = Depends(get_db)):
    contrato = db.query(ContratoVenda).filter(ContratoVenda.id_contrato_venda == contrato_id).first()
    if not contrato:
        raise HTTPException(status_code=404, detail="Contrato de venda não encontrado")
    db.delete(contrato)
    db.commit()
    return {"msg": "Contrato de venda deletado com sucesso"}

contrato_venda_router = router
