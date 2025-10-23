
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from sqlalchemy import func

from database import get_db
from models import Usuario, ContratoAluguel
from schemas import Usuario as UsuarioSchema

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

# -------------------- Schema para criação/atualização --------------------
class UsuarioIn(BaseModel):
    nome: str
    email: str
    senha: str
    # adicione outros campos necessários do seu model Usuario

# -------------------- CRUD Usuários --------------------
@router.post("/", response_model=UsuarioSchema, summary="Criar novo usuário")
def create_usuario(usuario: UsuarioIn, db: Session = Depends(get_db)):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.get("/", response_model=List[UsuarioSchema], summary="Listar usuários")
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Usuario).offset(skip).limit(limit).all()

@router.get("/{usuario_id}", response_model=UsuarioSchema, summary="Buscar usuário pelo ID")
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=UsuarioSchema, summary="Atualizar usuário")
def update_usuario(usuario_id: int, usuario_update: UsuarioIn, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    for key, value in usuario_update.dict().items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.delete("/{usuario_id}", summary="Deletar usuário")
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensagem": "Usuário deletado com sucesso"}

# -------------------- Relatório: Contratos Ativos --------------------
class UsuarioContratos(BaseModel):
    nome: str
    total_contratos_ativos: int

@router.get("/contratos-ativos", response_model=List[UsuarioContratos], summary="Listar total de contratos ativos por usuário")
def contratos_ativos(db: Session = Depends(get_db)):
    results = (
        db.query(
            Usuario.nome,
            func.count(ContratoAluguel.id_contrato_alug).label("total_contratos_ativos")
        )
        .outerjoin(
            ContratoAluguel,
            (ContratoAluguel.fk_id_usuario == Usuario.id_usuario) &
            (ContratoAluguel.data_fim >= func.current_date())
        )
        .group_by(Usuario.nome)
        .all()
    )
    return results
