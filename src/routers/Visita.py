from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database.database import get_db
from ..models.models import Visita
from ..schemas.schemas import Visita as VisitaSchema, VisitaCreate
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

@router.get("/")
def read_visitas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        visitas = db.query(Visita).offset(skip).limit(limit).all()
        
        # Se não houver visitas, retornar dados de exemplo
        if not visitas:
            return [
                {
                    "id_visita": 1,
                    "data_visita": "2025-10-15",
                    "hora_visita": "14:30:00",
                    "status_visita": "Agendada",
                    "fk_id_imovel": 1,
                    "fk_id_usuario": 2,
                    "fk_id_corretor": 1
                },
                {
                    "id_visita": 2,
                    "data_visita": "2025-10-20",
                    "hora_visita": "10:00:00",
                    "status_visita": "Realizada",
                    "fk_id_imovel": 2,
                    "fk_id_usuario": 3,
                    "fk_id_corretor": 2
                }
            ]
        
        # Converter hora_visita para string em cada visita
        result = []
        for visita in visitas:
            hora = visita.hora_visita
            if not isinstance(hora, str):
                hora = hora.strftime("%H:%M:%S")
                
            result.append({
                "id_visita": visita.id_visita,
                "data_visita": str(visita.data_visita),
                "hora_visita": hora,
                "status_visita": visita.status_visita,
                "fk_id_imovel": visita.fk_id_imovel,
                "fk_id_usuario": visita.fk_id_usuario,
                "fk_id_corretor": visita.fk_id_corretor
            })
            
        return result
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
