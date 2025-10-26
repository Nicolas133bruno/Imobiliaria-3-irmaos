# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from src.routers.Usuario import router as usuario_router
from src.routers.ContratoAluguel import router as contrato_aluguel_router
from src.routers.ContratoVenda import router as contrato_venda_router
from src.routers.StatusImovel import router as status_imovel_router
from src.routers.Imovel import router as imovel_router
from src.routers.Visita import router as visita_router
from src.routers.Corretor import router as corretor_router
from src.routers.Perfil import router as perfil_router
from src.routers.Endereco import router as endereco_router
from src.routers.relatorios import router as relatorios_router
from src.routers.consulta import router as consulta_router

# =========================
# Criando a aplicacao
# =========================
app = FastAPI(
    title="API Imobiliaria 3 Irmaos",
    description="API para gerenciar corretores, imoveis, perfis, usuarios, visitas e contratos",
    version="1.0.0",
)

# =========================
# CORS
# =========================
origins = ["http://localhost", "http://localhost:8080", "http://127.0.0.1:8000", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Incluindo routers
# =========================
app.include_router(usuario_router)
app.include_router(perfil_router)
app.include_router(corretor_router)
app.include_router(endereco_router)
app.include_router(imovel_router)
app.include_router(visita_router)
app.include_router(contrato_aluguel_router)
app.include_router(contrato_venda_router)
app.include_router(status_imovel_router)  # Status Imovel completo
app.include_router(relatorios_router)
app.include_router(consulta_router)  # Consultas gerais

# =========================
# Endpoint raiz
# =========================
@app.get("/")
def root():
    return {"message": "API Imobiliaria 3 Irmaos esta no ar!"}
