import pytest
from model.profesores import Profesores

@pytest.fixture
def profesores_instance():
    return Profesores()

# Prueba de inserción de profesor en la base de datos
def test_insert_profesor(profesores_instance):
    data = {"nombre_profesor": "Nuevo Profesor"}
    profesores_instance.insert_profesor(data)
    profesores = profesores_instance.read_all_profesores()
    assert any(p["nombre_profesor"] == data["nombre_profesor"] for p in profesores)

# Prueba de actualización de profesor en la base de datos
def test_update_profesor(profesores_instance):
    profesor_id = 1
    updated_data = {"nombre_profesor": "Profesor Actualizado"}
    profesores_instance.update(profesor_id, updated_data)
    profesor = profesores_instance.read_all_profesores()
    assert any(p["nombre_profesor"] == updated_data["nombre_profesor"] for p in profesor)

# Prueba de eliminación de profesor en la base de datos
def test_delete_profesor(profesores_instance):
    profesor_id = 1
    profesores_instance.delete(profesor_id)
    profesor = profesores_instance.read_all_profesores()
    assert not any(p["profesor_id"] == profesor_id for p in profesor)

# Prueba de lectura de todos los profesores en la base de datos
def test_read_all_profesores(profesores_instance):
    profesores = profesores_instance.read_all_profesores()
    assert isinstance(profesores, list)
    assert all(isinstance(profesor["profesor_id"], int) and isinstance(profesor["nombre_profesor"], str) for profesor in profesores)
