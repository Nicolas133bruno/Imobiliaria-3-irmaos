from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database.database import get_db
from src.models.models import Endereco
from src.schemas.schemas import Endereco as EnderecoSchema, EnderecoCreate

router = APIRouter(prefix="/enderecos", tags=["Enderecos"])

# -------------------- CRUD Enderecos --------------------
@router.post("/", response_model=EnderecoSchema, summary="Criar novo endereço")
def create_endereco(endereco: EnderecoCreate, db: Session = Depends(get_db)):
    try:
        db_endereco = Endereco(**endereco.model_dump())
        db.add(db_endereco)
        db.commit()
        db.refresh(db_endereco)
        return db_endereco
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao criar endereço: {str(e)}")

@router.get("/", response_model=List[EnderecoSchema], summary="Listar enderecos")
def read_enderecos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return db.query(Endereco).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar endereços: {str(e)}")

@router.get("/{endereco_id}", response_model=EnderecoSchema, summary="Buscar endereco pelo ID")
def read_endereco(endereco_id: int, db: Session = Depends(get_db)):
    try:
        endereco = db.query(Endereco).filter(Endereco.id_endereco == endereco_id).first()
        if not endereco:
            raise HTTPException(status_code=404, detail="Endereco nao encontrado")
        return endereco
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar endereço: {str(e)}")

@router.put("/{endereco_id}", response_model=EnderecoSchema, summary="Atualizar endereco")
def update_endereco(endereco_id: int, endereco_update: EnderecoCreate, db: Session = Depends(get_db)):
    try:
        endereco = db.query(Endereco).filter(Endereco.id_endereco == endereco_id).first()
        if not endereco:
            raise HTTPException(status_code=404, detail="Endereco nao encontrado")
        for key, value in endereco_update.model_dump().items():
            setattr(endereco, key, value)
        db.commit()
        db.refresh(endereco)
        return endereco
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao atualizar endereço: {str(e)}")

@router.delete("/{endereco_id}", summary="Deletar endereco")
def delete_endereco(endereco_id: int, db: Session = Depends(get_db)):
    try:
        endereco = db.query(Endereco).filter(Endereco.id_endereco == endereco_id).first()
        if not endereco:
            raise HTTPException(status_code=404, detail="Endereco nao encontrado")
        db.delete(endereco)
        db.commit()
        return {"mensagem": "Endereco deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Erro ao deletar endereço: {str(e)}")

# -------------------- Busca por Cidade --------------------
@router.get("/cidade/{cidade}", response_model=List[EnderecoSchema], summary="Buscar enderecos por cidade")
def read_enderecos_by_cidade(cidade: str, db: Session = Depends(get_db)):
    try:
        enderecos = db.query(Endereco).filter(Endereco.cidade.ilike(f"%{cidade}%")).all()
        return enderecos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar endereços por cidade: {str(e)}")

# -------------------- Busca por Estado --------------------
@router.get("/estado/{estado}", response_model=List[EnderecoSchema], summary="Buscar enderecos por estado")
def read_enderecos_by_estado(estado: str, db: Session = Depends(get_db)):
    try:
        enderecos = db.query(Endereco).filter(Endereco.estado.ilike(f"%{estado}%")).all()
        return enderecos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar endereços por estado: {str(e)}")
