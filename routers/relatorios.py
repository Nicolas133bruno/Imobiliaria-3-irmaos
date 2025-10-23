# routers/relatorios.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models import Usuario, Perfil, Corretor, Imovel, Visita, ContratoAluguel, ContratoVenda, StatusImovel

router = APIRouter(
    prefix="/relatorios",
    tags=["Relatórios"]
)

# =========================
# Usuários com total de contratos
# =========================
@router.get("/usuarios_com_contratos")
def usuarios_com_contratos(db: Session = Depends(get_db)):
    resultado = (
        db.query(
            Usuario.nome,
            func.count(ContratoAluguel.id).label("total_contratos_aluguel"),
            func.count(ContratoVenda.id).label("total_contratos_venda")
        )
        .outerjoin(ContratoAluguel, Usuario.id == ContratoAluguel.fk_usuario_id)
        .outerjoin(ContratoVenda, Usuario.id == ContratoVenda.fk_usuario_id)
        .group_by(Usuario.id)
        .all()
    )
    return resultado

# =========================
# Imóveis com status
# =========================
@router.get("/imoveis_com_status")
def imoveis_com_status(db: Session = Depends(get_db)):
    resultado = (
        db.query(
            Imovel.endereco,
            Imovel.tipo,
            Imovel.valor,
            StatusImovel.descricao.label("status")
        )
        .join(StatusImovel, Imovel.fk_status_id == StatusImovel.id)
        .all()
    )
    return resultado

# =========================
# Visitas por corretor
# =========================
@router.get("/visitas_por_corretor")
def visitas_por_corretor(db: Session = Depends(get_db)):
    resultado = (
        db.query(
            Corretor.nome,
            func.count(Visita.id).label("total_visitas")
        )
        .join(Visita, Corretor.id == Visita.fk_corretor_id)
        .group_by(Corretor.id)
        .all()
    )
    return resultado

# =========================
# Contratos de aluguel ativos
# =========================
@router.get("/contratos_aluguel_ativos")
def contratos_aluguel_ativos(db: Session = Depends(get_db)):
    from datetime import date
    hoje = date.today()
    resultado = (
        db.query(
            Usuario.nome.label("usuario"),
            Imovel.endereco.label("imovel"),
            ContratoAluguel.data_inicio,
            ContratoAluguel.data_fim,
            ContratoAluguel.valor
        )
        .join(Usuario, ContratoAluguel.fk_usuario_id == Usuario.id)
        .join(Imovel, ContratoAluguel.fk_imovel_id == Imovel.id)
        .filter(ContratoAluguel.data_fim >= hoje)
        .all()
    )
    return resultado

# =========================
# Contratos de venda
# =========================
@router.get("/contratos_venda")
def contratos_venda(db: Session = Depends(get_db)):
    resultado = (
        db.query(
            Usuario.nome.label("usuario"),
            Imovel.endereco.label("imovel"),
            ContratoVenda.data,
            ContratoVenda.valor
        )
        .join(Usuario, ContratoVenda.fk_usuario_id == Usuario.id)
        .join(Imovel, ContratoVenda.fk_imovel_id == Imovel.id)
        .all()
    )
    return resultado

# =========================
# Quantidade de imóveis por status
# =========================
@router.get("/imoveis_por_status")
def imoveis_por_status(db: Session = Depends(get_db)):
    resultado = (
        db.query(
            StatusImovel.descricao,
            func.count(Imovel.id).label("total_imoveis")
        )
        .join(Imovel, StatusImovel.id == Imovel.fk_status_id)
        .group_by(StatusImovel.id)
        .all()
    )
    return resultado

# =========================
# Usuários com perfil
# =========================
@router.get("/usuarios_com_perfil")
def usuarios_com_perfil(db: Session = Depends(get_db)):
    resultado = (
        db.query(
            Usuario.nome,
            Perfil.tipo.label("perfil")
        )
        .join(Perfil, Usuario.fk_perfil_id == Perfil.id)
        .all()
    )
    return resultado
