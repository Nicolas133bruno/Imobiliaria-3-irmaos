from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Usuario, Perfil, Corretor, Imovel, Visita, Contrato_Aluguel, Contrato_Venda
from schemas import (
    Usuario as UsuarioSchema,
    Perfil as PerfilSchema,
    Corretor as CorretorSchema,
    Imovel as ImovelSchema,
    Visita as VisitaSchema,
    ContratoAluguel as ContratoAluguelSchema,
    ContratoVenda as ContratoVendaSchema
)

router = APIRouter(prefix="/consultas", tags=["Consultas"])

@router.get("/usuarios", response_model=List[UsuarioSchema])
def consultar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.get("/perfils", response_model=List[PerfilSchema])
def consultar_perfils(db: Session = Depends(get_db)):
    return db.query(Perfil).all()

@router.get("/corretores", response_model=List[CorretorSchema])
def consultar_corretores(db: Session = Depends(get_db)):
    return db.query(Corretor).all()

@router.get("/imoveis", response_model=List[ImovelSchema])
def consultar_imoveis(db: Session = Depends(get_db)):
    return db.query(Imovel).all()

@router.get("/visitas", response_model=List[VisitaSchema])
def consultar_visitas(db: Session = Depends(get_db)):
    return db.query(Visita).all()

@router.get("/contratos_aluguel", response_model=List[ContratoAluguelSchema])
def consultar_contratos_aluguel(db: Session = Depends(get_db)):
    return db.query(Contrato_Aluguel).all()

@router.get("/contratos_venda", response_model=List[ContratoVendaSchema])
def consultar_contratos_venda(db: Session = Depends(get_db)):
    return db.query(Contrato_Venda).all()
