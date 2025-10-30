# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importação dos routers
try:
    from ..routers.Usuario import router as usuario_router
    from ..routers.ContratoAluguel import router as contrato_aluguel_router
    from ..routers.ContratoVenda import router as contrato_venda_router
    from ..routers.StatusImovel import router as status_imovel_router
    from ..routers.Imovel import router as imovel_router
    from ..routers.Visita import router as visita_router
    from ..routers.Corretor import router as corretor_router
    from ..routers.Perfil import router as perfil_router
    from ..routers.Endereco import router as endereco_router
    from ..routers.relatorios import router as relatorios_router
    from ..routers.consulta import router as consulta_router
    
    ROUTERS_LOADED = True
except ImportError as e:
    print(f"Aviso: Não foi possível carregar todos os routers: {e}")
    ROUTERS_LOADED = False

app = FastAPI(
    title="API Imobiliária 3 Irmãos",
    description="API para gerenciar corretores, imóveis, perfis, usuários, visitas e contratos",
    version="1.0.0"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Imobiliária 3 Irmãos API - Funcionando!"}

@app.get("/status")
def status():
    return {
        "status": "online",
        "routers_loaded": ROUTERS_LOADED
    }

# Inclusão dos routers se carregados com sucesso
if ROUTERS_LOADED:
    try:
        app.include_router(usuario_router)
        app.include_router(contrato_aluguel_router)
        app.include_router(contrato_venda_router)
        app.include_router(status_imovel_router)
        app.include_router(imovel_router)
        app.include_router(visita_router)
        app.include_router(corretor_router)
        app.include_router(perfil_router)
        app.include_router(endereco_router)
        app.include_router(relatorios_router)
        app.include_router(consulta_router)
        print("Todos os routers foram carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao incluir routers: {e}")
