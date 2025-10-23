from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional, Generic, TypeVar, List

# -------------------- Paginação genérica --------------------
T = TypeVar("T")

class PaginatedResponse(BaseModel, Generic[T]):
    total: int
    limit: int
    offset: int
    next: Optional[str]
    previous: Optional[str]
    items: List[T]

# -------------------- Perfil --------------------
class PerfilBase(BaseModel):
    tipo: str

class PerfilCreate(PerfilBase):
    pass

class Perfil(PerfilBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Usuario --------------------
class UsuarioBase(BaseModel):
    nome: str
    cpf: str
    telefone: str
    email: str
    data_nascimento: date
    sexo: str
    login_usu: str
    senha_usu: str
    fk_perfil_id: int

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Corretor --------------------
class CorretorBase(BaseModel):
    creci: str
    fk_usuario_id: int

class CorretorCreate(CorretorBase):
    pass

class Corretor(CorretorBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- StatusImovel --------------------
class StatusImovelBase(BaseModel):
    descricao: str

class StatusImovelCreate(StatusImovelBase):
    pass

class StatusImovel(StatusImovelBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Imovel --------------------
class ImovelBase(BaseModel):
    area_total: Decimal
    quarto: int
    banheiro: int
    vaga_garagem: int
    valor: Decimal
    tipo: str
    desc_tipo_imovel: str
    fk_status_id: int
    fk_corretor_id: int

class ImovelCreate(ImovelBase):
    pass

class Imovel(ImovelBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Visita --------------------
class VisitaBase(BaseModel):
    data_visita: date
    hora_visita: str
    status_visita: str
    fk_usuario_id: int
    fk_corretor_id: int
    fk_imovel_id: int

class VisitaCreate(VisitaBase):
    pass

class Visita(VisitaBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Contrato Aluguel --------------------
class ContratoAluguelBase(BaseModel):
    tipo: str
    data_inicio: date
    data_fim: date
    valor_mensalidade: Decimal
    fk_usuario_id: int
    fk_corretor_id: int
    fk_imovel_id: int

class ContratoAluguelCreate(ContratoAluguelBase):
    pass

class ContratoAluguel(ContratoAluguelBase):
    id: int
    class Config:
        orm_mode = True

# -------------------- Contrato Venda --------------------
class ContratoVendaBase(BaseModel):
    tipo_venda: str
    data_inicio: date
    data_fim: date
    valor_negociado: Decimal
    fk_usuario_id: int
    fk_corretor_id: int
    fk_imovel_id: int

class ContratoVendaCreate(ContratoVendaBase):
    pass

class ContratoVenda(ContratoVendaBase):
    id: int
    class Config:
        orm_mode = True
