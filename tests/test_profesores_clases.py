# test_profesores_clases.py

import pytest
from model.profesores_clases import ProfesoresClases
from schema.profesores_clases_schema import ProfesoresClasesSchema
from pydantic import ValidationError

# Pruebas unitarias para el modelo ProfesoresClasesSchema

def test_valid_profesores_clases_schema():
    # Datos válidos para el esquema ProfesoresClasesSchema
    data = {"profesor_id": 1, "clase_id": 1}
    profesores_clases = ProfesoresClasesSchema(**data)
    assert profesores_clases.profesor_id == 1
    assert profesores_clases.clase_id == 1

def test_invalid_profesores_clases_schema_invalid_types():
    # Datos inválidos para el esquema ProfesoresClasesSchema (profesor_id no es entero)
    data = {"profesor_id": "no_es_entero", "clase_id": 1}
    with pytest.raises(ValidationError) as excinfo:
        ProfesoresClasesSchema(**data)
    assert "'profesor_id' expected int" in str(excinfo.value)

def test_invalid_profesores_clases_schema_missing_fields():
    # Datos inválidos para el esquema ProfesoresClasesSchema (falta clase_id)
    data = {"profesor_id": 1}
    with pytest.raises(ValidationError) as excinfo:
        ProfesoresClasesSchema(**data)
    assert "'clase_id' is a required field" in str(excinfo.value)


# Pruebas unitarias para el enrutador main_profesor_clase.py

class MockProfesoresClases:
    def __init__(self):
        self.data = []

    def read_all_profesores_clases(self):
        return self.data

    def insert_profesor_clase(self, data):
        self.data.append(data)

    def delete(self, profesor_id: int, clase_id: int):
        self.data = [item for item in self.data if item["profesor_id"] != profesor_id or item["clase_id"] != clase_id]

@pytest.fixture
def mock_profesores_clases():
    return MockProfesoresClases()

def test_read_all_profesores_clases(mock_profesores_clases):
    # Datos de prueba para el MockProfesoresClases
    mock_data = [{"profesor_id": 1, "clase_id": 1}, {"profesor_id": 2, "clase_id": 2}]
    mock_profesores_clases.data = mock_data

    # Crear una instancia del enrutador con el MockProfesoresClases
    from routers.main_profesor_clase import routerprofesores_clases
    routerprofesores_clases.dependency_overrides[ProfesoresClases] = lambda: mock_profesores_clases

    # Realizar la solicitud GET a la ruta "/profesores_clases/read"
    from fastapi.testclient import TestClient
    from main import app
    client = TestClient(app)
    response = client.get("/profesores_clases/read")

    # Verificar la respuesta
    assert response.status_code == 200
    assert response.json() == mock_data

def test_insert_and_delete_profesor_clase(mock_profesores_clases):
    # Crear una instancia del enrutador con el MockProfesoresClases
    from routers.main_profesor_clase import routerprofesores_clases
    routerprofesores_clases.dependency_overrides[ProfesoresClases] = lambda: mock_profesores_clases

    # Realizar la solicitud POST para insertar un registro
    data = {"profesor_id": 1, "clase_id": 1}
    from fastapi.testclient import TestClient
    from main import app
    client = TestClient(app)
    response = client.post("/profesores_clases/insert", json=data)

    # Verificar la respuesta y que el registro se haya insertado correctamente
    assert response.status_code == 200
    assert response.json() == {"message": "Registro añadido exitosamente"}
    assert len(mock_profesores_clases.data) == 1

    # Realizar la solicitud DELETE para borrar el registro
    response = client.delete("/profesores_clases/delete/1/1")

    # Verificar la respuesta y que el registro se haya borrado correctamente
    assert response.status_code == 200
    assert response.json() == {"message": "Registro con profesor_id 1 y clase_id 1 borrado exitosamente"}
    assert len(mock_profesores_clases.data) == 0
