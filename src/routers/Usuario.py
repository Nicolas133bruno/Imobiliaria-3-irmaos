
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func
from pydantic import BaseModel

from src.database.database import get_db
from src.models.models import Usuario, ContratoAluguel
from src.schemas.schemas import Usuario as UsuarioSchema, UsuarioCreate, UsuarioUpdate, UsuarioLogin

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# -------------------- CRUD Usuarios --------------------


@router.post("/", response_model=UsuarioSchema, summary="Criar novo usuario")
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        hashed_password = usuario.senha_usu # Temporarily store the plain password
        usuario_data = usuario.model_dump(exclude={'senha_usu'})
        db_usuario = Usuario(**usuario_data)
        db_usuario.set_senha(hashed_password) # Hash the password
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400, detail=f"Erro ao criar usuário: {str(e)}"
        )


@router.get("/", response_model=List[UsuarioSchema],
            summary="Listar usuarios")
def read_usuarios(skip: int = 0, limit: int = 100,
                  db: Session = Depends(get_db)):
    try:
        return db.query(Usuario).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao listar usuários: {str(e)}"
        )


@router.get("/{usuario_id}", response_model=UsuarioSchema,
            summary="Buscar usuario pelo ID")
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        usuario = db.query(Usuario).filter(
            Usuario.id_usuario == usuario_id
        ).first()
        if not usuario:
            raise HTTPException(
                status_code=404, detail="Usuário não encontrado"
            )
        return usuario
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao buscar usuário: {str(e)}"
        )


@router.put("/{usuario_id}", response_model=UsuarioSchema,
            summary="Atualizar usuario")
def update_usuario(usuario_id: int, usuario_update: UsuarioUpdate,
                   db: Session = Depends(get_db)):
    try:
        usuario = db.query(Usuario).filter(
            Usuario.id_usuario == usuario_id
        ).first()
        if not usuario:
            raise HTTPException(
                status_code=404, detail="Usuário não encontrado"
            )

        update_data = usuario_update.model_dump(exclude_unset=True)
        if "senha_usu" in update_data:
            usuario.set_senha(update_data["senha_usu"])
            del update_data["senha_usu"]

        for key, value in update_data.items():
            setattr(usuario, key, value)

        db.commit()
        db.refresh(usuario)
        return usuario
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400, detail=f"Erro ao atualizar usuário: {str(e)}"
        )


@router.delete("/{usuario_id}", summary="Deletar usuario")
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    try:
        usuario = db.query(Usuario).filter(
            Usuario.id_usuario == usuario_id
        ).first()
        if not usuario:
            raise HTTPException(
                status_code=404, detail="Usuário não encontrado"
            )
        db.delete(usuario)
        db.commit()
        return {"mensagem": "Usuário deletado com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400, detail=f"Erro ao deletar usuário: {str(e)}"
        )


@router.post("/login", summary="Autenticar usuário e gerar token (simulado)")
def login_usuario(usuario_login: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.login_usu == usuario_login.login_usu).first()
    if not usuario or not usuario.verify_senha(usuario_login.senha_usu):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    # Em um cenário real, um token JWT seria gerado aqui
    return {"mensagem": "Login bem-sucedido", "usuario_id": usuario.id_usuario}


# -------------------- Relatorio: Contratos Ativos --------------------


class UsuarioContratos(BaseModel):
    nome: str
    total_contratos_ativos: int


@router.get("/contratos-ativos", response_model=List[UsuarioContratos],
            summary="Listar total de contratos ativos por usuario")
def contratos_ativos(db: Session = Depends(get_db)):
    try:
        results = (
            db.query(
                Usuario.nome,
                func.count(ContratoAluguel.id_contrato_alug).label(
                    "total_contratos_ativos"
                )
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar contratos ativos: {str(e)}")
