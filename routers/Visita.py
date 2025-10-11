from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Visita
from schemas import Visita as VisitaSchema, VisitaCreate

router = APIRouter(prefix="/visitas", tags=["Visitas"])

@router.post("/", response_model=VisitaSchema)
def create_visita(visita: VisitaCreate, db: Session = Depends(get_db)):
    db_visita = Visita(**visita.dict())
    db.add(db_visita)
    db.commit()
    db.refresh(db_visita)
    return db_visita

@router.get("/", response_model=List[VisitaSchema])
def read_visitas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    visitas = db.query(Visita).offset(skip).limit(limit).all()
    return visitas

@router.get("/{visita_id}", response_model=VisitaSchema)
def read_visita(visita_id: int, db: Session = Depends(get_db)):
    visita = db.query(Visita).filter(Visita.id_visita == visita_id).first()
    if not visita:
        raise HTTPException(status_code=404, detail="Visita não encontrada")
    return visita

@router.put("/{visita_id}", response_model=VisitaSchema)
def update_visita(visita_id: int, visita_update: VisitaCreate, db: Session = Depends(get_db)):
    visita = db.query(Visita).filter(Visita.id_visita == visita_id).first()
    if not visita:
        raise HTTPException(status_code=404, detail="Visita não encontrada")
    for key, value in visita_update.dict().items():
        setattr(visita, key, value)
    db.commit()
    db.refresh(visita)
    return visita

@router.delete("/{visita_id}")
def delete_visita(visita_id: int, db: Session = Depends(get_db)):
    visita = db.query(Visita).filter(Visita.id_visita == visita_id).first()
    if not visita:
        raise HTTPException(status_code=404, detail="Visita não encontrada")
    db.delete(visita)
    db.commit()
    return {"msg": "Visita deletada com sucesso"}

visita_router = router
