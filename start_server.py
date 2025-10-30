#!/usr/bin/env python3
"""
Script para iniciar o servidor FastAPI
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.app.main:app", host="127.0.0.1", port=3000, reload=True)