# test_db_integration.py

import pytest
from db_connection import DataBaseConnection

@pytest.fixture
def db_connection():
    # Usar una base de datos de prueba o sandbox
    db_name = "test_db"
    db_user = "test_user"
    db_password = "test_password"
    db_host = "localhost"
    db_port = "5432"
    # Realizar la conexión
    db_conn = DataBaseConnection(
        db_name=db_name,
        db_user=db_user,
        db_password=db_password,
        db_host=db_host,
        db_port=db_port
    )
    yield db_conn
    # Limpiar recursos después de las pruebas
    db_conn.conn.close()

def test_db_connection(db_connection):
    # Verificar que la conexión se haya establecido correctamente
    assert db_connection.conn is not None
    assert not db_connection.conn.closed

def test_db_read_all_profesores_clases(db_connection):
    # Insertar datos de prueba en la base de datos antes de la prueba
    with db_connection.conn.cursor() as cur:
        cur.execute("""
            INSERT INTO "Profesores_clases"(profesor_id, clase_id) 
            VALUES (1, 1), (2, 2)
        """)
        db_connection.conn.commit()

    # Realizar la operación de lectura en la base de datos
    with db_connection.conn.cursor() as cur:
        cur.execute("""SELECT * FROM "Profesores_clases" """)
        data = cur.fetchall()

    # Verificar que los datos sean correctos
    assert len(data) == 2
    assert data[0] == (1, 1)
    assert data[1] == (2, 2)
