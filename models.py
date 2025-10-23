from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class StatusImovel(Base):
    __tablename__ = "status_imovel"
    id_status = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, unique=True, index=True)

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

class Perfil(Base):
    __tablename__ = "perfil"
    id = Column(Integer, primary_key=True, index=True)
    tipo_perf = Column(String, index=True)

class Corretor(Base):
    __tablename__ = "corretor"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

class Imovel(Base):
    __tablename__ = "imovel"
    id = Column(Integer, primary_key=True, index=True)
    endereco = Column(String, index=True)
    tipo = Column(String)
    valor = Column(Float)
    fk_status_id = Column(Integer, ForeignKey("status_imovel.id_status"))
    status = relationship("StatusImovel")

class Visita(Base):
    __tablename__ = "visita"
    id = Column(Integer, primary_key=True, index=True)
    fk_corretor_id = Column(Integer, ForeignKey("corretor.id"))

class ContratoAluguel(Base):
    __tablename__ = "contrato_aluguel"
    id = Column(Integer, primary_key=True, index=True)
    fk_usuario_id = Column(Integer, ForeignKey("usuario.id"))

class ContratoVenda(Base):
    __tablename__ = "contrato_venda"
    id = Column(Integer, primary_key=True, index=True)
    fk_usuario_id = Column(Integer, ForeignKey("usuario.id"))
