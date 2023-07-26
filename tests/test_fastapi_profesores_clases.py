# test_fastapi.py

import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_read_profesores_clases(client):
    # Simulamos la respuesta de la base de datos
    data = [{"profesor_id": 1, "clase_id": 1}, {"profesor_id": 2, "clase_id": 2}]
    response = client.get("/profesores_clases/read")
    assert response.status_code == 200
    assert response.json() == data

def test_insert_profesor_clase(client):
    # Simulamos el insert en la base de datos
    data = {"profesor_id": 1, "clase_id": 1}
    response = client.post("/profesores_clases/insert", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Registro añadido exitosamente"}

def test_delete_profesor_clase(client):
    # Simulamos el delete en la base de datos
    response = client.delete("/profesores_clases/delete/1/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Registro con profesor_id 1 y clase_id 1 borrado exitosamente"}
