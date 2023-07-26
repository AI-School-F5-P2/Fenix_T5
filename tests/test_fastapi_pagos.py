import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_pagos():
    # Prueba para verificar que la ruta "/pagos/read" devuelve una respuesta exitosa
    response = client.get("/pagos/read")
    assert response.status_code == 200

def test_create_pagos():
    # Prueba para verificar que se puede crear un pago correctamente
    data = {"alumno_id": 1, "clase_id": 2, "fecha_pago": "2023-07-25"}
    response = client.post("/pagos/pagos/insert", json=data)
    assert response.status_code == 200

def test_get_pagos_by_alumno_id():
    # Prueba para verificar que se puede obtener los pagos de un alumno por su ID
    response = client.get("/pagos/alumno/1")
    assert response.status_code == 200

def test_get_total_pagado_por_alumno():
    # Prueba para verificar que se puede obtener el total pagado por un alumno
    response = client.get("/pagos/alumno/importe_total/1")
    assert response.status_code == 200

def test_update_pagos():
    # Prueba para verificar que se puede actualizar un pago correctamente
    pago_id = 1
    data = {"alumno_id": 1, "clase_id": 2, "fecha_pago": "2023-07-26"}
    response = client.put(f"/pagos/update/{pago_id}", json=data)
    assert response.status_code == 200

def test_delete_pagos():
    # Prueba para verificar que se puede eliminar un pago correctamente
    pago_id = 1
    response = client.delete(f"/pagos/delete/{pago_id}")
    assert response.status_code == 200
