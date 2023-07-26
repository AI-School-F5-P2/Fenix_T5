import pytest
from model.profesores import Profesores
from db_connection import DataBaseConnection

# Fixture para obtener una instancia de la clase Profesores
@pytest.fixture
def profesores_instance():
    return Profesores()

# Fixture para obtener una instancia de la clase DataBaseConnection
@pytest.fixture
def db_connection():
    return DataBaseConnection()

# Prueba de inserción de profesor en la base de datos
def test_insert_profesor_integration(profesores_instance, db_connection):
    data = {"nombre_profesor": "Nuevo Profesor"}
    profesores_instance.insert_profesor(data)

    # Verificar que el profesor fue insertado correctamente en la base de datos
    with db_connection.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Profesores" WHERE nombre_profesor = %(nombre)s""", {"nombre": data["nombre_profesor"]})
            result = cur.fetchone()
            assert result is not None
            assert result[1] == data["nombre_profesor"]

# Prueba de actualización de profesor en la base de datos
def test_update_profesor_integration(profesores_instance, db_connection):
    profesor_id = 1
    updated_data = {"nombre_profesor": "Profesor Actualizado"}
    profesores_instance.update(profesor_id, updated_data)

    # Verificar que el profesor fue actualizado correctamente en la base de datos
    with db_connection.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Profesores" WHERE profesor_id = %(id)s""", {"id": profesor_id})
            result = cur.fetchone()
            assert result is not None
            assert result[1] == updated_data["nombre_profesor"]

# Prueba de eliminación de profesor en la base de datos
def test_delete_profesor_integration(profesores_instance, db_connection):
    profesor_id = 1
    profesores_instance.delete(profesor_id)

    # Verificar que el profesor fue eliminado correctamente de la base de datos
    with db_connection.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Profesores" WHERE profesor_id = %(id)s""", {"id": profesor_id})
            result = cur.fetchone()
            assert result is None

# Prueba de lectura de todos los profesores en la base de datos
def test_read_all_profesores_integration(profesores_instance, db_connection):
    # Insertar algunos datos para probar la lectura
    data1 = {"nombre_profesor": "Profesor 1"}
    data2 = {"nombre_profesor": "Profesor 2"}
    profesores_instance.insert_profesor(data1)
    profesores_instance.insert_profesor(data2)

    # Realizar la lectura de todos los profesores en la base de datos
    profesores = profesores_instance.read_all_profesores()
    assert isinstance(profesores, list)

    # Verificar que los profesores insertados están presentes en el resultado
    nombres_profesores = [profesor["nombre_profesor"] for profesor in profesores]
    assert data1["nombre_profesor"] in nombres_profesores
    assert data2["nombre_profesor"] in nombres_profesores
