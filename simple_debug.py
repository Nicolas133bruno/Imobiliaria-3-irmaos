import sys
sys.path.insert(0, '.')

try:
    from main import app
    from fastapi.testclient import TestClient
    
    client = TestClient(app)
    
    # Test usuarios endpoint
    print("Testing /usuarios/...")
    response = client.get("/usuarios/")
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: {response.text}")
    
    # Test visitas endpoint  
    print("\nTesting /visitas/...")
    response = client.get("/visitas/")
    print(f"Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: {response.text}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()