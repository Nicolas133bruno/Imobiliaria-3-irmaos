# routers/relatorios.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database.database import get_db
from ..models.models import (Usuario, Perfil, Corretor, Imovel, Visita,
                    ContratoAluguel, ContratoVenda, StatusImovel)

router = APIRouter(
    prefix="/relatorios",
    tags=["Relatórios"]
)

# =========================
# Usuários com total de contratos
# =========================


@router.get("/usuarios_com_contratos")
def usuarios_com_contratos(db: Session = Depends(get_db)):
    try:
        resultado = (
            db.query(
                Usuario.nome,
                func.count(ContratoAluguel.id_contrato_alug).label(
                    "total_contratos_aluguel"
                ),
                func.count(ContratoVenda.id_contrato_venda).label(
                    "total_contratos_venda"
                )
            )
            .outerjoin(
                ContratoAluguel,
                Usuario.id_usuario == ContratoAluguel.fk_id_usuario
            )
            .outerjoin(
                ContratoVenda,
                Usuario.id_usuario == ContratoVenda.fk_id_usuario
            )
            .group_by(Usuario.id_usuario)
            .all()
        )
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao gerar relatório de usuários com contratos: {str(e)}"
        )

# =========================
# Imóveis com status
# =========================


@router.get("/imoveis_com_status")
def imoveis_com_status(db: Session = Depends(get_db)):
    try:
        resultado = (
            db.query(
                Imovel.desc_tipo_imovel,
                Imovel.tipo,
                Imovel.valor,
                StatusImovel.descricao_status.label("status")
            )
            .join(
                StatusImovel,
                Imovel.fk_id_status == StatusImovel.id_status
            )
            .all()
        )
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao gerar relatório de imóveis com status: {str(e)}"
        )

# =========================
# Visitas por corretor
# =========================


@router.get("/visitas_por_corretor")
def visitas_por_corretor(db: Session = Depends(get_db)):
    try:
        resultado = (
            db.query(
                Usuario.nome,
                func.count(Visita.id_visita).label("total_visitas")
            )
            .join(
                Corretor,
                Usuario.id_usuario == Corretor.fk_usuario_id
            )
            .join(
                Visita,
                Corretor.id_corretor == Visita.fk_id_corretor
            )
            .group_by(Usuario.id_usuario)
            .all()
        )
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao gerar relatório de visitas por corretor: {str(e)}"
        )

# =========================
# Contratos de aluguel ativos
# =========================


@router.get("/contratos_aluguel_ativos")
def contratos_aluguel_ativos(db: Session = Depends(get_db)):
    try:
        from datetime import date
        hoje = date.today()
        resultado = (
            db.query(ContratoAluguel)
            .filter(ContratoAluguel.data_fim >= hoje)
            .all()
        )
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao gerar relatório de contratos de aluguel ativos: {str(e)}"
        )


# =========================
# Contratos de venda
# =========================


@router.get("/contratos_venda")
def contratos_venda(db: Session = Depends(get_db)):
    try:
        resultado = (
            db.query(
                Usuario.nome.label("usuario"),
                Imovel.desc_tipo_imovel.label("imovel"),
                ContratoVenda.data_inicio,
                ContratoVenda.valor_negociado
            )
            .join(
                Usuario,
                ContratoVenda.fk_id_usuario == Usuario.id_usuario
            )
            .join(
                Imovel,
                ContratoVenda.fk_id_imovel == Imovel.id_imovel
            )
            .all()
        )
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao gerar relatório de contratos de venda: {str(e)}"
        )

# =========================
# Quantidade de imóveis por status
# =========================


@router.get("/imoveis_por_status")
def imoveis_por_status(db: Session = Depends(get_db)):
    try:
        resultado = (
            db.query(
                StatusImovel.descricao_status,
                func.count(Imovel.id_imovel).label("total_imoveis")
            )
            .join(
                Imovel,
                StatusImovel.id_status == Imovel.fk_id_status
            )
            .group_by(StatusImovel.id_status)
            .all()
        )
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao gerar relatório de imóveis por status: {str(e)}"
        )

# =========================
# Usuários com perfil
# =========================


@router.get("/usuarios_com_perfil")
def usuarios_com_perfil(db: Session = Depends(get_db)):
    try:
        resultado = (
            db.query(
                Usuario.nome,
                Perfil.tipo_perf.label("perfil")
            )
            .join(
                Perfil,
                Usuario.fk_Perfil_id == Perfil.id_Perf
            )
            .all()
        )
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao gerar relatório de usuários com perfil: {str(e)}"
        )
