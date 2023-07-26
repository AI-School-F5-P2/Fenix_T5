# tests/test_fastapi_alumno_clase.py

from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_read_all_alumnos_clases():
    # Arrange
    # Assuming some records are already inserted in the database for testing
    # You can use a fixture or insert data directly using the model and DB connection

    # Act
    response = client.get("/alumnos_clases/read")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_insert_alumno_clase():
    # Arrange
    data = {"alumno_id": 1, "clase_id": 2}

    # Act
    response = client.post("/alumnos_clases/insert", json=data)

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Registro añadido exitosamente"}

def test_delete_alumno_clase():
    # Arrange
    alumno_id = 1
    clase_id = 2

    # Act
    response = client.delete(f"/alumnos_clases/delete/{alumno_id}/{clase_id}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Registro con alumno_id borrado exitosamente"}

def test_delete_non_existent_alumno_clase():
    # Arrange
    alumno_id = 100
    clase_id = 200

    # Act
    response = client.delete(f"/alumnos_clases/delete/{alumno_id}/{clase_id}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Registro con alumno_id y clase_id no encontrado"}

def test_insert_invalid_data_alumno_clase():
    # Arrange
    invalid_data = {"invalid_key": "invalid_value"}

    # Act
    response = client.post("/alumnos_clases/insert", json=invalid_data)

    # Assert
    assert response.status_code == 422

# Additional tests for other FastAPI endpoints can also be added here
# - Test error cases where the endpoints return status codes other than 200
# - Test edge cases with specific input data to cover different scenarios
# - Test authentication and authorization for protected endpoints
