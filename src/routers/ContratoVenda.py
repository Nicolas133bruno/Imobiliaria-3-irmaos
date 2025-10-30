from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database.database import get_db
from ..models.models import ContratoVenda
from ..schemas.schemas import ContratoVenda as ContratoVendaSchema, ContratoVendaCreate

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

@router.get("/")
def read_contratos_venda(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        contratos = db.query(ContratoVenda).offset(skip).limit(limit).all()
        
        # Se não houver contratos, retornar dados de exemplo
        if not contratos:
            return [
                {
                    "id_contrato_venda": 1,
                    "tipo_venda": "À Vista",
                    "data_inicio": "2025-03-10",
                    "data_fim": "2025-03-10",
                    "valor_negociado": 450000.00,
                    "fk_id_usuario": 1,
                    "fk_id_imovel": 2
                },
                {
                    "id_contrato_venda": 2,
                    "tipo_venda": "Financiado",
                    "data_inicio": "2025-04-15",
                    "data_fim": "2025-04-15",
                    "valor_negociado": 320000.00,
                    "fk_id_usuario": 3,
                    "fk_id_imovel": 4
                }
            ]
        
        # Converter para dicionários
        result = []
        for contrato in contratos:
            result.append({
                "id_contrato_venda": contrato.id_contrato_venda,
                "tipo_venda": contrato.tipo_venda,
                "data_inicio": str(contrato.data_inicio),
                "data_fim": str(contrato.data_fim),
                "valor_negociado": float(contrato.valor_negociado),
                "fk_id_usuario": contrato.fk_id_usuario,
                "fk_id_imovel": contrato.fk_id_imovel
            })
            
        return result
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
