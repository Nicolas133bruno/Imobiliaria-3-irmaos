from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.database.database import get_db
from src.models.models import Visita
from src.schemas.schemas import Visita as VisitaSchema, VisitaCreate
from datetime import datetime

router = APIRouter(prefix="/visitas", tags=["Visitas"])

@router.post("/", response_model=VisitaSchema)
def create_visita(visita: VisitaCreate, db: Session = Depends(get_db)):
    try:
        visita_dict = visita.model_dump()
        # Converter a string de hora para objeto Time
        if isinstance(visita_dict["hora_visita"], str):
            try:
                hora_obj = datetime.strptime(visita_dict["hora_visita"], "%H:%M:%S").time()
                # Não convertemos para time, mantemos como string conforme o schema
            except ValueError:
                try:
                    hora_obj = datetime.strptime(visita_dict["hora_visita"], "%H:%M").time()
                    # Formatamos de volta para string no formato HH:MM:SS
                    visita_dict["hora_visita"] = hora_obj.strftime("%H:%M:%S")
                except ValueError:
                    raise HTTPException(status_code=400, detail="Formato de hora inválido. Use HH:MM:SS ou HH:MM")
        
        db_visita = Visita(**visita_dict)
        db.add(db_visita)
        db.commit()
        db.refresh(db_visita)
        
        # Garantir que hora_visita seja retornado como string
        if hasattr(db_visita, 'hora_visita') and not isinstance(db_visita.hora_visita, str):
            db_visita.hora_visita = db_visita.hora_visita.strftime("%H:%M:%S")
            
        return db_visita
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar visita: {str(e)}")

@router.get("/", response_model=List[VisitaSchema])
def read_visitas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        visitas = db.query(Visita).offset(skip).limit(limit).all()
        
        # Converter hora_visita para string em cada visita
        for visita in visitas:
            if hasattr(visita, 'hora_visita') and not isinstance(visita.hora_visita, str):
                visita.hora_visita = visita.hora_visita.strftime("%H:%M:%S")
                
        return visitas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar visitas: {str(e)}")

@router.get("/{visita_id}", response_model=VisitaSchema)
def read_visita(visita_id: int, db: Session = Depends(get_db)):
    try:
        visita = db.query(Visita).filter(Visita.id_visita == visita_id).first()
        if not visita:
            raise HTTPException(status_code=404, detail="Visita não encontrada")
            
        # Converter hora_visita para string
        if hasattr(visita, 'hora_visita') and not isinstance(visita.hora_visita, str):
            visita.hora_visita = visita.hora_visita.strftime("%H:%M:%S")
            
        return visita
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar visita: {str(e)}")

@router.put("/{visita_id}", response_model=VisitaSchema)
def update_visita(visita_id: int, visita_update: VisitaCreate, db: Session = Depends(get_db)):
    try:
        visita = db.query(Visita).filter(Visita.id_visita == visita_id).first()
        if not visita:
            raise HTTPException(status_code=404, detail="Visita não encontrada")
        
        visita_dict = visita_update.model_dump()
        # Converter a string de hora para objeto Time para o banco de dados
        if isinstance(visita_dict["hora_visita"], str):
            try:
                hora_obj = datetime.strptime(visita_dict["hora_visita"], "%H:%M:%S").time()
                visita_dict["hora_visita"] = hora_obj
            except ValueError:
                try:
                    hora_obj = datetime.strptime(visita_dict["hora_visita"], "%H:%M").time()
                    visita_dict["hora_visita"] = hora_obj
                except ValueError:
                    raise HTTPException(status_code=400, detail="Formato de hora inválido. Use HH:MM:SS ou HH:MM")
        
        for key, value in visita_dict.items():
            setattr(visita, key, value)
        
        db.commit()
        db.refresh(visita)
        
        # Converter hora_visita para string para a resposta
        if hasattr(visita, 'hora_visita') and not isinstance(visita.hora_visita, str):
            visita.hora_visita = visita.hora_visita.strftime("%H:%M:%S")
            
        return visita
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar visita: {str(e)}")

@router.delete("/{visita_id}")
def delete_visita(visita_id: int, db: Session = Depends(get_db)):
    try:
        visita = db.query(Visita).filter(Visita.id_visita == visita_id).first()
        if not visita:
            raise HTTPException(status_code=404, detail="Visita não encontrada")
        db.delete(visita)
        db.commit()
        return {"msg": "Visita deletada com sucesso"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao deletar visita: {str(e)}")
