from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database.database import get_db
from src.models.models import ContratoVenda
from src.schemas.schemas import ContratoVenda as ContratoVendaSchema, ContratoVendaCreate

router = APIRouter(prefix="/contratos_venda", tags=["Contrato Venda"])

@router.post("/", response_model=ContratoVendaSchema)
def create_contrato_venda(contrato: ContratoVendaCreate, db: Session = Depends(get_db)):
    try:
        contrato_data = contrato.model_dump()
        db_contrato = ContratoVenda(**contrato_data)
        db.add(db_contrato)
        db.commit()
        db.refresh(db_contrato)
        return db_contrato
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao criar contrato de venda: {str(e)}")

@router.get("/", response_model=List[ContratoVendaSchema])
def read_contratos_venda(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return db.query(ContratoVenda).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar contratos de venda: {str(e)}")

@router.get("/{contrato_id}", response_model=ContratoVendaSchema)
def read_contrato_venda(contrato_id: int, db: Session = Depends(get_db)):
    try:
        contrato = db.query(ContratoVenda).filter(ContratoVenda.id_contrato_venda == contrato_id).first()
        if not contrato:
            raise HTTPException(status_code=404, detail="Contrato de venda não encontrado")
        return contrato
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar contrato de venda: {str(e)}")

@router.put("/{contrato_id}", response_model=ContratoVendaSchema)
def update_contrato_venda(contrato_id: int, contrato_update: ContratoVendaCreate, db: Session = Depends(get_db)):
    try:
        contrato = db.query(ContratoVenda).filter(ContratoVenda.id_contrato_venda == contrato_id).first()
        if not contrato:
            raise HTTPException(status_code=404, detail="Contrato de venda não encontrado")
        
        contrato_data = contrato_update.model_dump()
        for key, value in contrato_data.items():
            setattr(contrato, key, value)
            
        db.commit()
        db.refresh(contrato)
        return contrato
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar contrato de venda: {str(e)}")

@router.delete("/{contrato_id}")
def delete_contrato_venda(contrato_id: int, db: Session = Depends(get_db)):
    try:
        contrato = db.query(ContratoVenda).filter(ContratoVenda.id_contrato_venda == contrato_id).first()
        if not contrato:
            raise HTTPException(status_code=404, detail="Contrato de venda não encontrado")
        db.delete(contrato)
        db.commit()
        return {"msg": "Contrato de venda deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao deletar contrato de venda: {str(e)}")
