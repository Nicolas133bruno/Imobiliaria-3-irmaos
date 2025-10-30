import sys
import traceback
from fastapi.testclient import TestClient

# Add the current directory to Python path
sys.path.insert(0, '.')

try:
    from main import app
    
    client = TestClient(app)
    
    print("Testing /usuarios/ endpoint:")
    try:
        response = client.get("/usuarios/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
    
    print("\nTesting /visitas/ endpoint:")
    try:
        response = client.get("/visitas/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        
except ImportError as e:
    print(f"Import error: {e}")
    traceback.print_exc()
except Exception as e:
    print(f"Unexpected error: {e}")
    traceback.print_exc()