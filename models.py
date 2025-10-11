from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, DECIMAL, CHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Perfil(Base):
    __tablename__ = "Perfil"
    id_Perf = Column(Integer, primary_key=True, index=True)
    tipo_perf = Column(String(50), nullable=False)
    usuarios = relationship("Usuario", back_populates="perfil")

class Usuario(Base):
    __tablename__ = "Usuario"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    sexo = Column(CHAR(1), nullable=False)
    login_usu = Column(String(50), nullable=False)
    senha_usu = Column(String(100), nullable=False)
    fk_Perfil_id = Column(Integer, ForeignKey("Perfil.id_Perf"))
    perfil = relationship("Perfil", back_populates="usuarios")
    corretor = relationship("Corretor", uselist=False, back_populates="usuario")
    visitas = relationship("Visita", back_populates="usuario")
    contratos_aluguel = relationship("Contrato_Aluguel", back_populates="usuario")
    contratos_venda = relationship("Contrato_Venda", back_populates="usuario")

class Corretor(Base):
    __tablename__ = "Corretor"
    id_corretor = Column(Integer, primary_key=True, index=True)
    creci = Column(String(20), nullable=False)
    fk_usuario_id = Column(Integer, ForeignKey("Usuario.id_usuario"))
    usuario = relationship("Usuario", back_populates="corretor")
    imoveis = relationship("Imovel", back_populates="corretor")
    visitas = relationship("Visita", back_populates="corretor")

class Status_Imovel(Base):
    __tablename__ = "Status_Imovel"
    id_status = Column(Integer, primary_key=True, index=True)
    descricao_status = Column(String(100), nullable=False)
    imoveis = relationship("Imovel", back_populates="status")

class Endereco(Base):
    __tablename__ = "Endereco"
    id_endereco = Column(Integer, primary_key=True, index=True)
    logradouro = Column(String(100), nullable=False)
    numero = Column(String(10), nullable=False)
    bairro = Column(String(50), nullable=False)
    complemento = Column(String(50))
    cidade = Column(String(50), nullable=False)
    estado = Column(CHAR(2), nullable=False)
    cep = Column(String(10), nullable=False)
    imoveis = relationship("Imovel", back_populates="endereco")

class Imovel(Base):
    __tablename__ = "Imovel"
    id_imovel = Column(Integer, primary_key=True, index=True)
    area_total = Column(DECIMAL(10,2), nullable=False)
    quarto = Column(Integer, nullable=False)
    banheiro = Column(Integer, nullable=False)
    vaga_garagem = Column(Integer, nullable=False)
    valor = Column(DECIMAL(12,2), nullable=False)
    tipo = Column(String(50), nullable=False)
    desc_tipo_imovel = Column(String(100), nullable=False)
    fk_id_status = Column(Integer, ForeignKey("Status_Imovel.id_status"))
    fk_id_endereco = Column(Integer, ForeignKey("Endereco.id_endereco"))
    fk_id_corretor = Column(Integer, ForeignKey("Corretor.id_corretor"))
    status = relationship("Status_Imovel", back_populates="imoveis")
    endereco = relationship("Endereco", back_populates="imoveis")
    corretor = relationship("Corretor", back_populates="imoveis")
    visitas = relationship("Visita", back_populates="imovel")
    contratos_aluguel = relationship("Contrato_Aluguel", back_populates="imovel")
    contratos_venda = relationship("Contrato_Venda", back_populates="imovel")

class Visita(Base):
    __tablename__ = "Visita"
    id_visita = Column(Integer, primary_key=True, index=True)
    data_visita = Column(Date, nullable=False)
    hora_visita = Column(Time, nullable=False)
    status_visita = Column(String(50), nullable=False)
    fk_id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario"))
    fk_id_corretor = Column(Integer, ForeignKey("Corretor.id_corretor"))
    fk_id_imovel = Column(Integer, ForeignKey("Imovel.id_imovel"))
    usuario = relationship("Usuario", back_populates="visitas")
    corretor = relationship("Corretor", back_populates="visitas")
    imovel = relationship("Imovel", back_populates="visitas")

class Contrato_Aluguel(Base):
    __tablename__ = "Contrato_Aluguel"
    id_contrato_alug = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    valor_mensalidade = Column(DECIMAL(12,2), nullable=False)
    fk_id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario"))
    fk_id_imovel = Column(Integer, ForeignKey("Imovel.id_imovel"))
    usuario = relationship("Usuario", back_populates="contratos_aluguel")
    imovel = relationship("Imovel", back_populates="contratos_aluguel")

class Contrato_Venda(Base):
    __tablename__ = "Contrato_Venda"
    id_contrato_venda = Column(Integer, primary_key=True, index=True)
    tipo_venda = Column(String(50), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    valor_negociado = Column(DECIMAL(12,2), nullable=False)
    fk_id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario"))
    fk_id_imovel = Column(Integer, ForeignKey("Imovel.id_imovel"))
    usuario = relationship("Usuario", back_populates="contratos_venda")
    imovel = relationship("Imovel", back_populates="contratos_venda")
