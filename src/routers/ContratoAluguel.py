from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from src.database.database import get_db
from src.models.models import ContratoAluguel
from src.schemas.schemas import ContratoAluguelCreate, ContratoAluguel as ContratoAluguelSchema

router = APIRouter(prefix="/contratos_aluguel", tags=["Contrato Aluguel"])

# -------------------- CRUD Contrato Aluguel --------------------
@router.post("/", response_model=ContratoAluguelSchema)
def create_contrato_aluguel(contrato: ContratoAluguelCreate, db: Session = Depends(get_db)):
    try:
        # Criando um dicionário com os dados do contrato
        contrato_data = contrato.model_dump()
        
        # Criando o objeto ContratoAluguel
        db_contrato = ContratoAluguel(**contrato_data)
        db.add(db_contrato)
        db.commit()
        db.refresh(db_contrato)
        return db_contrato
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao criar contrato de aluguel: {str(e)}")

@router.get("/", response_model=List[ContratoAluguelSchema])
def read_contratos_aluguel(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return db.query(ContratoAluguel).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar contratos de aluguel: {str(e)}")

@router.get("/{contrato_id}", response_model=ContratoAluguelSchema)
def read_contrato_aluguel(contrato_id: int, db: Session = Depends(get_db)):
    try:
        contrato = db.query(ContratoAluguel).filter(ContratoAluguel.id_contrato_alug == contrato_id).first()
        if not contrato:
            raise HTTPException(status_code=404, detail="Contrato de aluguel não encontrado")
        return contrato
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar contrato de aluguel: {str(e)}")

@router.put("/{contrato_id}", response_model=ContratoAluguelSchema)
def update_contrato_aluguel(contrato_id: int, contrato_update: ContratoAluguelCreate, db: Session = Depends(get_db)):
    try:
        contrato = db.query(ContratoAluguel).filter(ContratoAluguel.id_contrato_alug == contrato_id).first()
        if not contrato:
            raise HTTPException(status_code=404, detail="Contrato de aluguel não encontrado")
        
        # Atualizando os campos do contrato
        contrato_data = contrato_update.model_dump()
        for key, value in contrato_data.items():
            setattr(contrato, key, value)
            
        db.commit()
        db.refresh(contrato)
        return contrato
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar contrato de aluguel: {str(e)}")

@router.delete("/{contrato_id}")
def delete_contrato_aluguel(contrato_id: int, db: Session = Depends(get_db)):
    try:
        contrato = db.query(ContratoAluguel).filter(ContratoAluguel.id_contrato_alug == contrato_id).first()
        if not contrato:
            raise HTTPException(status_code=404, detail="Contrato de aluguel não encontrado")
        db.delete(contrato)
        db.commit()
        return {"mensagem": "Contrato de aluguel deletado com sucesso"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao deletar contrato de aluguel: {str(e)}")
