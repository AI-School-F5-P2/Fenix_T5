import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Pruebas para la ruta de lectura de profesores
def test_read_profesores():
    response = client.get("/profesores/read")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Pruebas para la ruta de inserción de profesores
def test_insert_profesor():
    data = {"nombre_profesor": "Nuevo Profesor"}
    response = client.post("/profesores/insert", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Registro añadido exitosamente"}

# Pruebas para la ruta de actualización de profesores
def test_update_profesor():
    data = {"nombre_profesor": "Profesor Actualizado"}
    response = client.put("/profesores/update/1", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Registro con profesor_id 1 modificado exitosamente"}

# Pruebas para la ruta de eliminación de profesores
def test_delete_profesor():
    response = client.delete("/profesores/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Registro con profesor_id 1 borrado exitosamente"}
