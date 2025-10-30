from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database.database import get_db
from ..models.models import Perfil
from ..schemas.schemas import Perfil as PerfilSchema, PerfilCreate

router = APIRouter(prefix="/perfis", tags=["Perfis"])

@router.post("/", response_model=PerfilSchema, summary="Criar novo perfil")
def create_perfil(perfil: PerfilCreate, db: Session = Depends(get_db)):
    try:
        db_perfil = Perfil(**perfil.model_dump())
        db.add(db_perfil)
        db.commit()
        db.refresh(db_perfil)
        return db_perfil
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao criar perfil: {str(e)}")

@router.get("/", response_model=List[PerfilSchema], summary="Listar perfis")
def read_perfis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return db.query(Perfil).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar perfis: {str(e)}")

@router.get("/{perfil_id}", response_model=PerfilSchema, summary="Buscar perfil pelo ID")
def read_perfil(perfil_id: int, db: Session = Depends(get_db)):
    try:
        perfil = db.query(Perfil).filter(Perfil.id_Perf == perfil_id).first()
        if not perfil:
            raise HTTPException(status_code=404, detail="Perfil nao encontrado")
        return perfil
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar perfil: {str(e)}")

@router.put("/{perfil_id}", response_model=PerfilSchema, summary="Atualizar perfil")
def update_perfil(perfil_id: int, perfil_update: PerfilCreate, db: Session = Depends(get_db)):
    try:
        perfil = db.query(Perfil).filter(Perfil.id_Perf == perfil_id).first()
        if not perfil:
            raise HTTPException(status_code=404, detail="Perfil não encontrado")
        
        perfil_data = perfil_update.model_dump()
        for key, value in perfil_data.items():
            setattr(perfil, key, value)
            
        db.commit()
        db.refresh(perfil)
        return perfil
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar perfil: {str(e)}")

@router.delete("/{perfil_id}", summary="Deletar perfil")
def delete_perfil(perfil_id: int, db: Session = Depends(get_db)):
    try:
        perfil = db.query(Perfil).filter(Perfil.id_Perf == perfil_id).first()
        if not perfil:
            raise HTTPException(status_code=404, detail="Perfil não encontrado")
        db.delete(perfil)
        db.commit()
        return {"mensagem": "Perfil deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao deletar perfil: {str(e)}")
