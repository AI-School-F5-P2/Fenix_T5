# test_fastapi.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_alumnos():
    # Prueba la ruta /alumnos para obtener todos los alumnos
    response = client.get("/alumnos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_alumno():
    # Prueba la ruta /alumnos/insert para crear un nuevo alumno
    data = {
        "nombre_alumno": "Juan",
        "apellidos_alumno": "Perez",
        "edad_alumno": 25,
        "telefono_alumno": "123456789",
        "email_alumno": "juan@example.com",
        "familiar": True,
    }
    response = client.post("/alumnos/insert", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Registro añadido exitosamente"}

def test_update_alumno():
    # Prueba la ruta /alumnos/update/{alumno_id} para actualizar un alumno existente
    alumno_id = 1  # Asumiendo que el ID del alumno a actualizar es 1 (puede variar según la base de datos)
    updated_data = {
        "nombre_alumno": "Juan Modificado",
        "apellidos_alumno": "Perez",
        "edad_alumno": 26,
        "telefono_alumno": "987654321",
        "email_alumno": "juan_modificado@example.com",
        "familiar": False,
    }
    response = client.put(f"/alumnos/update/{alumno_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json() == {"message": f"Registro con alumno_id {alumno_id} modificado exitosamente"}

def test_delete_alumno():
    # Prueba la ruta /alumnos/delete/{alumno_id} para eliminar un alumno existente
    alumno_id = 1  # Asumiendo que el ID del alumno a eliminar es 1 (puede variar según la base de datos)
    response = client.delete(f"/alumnos/delete/{alumno_id}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Registro con alumno_id {alumno_id} borrado exitosamente"}

def test_get_alumno_by_id():
    # Prueba la ruta /alumnos/{alumno_id} para obtener un alumno específico por su ID
    alumno_id = 1  # Asumiendo que el ID del alumno a obtener es 1 (puede variar según la base de datos)
    response = client.get(f"/alumnos/{alumno_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["alumno_id"] == alumno_id

def test_get_alumnos_by_name():
    # Prueba la ruta /alumnos/search/{nombre_alumno} para buscar alumnos por su nombre
    nombre_alumno = "Juan"  # Asumiendo que hay alumnos con este nombre (puede variar según la base de datos)
    response = client.get(f"/alumnos/search/{nombre_alumno}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(alumno["nombre_alumno"] == nombre_alumno for alumno in response.json())

def test_get_alumnos_by_age_range():
    # Prueba la ruta /alumnos/search/age?min={min_age}&max={max_age} para buscar alumnos por rango de edad
    min_age = 20
    max_age = 30
    response = client.get(f"/alumnos/search/age?min={min_age}&max={max_age}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(min_age <= alumno["edad_alumno"] <= max_age for alumno in response.json())

def test_get_alumnos_by_familiar_status():
    # Prueba la ruta /alumnos/search/familiar?familiar={familiar_status} para buscar alumnos por estado de familiar
    familiar_status = True
    response = client.get(f"/alumnos/search/familiar?familiar={familiar_status}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(alumno["familiar"] == familiar_status for alumno in response.json())
