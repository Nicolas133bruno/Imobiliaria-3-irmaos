# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from routers.Usuario import router as usuario_router
from routers.ContratoAluguel import  router as contrato_aluguel_router
from routers.ContratoVenda import router as contrato_venda_router
from routers.StatusImovel import router as status_imovel_router
from routers.Imovel import router as imovel_router
from routers.Visita import router as visita_router
from routers.Corretor import router as corretor_router
from routers.Perfil import router as perfil_router
from routers.relatorios import router as relatorios_router

# =========================
# Criando a aplicação
# =========================
app = FastAPI(
    title="API Imobiliária 3 Irmãos",
    description="API para gerenciar corretores, imóveis, perfis, usuários, visitas e contratos",
    version="1.0.0",
)

# =========================
# CORS
# =========================
origins = ["http://localhost", "http://localhost:8080"]
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
app.include_router(imovel_router)
app.include_router(visita_router)
app.include_router(contrato_aluguel_router)
app.include_router(contrato_venda_router)
app.include_router(status_imovel_router)  # Status Imóvel completo
app.include_router(relatorios_router)

# =========================
# Endpoint raiz
# =========================
@app.get("/")
def root():
    return {"message": "API Imobiliária 3 Irmãos está no ar!"}
