import pytest
from model.pagos import Pagos
from db_connection import DataBaseConnection

# Fixture para establecer la conexión a la base de datos
@pytest.fixture(scope="module")
def db_connection():
    connection = DataBaseConnection()
    yield connection
    connection.conn.close()

# Pruebas de integración que involucran la base de datos y el componente Pagos
def test_db_integration_insert_pagos(db_connection):
    # Prueba de inserción de pago en la base de datos
    pagos_instance = Pagos()
    pago_data = {
        "alumno_id": 1,
        "clase_id": 2,
        "fecha_pago": "2023-07-25"
    }
    pagos_instance.insert(pago_data)

    # Verificar que el pago se insertó correctamente en la base de datos
    with db_connection.conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM Pagos WHERE alumno_id = 1 AND clase_id = 2 AND fecha_pago = '2023-07-25'")
        count = cur.fetchone()[0]
    assert count == 1

def test_db_integration_delete_pagos(db_connection):
    # Prueba de eliminación de pago en la base de datos
    pagos_instance = Pagos()
    pago_id = 1
    pagos_instance.delete(pago_id)

    # Verificar que el pago se eliminó correctamente de la base de datos
    with db_connection.conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM Pagos WHERE pago_id = 1")
        count = cur.fetchone()[0]
    assert count == 0

def test_db_integration_update_pagos(db_connection):
    # Prueba de actualización de pago en la base de datos
    pagos_instance = Pagos()
    pago_id = 1
    updated_data = {
        "alumno_id": 1,
        "clase_id": 3,
        "fecha_pago": "2023-07-26"
    }
    pagos_instance.update(pago_id, updated_data)

    # Verificar que el pago se actualizó correctamente en la base de datos
    with db_connection.conn.cursor() as cur:
        cur.execute("SELECT clase_id, fecha_pago FROM Pagos WHERE pago_id = 1")
        result = cur.fetchone()
    assert result[0] == 3
    assert str(result[1]) == "2023-07-26"

def test_db_integration_pagos_by_alumnos(db_connection):
    # Prueba de obtención de pagos por alumno desde la base de datos
    pagos_instance = Pagos()
    alumno_id = 1
    pagos = pagos_instance.pagos_by_alumnos(alumno_id)

    # Verificar que se obtuvieron los pagos del alumno correctamente desde la base de datos
    with db_connection.conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM Pagos WHERE alumno_id = 1")
        count = cur.fetchone()[0]
    assert len(pagos) == count

def test_db_integration_total_pagado_alumno(db_connection):
    # Prueba de obtención del total pagado por un alumno desde la base de datos
    pagos_instance = Pagos()
    alumno_id = 1
    total_pagado = pagos_instance.total_pagado_alumno(alumno_id)

    # Verificar que se obtuvo el total pagado por el alumno correctamente desde la base de datos
    with db_connection.conn.cursor() as cur:
        cur.execute("SELECT SUM(importe_pagado) FROM Pagos WHERE alumno_id = 1")
        total_pagado_db = cur.fetchone()[0]
    assert total_pagado == total_pagado_db
