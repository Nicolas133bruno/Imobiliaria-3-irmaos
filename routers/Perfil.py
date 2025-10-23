from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Perfil
from schemas import Perfil as PerfilSchema, PerfilCreate

router = APIRouter(prefix="/perfils", tags=["Perfils"])

@router.post("/", response_model=PerfilSchema)
def create_perfil(perfil: PerfilCreate, db: Session = Depends(get_db)):
    db_perfil = Perfil(**perfil.dict())
    db.add(db_perfil)
    db.commit()
    db.refresh(db_perfil)
    return db_perfil

@router.get("/", response_model=List[PerfilSchema])
def read_perfils(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Perfil).offset(skip).limit(limit).all()

@router.get("/{perfil_id}", response_model=PerfilSchema)
def read_perfil(perfil_id: int, db: Session = Depends(get_db)):
    perfil = db.query(Perfil).filter(Perfil.id_Perf == perfil_id).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    return perfil

@router.put("/{perfil_id}", response_model=PerfilSchema)
def update_perfil(perfil_id: int, perfil_update: PerfilCreate, db: Session = Depends(get_db)):
    perfil = db.query(Perfil).filter(Perfil.id_Perf == perfil_id).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    for key, value in perfil_update.dict().items():
        setattr(perfil, key, value)
    db.commit()
    db.refresh(perfil)
    return perfil

@router.delete("/{perfil_id}")
def delete_perfil(perfil_id: int, db: Session = Depends(get_db)):
    perfil = db.query(Perfil).filter(Perfil.id_Perf == perfil_id).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    db.delete(perfil)
    db.commit()
    return {"msg": "Perfil deletado com sucesso"}
