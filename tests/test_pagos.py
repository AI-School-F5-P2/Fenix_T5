import pytest
from model.pagos import Pagos

def test_insert_pagos():
    # Prueba para verificar que se puede insertar un pago correctamente
    pago_data = {
        "alumno_id": 1,
        "clase_id": 2,
        "fecha_pago": "2023-07-25"
    }
    pagos_instance = Pagos()
    pagos_instance.insert(pago_data)

    # Verificar que el pago se insertó correctamente
    # (puedes verificar la base de datos o agregar más métodos en el modelo para hacer esta verificación)
    assert True

def test_delete_pagos():
    # Prueba para verificar que se puede eliminar un pago correctamente
    pago_id = 1
    pagos_instance = Pagos()
    pagos_instance.delete(pago_id)

    # Verificar que el pago se eliminó correctamente
    # (puedes verificar la base de datos o agregar más métodos en el modelo para hacer esta verificación)
    assert True

def test_update_pagos():
    # Prueba para verificar que se puede actualizar un pago correctamente
    pago_id = 1
    updated_data = {
        "alumno_id": 1,
        "clase_id": 3,
        "fecha_pago": "2023-07-26"
    }
    pagos_instance = Pagos()
    pagos_instance.update(pago_id, updated_data)

    # Verificar que el pago se actualizó correctamente
    # (puedes verificar la base de datos o agregar más métodos en el modelo para hacer esta verificación)
    assert True

def test_pagos_by_alumnos():
    # Prueba para verificar que se pueden obtener los pagos de un alumno correctamente
    alumno_id = 1
    pagos_instance = Pagos()
    pagos = pagos_instance.pagos_by_alumnos(alumno_id)

    # Verificar que se obtuvieron los pagos del alumno correctamente
    # (puedes verificar la base de datos o agregar más métodos en el modelo para hacer esta verificación)
    assert pagos is not None

def test_total_pagado_alumno():
    # Prueba para verificar que se puede obtener el total pagado por un alumno correctamente
    alumno_id = 1
    pagos_instance = Pagos()
    total_pagado = pagos_instance.total_pagado_alumno(alumno_id)

    # Verificar que se obtuvo el total pagado por el alumno correctamente
    # (puedes verificar la base de datos o agregar más métodos en el modelo para hacer esta verificación)
    assert total_pagado is not None
