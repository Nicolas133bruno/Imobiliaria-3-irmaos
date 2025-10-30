from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

try:
    response = client.get("/visitas/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        visitas = response.json()
        print(f"Number of visitas: {len(visitas)}")
        for visita in visitas[:3]:  # Show first 3 for brevity
            print(f"Visita: {visita}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()