from pydantic import BaseModel
from typing import Optional
from datetime import date, time
from decimal import Decimal

class PerfilBase(BaseModel):
    tipo_perf: str

class PerfilCreate(PerfilBase):
    pass

class Perfil(PerfilBase):
    id_Perf: int
    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nome: str
    cpf: str
    telefone: str
    email: str
    data_nascimento: date
    sexo: str
    login_usu: str
    senha_usu: str
    fk_Perfil_id: int

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id_usuario: int
    class Config:
        orm_mode = True

class CorretorBase(BaseModel):
    creci: str
    fk_usuario_id: int

class CorretorCreate(CorretorBase):
    pass

class Corretor(CorretorBase):
    id_corretor: int
    class Config:
        orm_mode = True

class StatusImovelBase(BaseModel):
    descricao_status: str

class StatusImovelCreate(StatusImovelBase):
    pass

class StatusImovel(StatusImovelBase):
    id_status: int
    class Config:
        orm_mode = True

class EnderecoBase(BaseModel):
    logradouro: str
    numero: str
    bairro: str
    complemento: Optional[str] = None
    cidade: str
    estado: str
    cep: str

class EnderecoCreate(EnderecoBase):
    pass

class Endereco(EnderecoBase):
    id_endereco: int
    class Config:
        orm_mode = True

class ImovelBase(BaseModel):
    area_total: Decimal
    quarto: int
    banheiro: int
    vaga_garagem: int
    valor: Decimal
    tipo: str
    desc_tipo_imovel: str
    fk_id_status: int
    fk_id_endereco: int
    fk_id_corretor: int

class ImovelCreate(ImovelBase):
    pass

class Imovel(ImovelBase):
    id_imovel: int
    class Config:
        orm_mode = True

class VisitaBase(BaseModel):
    data_visita: date
    hora_visita: time
    status_visita: str
    fk_id_usuario: int
    fk_id_corretor: int
    fk_id_imovel: int

class VisitaCreate(VisitaBase):
    pass

class Visita(VisitaBase):
    id_visita: int
    class Config:
        orm_mode = True

class ContratoAluguelBase(BaseModel):
    tipo: str
    data_inicio: date
    data_fim: date
    valor_mensalidade: Decimal
    fk_id_usuario: int
    fk_id_imovel: int

class ContratoAluguelCreate(ContratoAluguelBase):
    pass

class ContratoAluguel(ContratoAluguelBase):
    id_contrato_alug: int
    class Config:
        orm_mode = True

class ContratoVendaBase(BaseModel):
    tipo_venda: str
    data_inicio: date
    data_fim: date
    valor_negociado: Decimal
    fk_id_usuario: int
    fk_id_imovel: int

class ContratoVendaCreate(ContratoVendaBase):
    pass

class ContratoVenda(ContratoVendaBase):
    id_contrato_venda: int
    class Config:
        orm_mode = True
