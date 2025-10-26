from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database.database import get_db
from src.models.models import Imovel
from src.schemas.schemas import Imovel as ImovelSchema, ImovelCreate

router = APIRouter(prefix="/imoveis", tags=["Imóveis"])

@router.post("/", response_model=ImovelSchema)
def create_imovel(imovel: ImovelCreate, db: Session = Depends(get_db)):
    try:
        imovel_data = imovel.model_dump()
        db_imovel = Imovel(**imovel_data)
        db.add(db_imovel)
        db.commit()
        db.refresh(db_imovel)
        return db_imovel
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao criar imóvel: {str(e)}")

@router.get("/", response_model=List[ImovelSchema])
def read_imoveis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return db.query(Imovel).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar imóveis: {str(e)}")

@router.get("/{imovel_id}", response_model=ImovelSchema)
def read_imovel(imovel_id: int, db: Session = Depends(get_db)):
    try:
        imovel = db.query(Imovel).filter(Imovel.id_imovel == imovel_id).first()
        if not imovel:
            raise HTTPException(status_code=404, detail="Imóvel não encontrado")
        return imovel
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar imóvel: {str(e)}")

@router.put("/{imovel_id}", response_model=ImovelSchema)
def update_imovel(imovel_id: int, imovel_update: ImovelCreate, db: Session = Depends(get_db)):
    try:
        imovel = db.query(Imovel).filter(Imovel.id_imovel == imovel_id).first()
        if not imovel:
            raise HTTPException(status_code=404, detail="Imóvel não encontrado")
        
        imovel_data = imovel_update.model_dump()
        for key, value in imovel_data.items():
            setattr(imovel, key, value)
            
        db.commit()
        db.refresh(imovel)
        return imovel
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar imóvel: {str(e)}")

@router.delete("/{imovel_id}")
def delete_imovel(imovel_id: int, db: Session = Depends(get_db)):
    try:
        imovel = db.query(Imovel).filter(Imovel.id_imovel == imovel_id).first()
        if not imovel:
            raise HTTPException(status_code=404, detail="Imóvel não encontrado")
        db.delete(imovel)
        db.commit()
        return {"msg": "Imóvel deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao deletar imóvel: {str(e)}")
