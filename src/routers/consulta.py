from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel

from ..database.database import get_db
from ..models.models import Usuario, Perfil, Corretor, Imovel, Visita, ContratoAluguel, ContratoVenda, StatusImovel, Endereco
from ..schemas.schemas import (
    Usuario as UsuarioSchema,
    Perfil as PerfilSchema,
    Corretor as CorretorSchema,
    Imovel as ImovelSchema,
    Visita as VisitaSchema,
    ContratoAluguel as ContratoAluguelSchema,
    ContratoVenda as ContratoVendaSchema
)

router = APIRouter(prefix="/consulta", tags=["Consulta"])

@router.get("/usuarios", response_model=List[UsuarioSchema])
def consultar_usuarios(db: Session = Depends(get_db)):
    try:
        return db.query(Usuario).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao consultar usuários: {str(e)}"
        )

@router.get("/perfis", response_model=List[PerfilSchema])
def consultar_perfis(db: Session = Depends(get_db)):
    try:
        return db.query(Perfil).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao consultar perfis: {str(e)}"
        )

@router.get("/corretores", response_model=List[CorretorSchema])
def consultar_corretores(db: Session = Depends(get_db)):
    try:
        return db.query(Corretor).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao consultar corretores: {str(e)}"
        )

@router.get("/imoveis", response_model=List[ImovelSchema])
def consultar_imoveis(db: Session = Depends(get_db)):
    try:
        return db.query(Imovel).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao consultar imóveis: {str(e)}"
        )

@router.get("/visitas", response_model=List[VisitaSchema])
def consultar_visitas(db: Session = Depends(get_db)):
    try:
        return db.query(Visita).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao consultar visitas: {str(e)}"
        )

@router.get("/contratos_aluguel", response_model=List[ContratoAluguelSchema])
def consultar_contratos_aluguel(db: Session = Depends(get_db)):
    try:
        return db.query(ContratoAluguel).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao consultar contratos de aluguel: {str(e)}"
        )

@router.get("/contratos_venda", response_model=List[ContratoVendaSchema])
def consultar_contratos_venda(db: Session = Depends(get_db)):
    try:
        return db.query(ContratoVenda).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao consultar contratos de venda: {str(e)}"
        )
