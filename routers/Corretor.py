from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Corretor
from schemas import Corretor as CorretorSchema, CorretorCreate

router = APIRouter(prefix="/corretores", tags=["Corretores"])

@router.post("/", response_model=CorretorSchema)
def create_corretor(corretor: CorretorCreate, db: Session = Depends(get_db)):
    db_corretor = Corretor(**corretor.dict())
    db.add(db_corretor)
    db.commit()
    db.refresh(db_corretor)
    return db_corretor

@router.get("/", response_model=List[CorretorSchema])
def read_corretores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Corretor).offset(skip).limit(limit).all()

@router.get("/{corretor_id}", response_model=CorretorSchema)
def read_corretor(corretor_id: int, db: Session = Depends(get_db)):
    corretor = db.query(Corretor).filter(Corretor.id_corretor == corretor_id).first()
    if not corretor:
        raise HTTPException(status_code=404, detail="Corretor não encontrado")
    return corretor

@router.put("/{corretor_id}", response_model=CorretorSchema)
def update_corretor(corretor_id: int, corretor_update: CorretorCreate, db: Session = Depends(get_db)):
    corretor = db.query(Corretor).filter(Corretor.id_corretor == corretor_id).first()
    if not corretor:
        raise HTTPException(status_code=404, detail="Corretor não encontrado")
    for key, value in corretor_update.dict().items():
        setattr(corretor, key, value)
    db.commit()
    db.refresh(corretor)
    return corretor

@router.delete("/{corretor_id}")
def delete_corretor(corretor_id: int, db: Session = Depends(get_db)):
    corretor = db.query(Corretor).filter(Corretor.id_corretor == corretor_id).first()
    if not corretor:
        raise HTTPException(status_code=404, detail="Corretor não encontrado")
    db.delete(corretor)
    db.commit()
    return {"msg": "Corretor deletado com sucesso"}
