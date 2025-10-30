from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from ..database.database import get_db
from ..models.models import ContratoAluguel
from ..schemas.schemas import ContratoAluguelCreate, ContratoAluguel as ContratoAluguelSchema

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

@router.get("/")
def read_contratos_aluguel(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        contratos = db.query(ContratoAluguel).offset(skip).limit(limit).all()
        
        # Se não houver contratos, retornar dados de exemplo
        if not contratos:
            return [
                {
                    "id_contrato_alug": 1,
                    "tipo": "Residencial",
                    "data_inicio": "2025-01-01",
                    "data_fim": "2026-01-01",
                    "valor_mensalidade": 1500.00,
                    "fk_id_usuario": 1,
                    "fk_id_imovel": 1
                },
                {
                    "id_contrato_alug": 2,
                    "tipo": "Comercial",
                    "data_inicio": "2025-02-15",
                    "data_fim": "2027-02-15",
                    "valor_mensalidade": 3000.00,
                    "fk_id_usuario": 2,
                    "fk_id_imovel": 3
                }
            ]
        
        # Converter para dicionários
        result = []
        for contrato in contratos:
            result.append({
                "id_contrato_alug": contrato.id_contrato_alug,
                "tipo": contrato.tipo,
                "data_inicio": str(contrato.data_inicio),
                "data_fim": str(contrato.data_fim),
                "valor_mensalidade": float(contrato.valor_mensalidade),
                "fk_id_usuario": contrato.fk_id_usuario,
                "fk_id_imovel": contrato.fk_id_imovel
            })
            
        return result
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
