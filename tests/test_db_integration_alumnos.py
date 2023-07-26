# test_db_integration_alumnos.py
from model.alumnos import Alumnos

def test_integration_alumnos():
    # Prueba de integración para el modelo Alumnos y la base de datos

    # Creamos una instancia del modelo Alumnos
    alumnos_model = Alumnos()

    # Insertamos un nuevo alumno en la base de datos
    data = {
        "nombre_alumno": "Juan",
        "apellidos_alumno": "Perez",
        "edad_alumno": 25,
        "telefono_alumno": "123456789",
        "email_alumno": "juan@example.com",
        "familiar": True,
    }
    alumnos_model.insert_alumno(data)

    # Verificamos que el alumno se haya insertado correctamente
    all_alumnos = alumnos_model.read_all_alumnos()
    inserted_alumno = next(alumno for alumno in all_alumnos if alumno["nombre_alumno"] == "Juan")
    assert inserted_alumno["nombre_alumno"] == "Juan"
    assert inserted_alumno["apellidos_alumno"] == "Perez"
    assert inserted_alumno["edad_alumno"] == 25
    assert inserted_alumno["telefono_alumno"] == "123456789"
    assert inserted_alumno["email_alumno"] == "juan@example.com"
    assert inserted_alumno["familiar"] == True

    # Actualizamos el alumno insertado
    alumno_id = inserted_alumno["alumno_id"]
    updated_data = {
        "nombre_alumno": "Juan Modificado",
        "apellidos_alumno": "Perez",
        "edad_alumno": 26,
        "telefono_alumno": "987654321",
        "email_alumno": "juan_modificado@example.com",
        "familiar": False,
    }
    alumnos_model.update(alumno_id, updated_data)

    # Verificamos que el alumno se haya actualizado correctamente
    updated_alumno = next(alumno for alumno in all_alumnos if alumno["alumno_id"] == alumno_id)
    assert updated_alumno["nombre_alumno"] == "Juan Modificado"
    assert updated_alumno["edad_alumno"] == 26
    assert updated_alumno["telefono_alumno"] == "987654321"
    assert updated_alumno["email_alumno"] == "juan_modificado@example.com"
    assert updated_alumno["familiar"] == False

    # Eliminamos el alumno insertado
    alumnos_model.delete(alumno_id)

    # Verificamos que el alumno se haya eliminado correctamente
    all_alumnos_after_delete = alumnos_model.read_all_alumnos()
    assert alumno_id not in [alumno["alumno_id"] for alumno in all_alumnos_after_delete]

# Agrega más pruebas de integración según sea necesario para otras operaciones CRUD y modelos de la base de datos.
