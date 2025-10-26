from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Time, DECIMAL
from sqlalchemy.orm import relationship
from passlib.hash import bcrypt
from src.database.database import Base

class Perfil(Base):
    __tablename__ = "Perfil"
    id_Perf = Column(Integer, primary_key=True, index=True)
    tipo_perf = Column(String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<Perfil(id_Perf={self.id_Perf}, tipo_perf='{self.tipo_perf}')>"

    # Relacionamento
    usuarios = relationship("Usuario", back_populates="perfil")

class Usuario(Base):
    __tablename__ = "Usuario"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), nullable=False, unique=True)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    data_nascimento = Column(Date)
    sexo = Column(String(1))
    login_usu = Column(String(50), nullable=False, unique=True)
    senha_usu = Column(String(100), nullable=False)
    fk_Perfil_id = Column(Integer, ForeignKey("Perfil.id_Perf"), index=True, nullable=False)
    
    def __repr__(self):
        return f"<Usuario(id_usuario={self.id_usuario}, nome='{self.nome}', email='{self.email}')>"

    def set_senha(self, senha):
        self.senha_usu = bcrypt.hash(senha)

    def verify_senha(self, senha):
        return bcrypt.verify(senha, self.senha_usu)

    # Relacionamentos
    perfil = relationship("Perfil", back_populates="usuarios")
    corretor = relationship("Corretor", back_populates="usuario", uselist=False)
    visitas = relationship("Visita", back_populates="usuario")
    contratos_aluguel = relationship("ContratoAluguel", back_populates="usuario")
    contratos_venda = relationship("ContratoVenda", back_populates="usuario")

class Corretor(Base):
    __tablename__ = "Corretor"
    id_corretor = Column(Integer, primary_key=True, index=True)
    creci = Column(String(20), nullable=False, unique=True)
    fk_usuario_id = Column(Integer, ForeignKey("Usuario.id_usuario"), index=True, nullable=False)
    
    def __repr__(self):
        return f"<Corretor(id_corretor={self.id_corretor}, creci='{self.creci}')>"

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="corretor")
    imoveis = relationship("Imovel", back_populates="corretor")
    visitas = relationship("Visita", back_populates="corretor")

class StatusImovel(Base):
    __tablename__ = "Status_Imovel"
    id_status = Column(Integer, primary_key=True, index=True)
    descricao_status = Column(String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<StatusImovel(id_status={self.id_status}, descricao_status='{self.descricao_status}')>"

    # Relacionamento
    imoveis = relationship("Imovel", back_populates="status")

class Endereco(Base):
    __tablename__ = "Endereco"
    id_endereco = Column(Integer, primary_key=True, index=True)
    logradouro = Column(String(100), nullable=False)
    numero = Column(String(10), nullable=False)
    bairro = Column(String(50), nullable=False)
    complemento = Column(String(50))
    cidade = Column(String(50), nullable=False)
    estado = Column(String(2), nullable=False)
    cep = Column(String(10), nullable=False)
    
    def __repr__(self):
        return f"<Endereco(id_endereco={self.id_endereco}, cidade='{self.cidade}', estado='{self.estado}')>"

    # Relacionamento
    imoveis = relationship("Imovel", back_populates="endereco")

class Imovel(Base):
    __tablename__ = "Imovel"
    id_imovel = Column(Integer, primary_key=True, index=True)
    area_total = Column(DECIMAL(10,2), nullable=False)
    quarto = Column(Integer)
    banheiro = Column(Integer)
    vaga_garagem = Column(Integer)
    valor = Column(DECIMAL(12,2), nullable=False)
    tipo = Column(String(50), nullable=False)
    desc_tipo_imovel = Column(String(100))
    fk_id_status = Column(Integer, ForeignKey("Status_Imovel.id_status"), index=True, nullable=False)
    fk_id_endereco = Column(Integer, ForeignKey("Endereco.id_endereco"), index=True, nullable=False)
    fk_id_corretor = Column(Integer, ForeignKey("Corretor.id_corretor"), index=True, nullable=False)
    
    def __repr__(self):
        return f"<Imovel(id_imovel={self.id_imovel}, tipo='{self.tipo}', valor={self.valor})>"

    # Relacionamentos
    status = relationship("StatusImovel", back_populates="imoveis")
    endereco = relationship("Endereco", back_populates="imoveis")
    corretor = relationship("Corretor", back_populates="imoveis")
    visitas = relationship("Visita", back_populates="imovel")
    contratos_aluguel = relationship("ContratoAluguel", back_populates="imovel")
    contratos_venda = relationship("ContratoVenda", back_populates="imovel")

class Visita(Base):
    __tablename__ = "Visita"
    id_visita = Column(Integer, primary_key=True, index=True)
    data_visita = Column(Date, nullable=False)
    hora_visita = Column(Time, nullable=False)
    status_visita = Column(String(50), nullable=False)
    fk_id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario"), index=True, nullable=False)
    fk_id_corretor = Column(Integer, ForeignKey("Corretor.id_corretor"), index=True, nullable=False)
    fk_id_imovel = Column(Integer, ForeignKey("Imovel.id_imovel"), index=True, nullable=False)
    
    def __repr__(self):
        return f"<Visita(id_visita={self.id_visita}, data_visita='{self.data_visita}', hora_visita='{self.hora_visita}')>"

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="visitas")
    corretor = relationship("Corretor", back_populates="visitas")
    imovel = relationship("Imovel", back_populates="visitas")

class ContratoAluguel(Base):
    __tablename__ = "Contrato_Aluguel"
    id_contrato_alug = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    valor_mensalidade = Column(DECIMAL(12,2), nullable=False)
    fk_id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario"), index=True, nullable=False)
    fk_id_imovel = Column(Integer, ForeignKey("Imovel.id_imovel"), index=True, nullable=False)
    
    def __repr__(self):
        return f"<ContratoAluguel(id_contrato_alug={self.id_contrato_alug}, tipo='{self.tipo}', valor_mensalidade={self.valor_mensalidade})>"

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="contratos_aluguel")
    imovel = relationship("Imovel", back_populates="contratos_aluguel")

class ContratoVenda(Base):
    __tablename__ = "Contrato_Venda"
    id_contrato_venda = Column(Integer, primary_key=True, index=True)
    tipo_venda = Column(String(50), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    valor_negociado = Column(DECIMAL(12,2), nullable=False)
    fk_id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario"), index=True, nullable=False)
    fk_id_imovel = Column(Integer, ForeignKey("Imovel.id_imovel"), index=True, nullable=False)
    
    def __repr__(self):
        return f"<ContratoVenda(id_contrato_venda={self.id_contrato_venda}, tipo_venda='{self.tipo_venda}', valor_negociado={self.valor_negociado})>"

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="contratos_venda")
    imovel = relationship("Imovel", back_populates="contratos_venda")
