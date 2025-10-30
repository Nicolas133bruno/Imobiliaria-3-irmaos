"""
Módulo de rotas da API.

Contém todos os endpoints da aplicação FastAPI.
"""

from .ContratoAluguel import router as contrato_aluguel_router  # noqa
from .ContratoVenda import router as contrato_venda_router  # noqa
from .Corretor import router as corretor_router  # noqa
from .Endereco import router as endereco_router  # noqa
from .Imovel import router as imovel_router  # noqa
from .Perfil import router as perfil_router  # noqa
from .StatusImovel import router as status_imovel_router  # noqa
from .Usuario import router as usuario_router  # noqa
from .Visita import router as visita_router  # noqa
from .consulta import router as consulta_router  # noqa
from .relatorios import router as relatorios_router  # noqa