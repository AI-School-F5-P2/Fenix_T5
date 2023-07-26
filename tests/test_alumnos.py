# test_model_alumnos.py
from model.alumnos import Alumnos

def test_read_all_alumnos():
    # Prueba la función read_all_alumnos() del modelo Alumnos para obtener todos los alumnos
    alumnos_model = Alumnos()
    result = alumnos_model.read_all_alumnos()
    assert isinstance(result, list)

def test_insert_alumno():
    # Prueba la función insert_alumno() del modelo Alumnos para insertar un nuevo alumno
    alumnos_model = Alumnos()
    data = {
        "nombre_alumno": "Juan",
        "apellidos_alumno": "Perez",
        "edad_alumno": 25,
        "telefono_alumno": "123456789",
        "email_alumno": "juan@example.com",
        "familiar": True,
    }
    alumnos_model.insert_alumno(data)

    # Verificar que el alumno se ha insertado correctamente
    all_alumnos = alumnos_model.read_all_alumnos()
    inserted_alumno = next(alumno for alumno in all_alumnos if alumno["nombre_alumno"] == "Juan")
    assert inserted_alumno["nombre_alumno"] == "Juan"
    assert inserted_alumno["apellidos_alumno"] == "Perez"
    assert inserted_alumno["edad_alumno"] == 25
    assert inserted_alumno["telefono_alumno"] == "123456789"
    assert inserted_alumno["email_alumno"] == "juan@example.com"
    assert inserted_alumno["familiar"] == True

def test_update_alumno():
    # Prueba la función update_alumno() del modelo Alumnos para actualizar un alumno existente
    alumnos_model = Alumnos()
    data = {
        "nombre_alumno": "Juan",
        "apellidos_alumno": "Perez",
        "edad_alumno": 25,
        "telefono_alumno": "123456789",
        "email_alumno": "juan@example.com",
        "familiar": True,
    }
    alumnos_model.insert_alumno(data)

    # Obtener el ID del alumno insertado
    all_alumnos = alumnos_model.read_all_alumnos()
    alumno_id = next(alumno["alumno_id"] for alumno in all_alumnos if alumno["nombre_alumno"] == "Juan")

    # Datos actualizados
    updated_data = {
        "nombre_alumno": "Juan Modificado",
        "apellidos_alumno": "Perez",
        "edad_alumno": 26,
        "telefono_alumno": "987654321",
        "email_alumno": "juan_modificado@example.com",
        "familiar": False,
    }
    alumnos_model.update(alumno_id, updated_data)

    # Verificar que el alumno se ha actualizado correctamente
    updated_alumno = next(alumno for alumno in all_alumnos if alumno["alumno_id"] == alumno_id)
    assert updated_alumno["nombre_alumno"] == "Juan Modificado"
    assert updated_alumno["edad_alumno"] == 26
    assert updated_alumno["telefono_alumno"] == "987654321"
    assert updated_alumno["email_alumno"] == "juan_modificado@example.com"
    assert updated_alumno["familiar"] == False

def test_delete_alumno():
    # Prueba la función delete() del modelo Alumnos para eliminar un alumno existente
    alumnos_model = Alumnos()
    data = {
        "nombre_alumno": "Juan",
        "apellidos_alumno": "Perez",
        "edad_alumno": 25,
        "telefono_alumno": "123456789",
        "email_alumno": "juan@example.com",
        "familiar": True,
    }
    alumnos_model.insert_alumno(data)

    # Obtener el ID del alumno insertado
    all_alumnos = alumnos_model.read_all_alumnos()
    alumno_id = next(alumno["alumno_id"] for alumno in all_alumnos if alumno["nombre_alumno"] == "Juan")

    # Eliminar el alumno
    alumnos_model.delete(alumno_id)

    # Verificar que el alumno se ha eliminado correctamente
    all_alumnos_after_delete = alumnos_model.read_all_alumnos()
    assert alumno_id not in [alumno["alumno_id"] for alumno in all_alumnos_after_delete]
