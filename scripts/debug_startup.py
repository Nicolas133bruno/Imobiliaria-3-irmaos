import subprocess
import sys
import time

def debug_api_startup():
    """Inicia a API e captura todos os logs de inicialização"""
    
    print("🔧 Iniciando API em modo debug...")
    
    # Comando para iniciar a API
    cmd = [
        sys.executable, "-m", "uvicorn", 
        "main:app", 
        "--reload", 
        "--host", "0.0.0.0", 
        "--port", "8000", 
        "--log-level", "debug"
    ]
    
    try:
        # Executar o comando e capturar stdout e stderr
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        print("✅ API iniciada. Capturando logs...")
        print("📋 Logs de inicialização:")
        print("-" * 50)
        
        # Ler e exibir logs em tempo real
        for line in process.stdout:
            print(f"[STDOUT] {line.strip()}")
            
        for line in process.stderr:
            print(f"[STDERR] {line.strip()}")
            
        # Aguardar um pouco para capturar logs
        time.sleep(5)
        
        # Verificar se o processo ainda está rodando
        if process.poll() is not None:
            print(f"❌ API parou com código de saída: {process.returncode}")
            
            # Capturar stderr completo
            _, stderr_output = process.communicate()
            if stderr_output:
                print(f"\n🔍 Erros capturados:")
                print(stderr_output)
        else:
            print("✅ API está rodando normalmente")
            
    except Exception as e:
        print(f"❌ Erro ao iniciar API: {e}")
        
    print("\n🔍 Testando endpoint /usuarios/...")
    
    # Testar o endpoint após inicialização
    try:
        import requests
        response = requests.get("http://localhost:8000/usuarios/", timeout=10)
        print(f"📊 Status Code: {response.status_code}")
        print(f"📄 Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar à API")
    except Exception as e:
        print(f"❌ Erro ao testar endpoint: {e}")

if __name__ == "__main__":
    debug_api_startup()