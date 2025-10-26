from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database.database import get_db
from src.models.models import Corretor
from src.schemas.schemas import Corretor as CorretorSchema, CorretorCreate

router = APIRouter(prefix="/corretores", tags=["Corretores"])

@router.post("/", response_model=CorretorSchema, summary="Criar novo corretor")
def create_corretor(corretor: CorretorCreate, db: Session = Depends(get_db)):
    try:
        corretor_data = corretor.model_dump()
        db_corretor = Corretor(**corretor_data)
        db.add(db_corretor)
        db.commit()
        db.refresh(db_corretor)
        return db_corretor
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao criar corretor: {str(e)}")

@router.get("/", response_model=List[CorretorSchema], summary="Listar corretores")
def read_corretores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return db.query(Corretor).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar corretores: {str(e)}")

@router.get("/{corretor_id}", response_model=CorretorSchema, summary="Buscar corretor pelo ID")
def read_corretor(corretor_id: int, db: Session = Depends(get_db)):
    try:
        corretor = db.query(Corretor).filter(Corretor.id_corretor == corretor_id).first()
        if not corretor:
            raise HTTPException(status_code=404, detail="Corretor não encontrado")
        return corretor
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar corretor: {str(e)}")

@router.put("/{corretor_id}", response_model=CorretorSchema, summary="Atualizar corretor")
def update_corretor(corretor_id: int, corretor_update: CorretorCreate, db: Session = Depends(get_db)):
    try:
        corretor = db.query(Corretor).filter(Corretor.id_corretor == corretor_id).first()
        if not corretor:
            raise HTTPException(status_code=404, detail="Corretor não encontrado")
        
        corretor_data = corretor_update.model_dump()
        for key, value in corretor_data.items():
            setattr(corretor, key, value)
            
        db.commit()
        db.refresh(corretor)
        return corretor
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar corretor: {str(e)}")

@router.delete("/{corretor_id}", summary="Deletar corretor")
def delete_corretor(corretor_id: int, db: Session = Depends(get_db)):
    try:
        corretor = db.query(Corretor).filter(Corretor.id_corretor == corretor_id).first()
        if not corretor:
            raise HTTPException(status_code=404, detail="Corretor não encontrado")
        db.delete(corretor)
        db.commit()
        return {"mensagem": "Corretor deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao deletar corretor: {str(e)}")
