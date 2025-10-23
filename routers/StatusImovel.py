# routers/status_imovel.py
from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy.orm import Session
from typing import Optional, List
from pydantic import BaseModel
from database import get_db
from models import StatusImovel
from schemas import StatusImovel as StatusImovelSchema, PaginatedResponse

router = APIRouter(
    prefix="/status_imovel",
    tags=["Status Imóvel"]
)

# -------------------- Schema de entrada --------------------
class StatusImovelIn(BaseModel):
    descricao: str

# -------------------- CRUD Status Imóvel --------------------
@router.post("/", response_model=StatusImovelSchema, status_code=status.HTTP_201_CREATED)
def create_status_imovel(status_data: StatusImovelIn, db: Session = Depends(get_db)):
    existente = db.query(StatusImovel).filter(StatusImovel.descricao == status_data.descricao).first()
    if existente:
        raise HTTPException(status_code=409, detail="Status do imóvel já existe")
    novo_status = StatusImovel(**status_data.dict())
    db.add(novo_status)
    db.commit()
    db.refresh(novo_status)
    return novo_status

@router.get("/", response_model=PaginatedResponse[StatusImovelSchema])
def read_status_imoveis(request: Request, db: Session = Depends(get_db),
                        limit: int = Query(10, ge=1), offset: int = Query(0, ge=0),
                        order_by: Optional[str] = Query("id_status")):
    if order_by not in ["id_status", "descricao"]:
        raise HTTPException(status_code=400, detail="Campo de ordenação inválido")
    total = db.query(StatusImovel).count()
    items = db.query(StatusImovel).order_by(getattr(StatusImovel, order_by)).offset(offset).limit(limit).all()
    base_url = str(request.url).split("?")[0]
    next_offset = offset + limit
    prev_offset = offset - limit if offset - limit >= 0 else None
    next_url = f"{base_url}?limit={limit}&offset={next_offset}&order_by={order_by}" if next_offset < total else None
    prev_url = f"{base_url}?limit={limit}&offset={prev_offset}&order_by={order_by}" if prev_offset is not None else None
    return {"total": total, "limit": limit, "offset": offset, "next": next_url, "previous": prev_url, "items": items}

@router.get("/{status_id}", response_model=StatusImovelSchema)
def read_status_imovel(status_id: int, db: Session = Depends(get_db)):
    status_obj = db.query(StatusImovel).filter(StatusImovel.id_status == status_id).first()
    if not status_obj:
        raise HTTPException(status_code=404, detail="Status do imóvel não encontrado")
    return status_obj

@router.put("/{status_id}", response_model=StatusImovelSchema)
def update_status_imovel(status_id: int, status_update: StatusImovelIn, db: Session = Depends(get_db)):
    status_obj = db.query(StatusImovel).filter(StatusImovel.id_status == status_id).first()
    if not status_obj:
        raise HTTPException(status_code=404, detail="Status do imóvel não encontrado")
    for key, value in status_update.dict().items():
        setattr(status_obj, key, value)
    db.commit()
    db.refresh(status_obj)
    return status_obj

@router.delete("/{status_id}", response_model=dict[str, str])
def delete_status_imovel(status_id: int, db: Session = Depends(get_db)):
    status_obj = db.query(StatusImovel).filter(StatusImovel.id_status == status_id).first()
    if not status_obj:
        raise HTTPException(status_code=404, detail="Status do imóvel não encontrado")
    db.delete(status_obj)
    db.commit()
    return {"mensagem": "Status do imóvel deletado com sucesso"}
