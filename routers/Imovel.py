from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Imovel
from schemas import Imovel as ImovelSchema, ImovelCreate

router = APIRouter(prefix="/imoveis", tags=["Imóveis"])

@router.post("/", response_model=ImovelSchema)
def create_imovel(imovel: ImovelCreate, db: Session = Depends(get_db)):
    db_imovel = Imovel(**imovel.dict())
    db.add(db_imovel)
    db.commit()
    db.refresh(db_imovel)
    return db_imovel

@router.get("/", response_model=List[ImovelSchema])
def read_imoveis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Imovel).offset(skip).limit(limit).all()

@router.get("/{imovel_id}", response_model=ImovelSchema)
def read_imovel(imovel_id: int, db: Session = Depends(get_db)):
    imovel = db.query(Imovel).filter(Imovel.id_imovel == imovel_id).first()
    if not imovel:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    return imovel

@router.put("/{imovel_id}", response_model=ImovelSchema)
def update_imovel(imovel_id: int, imovel_update: ImovelCreate, db: Session = Depends(get_db)):
    imovel = db.query(Imovel).filter(Imovel.id_imovel == imovel_id).first()
    if not imovel:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    for key, value in imovel_update.dict().items():
        setattr(imovel, key, value)
    db.commit()
    db.refresh(imovel)
    return imovel

@router.delete("/{imovel_id}")
def delete_imovel(imovel_id: int, db: Session = Depends(get_db)):
    imovel = db.query(Imovel).filter(Imovel.id_imovel == imovel_id).first()
    if not imovel:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    db.delete(imovel)
    db.commit()
    return {"msg": "Imóvel deletado com sucesso"}
