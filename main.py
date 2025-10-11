from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importa os routers dos seus arquivos
from routers.Contrato_Venda import router as contrato_router
from routers.Corretor import router as corretor_router
from routers.Imovel import router as imovel_router
from routers.Perfil import router as perfil_router
from routers.Usuario import router as usuario_router
from routers.Visita import router as visita_router

app = FastAPI(
    title="API Imobiliária 3 Irmãos",
    description="API para gerenciar corretores, imóveis, perfis, usuários, visitas e contratos de venda",
    version="1.0.0"
)

# Configurar CORS (se precisar, pode ajustar as origens permitidas)
origins = [
    "http://localhost",
    "http://localhost:8000",
    # outras origens, se tiver front-end separado
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui os routers
app.include_router(contrato_router)
app.include_router(corretor_router)
app.include_router(imovel_router)
app.include_router(perfil_router)
app.include_router(usuario_router)
app.include_router(visita_router)

# Rota raiz só para teste simples
@app.get("/")
def root():
    return {"message": "API Imobiliária 3 Irmãos está no ar!"}
