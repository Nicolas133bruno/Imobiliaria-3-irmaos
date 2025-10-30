import sys
sys.path.insert(0, '.')

try:
    from main import app
    from fastapi.testclient import TestClient
    
    client = TestClient(app)
    
    # Test only usuarios endpoint
    print("Testing /usuarios/ endpoint only...")
    response = client.get("/usuarios/")
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        print("Success! Usuarios endpoint is working.")
        data = response.json()
        print(f"Number of usuarios: {len(data)}")
        if data:
            print(f"First usuario: {data[0]}")
    else:
        print(f"Error: {response.text}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()