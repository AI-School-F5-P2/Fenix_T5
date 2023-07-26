# tests/test_db_integration_alumno_clase.py

import pytest
import psycopg
from db_connection import DataBaseConnection
from model.alumnos_clases import AlumnosClases

def test_db_connection():
    # Arrange
    db_conn = DataBaseConnection()

    # Act
    conn = db_conn.get_connection()

    # Assert
    assert conn is not None
    assert not conn.closed

def test_alumnos_clases_integration():
    # Arrange
    db_conn = DataBaseConnection()
    alumnos_clases_instance = AlumnosClases()
    data1 = {"alumno_id": 1, "clase_id": 2}
    data2 = {"alumno_id": 3, "clase_id": 4}

    # Act
    # Test insert
    alumnos_clases_instance.insert_alumno_clase(data1)
    alumnos_clases_instance.insert_alumno_clase(data2)

    # Test read_all_alumnos_clases
    all_alumnos_clases = alumnos_clases_instance.read_all_alumnos_clases()

    # Assert
    assert len(all_alumnos_clases) == 2
    assert (data1["alumno_id"], data1["clase_id"]) in all_alumnos_clases
    assert (data2["alumno_id"], data2["clase_id"]) in all_alumnos_clases

    # Act
    # Test delete
    alumnos_clases_instance.delete(data1["alumno_id"], data1["clase_id"])
    all_alumnos_clases_after_delete = alumnos_clases_instance.read_all_alumnos_clases()

    # Assert
    assert (data1["alumno_id"], data1["clase_id"]) not in all_alumnos_clases_after_delete
    assert (data2["alumno_id"], data2["clase_id"]) in all_alumnos_clases_after_delete

def test_delete_non_existent_record_integration():
    # Arrange
    db_conn = DataBaseConnection()
    alumnos_clases_instance = AlumnosClases()
    data = {"alumno_id": 5, "clase_id": 6}

    # Act
    # Test delete non-existent record
    alumnos_clases_instance.delete(data["alumno_id"], data["clase_id"])
    all_alumnos_clases_after_delete = alumnos_clases_instance.read_all_alumnos_clases()

    # Assert
    # Ensure that no exceptions are raised and the database remains unchanged
    assert (data["alumno_id"], data["clase_id"]) not in all_alumnos_clases_after_delete

def test_insert_invalid_data_integration():
    # Arrange
    db_conn = DataBaseConnection()
    alumnos_clases_instance = AlumnosClases()
    invalid_data = {"invalid_key": "invalid_value"}  # Data with incorrect keys

    # Act and Assert
    # Test insert with invalid data
    try:
        alumnos_clases_instance.insert_alumno_clase(invalid_data)
        assert False, "Should raise an exception for invalid data"
    except KeyError:
        assert True

    # Ensure that the database remains unchanged
    all_alumnos_clases_after_insert = alumnos_clases_instance.read_all_alumnos_clases()
    assert len(all_alumnos_clases_after_insert) == 0

def test_database_connection_failure():
    # Arrange
    db_conn = DataBaseConnection()
    conn = db_conn.get_connection()
    conn.close()

    # Act and Assert
    # Ensure that the connection raises an exception when trying to execute a query after being closed
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM some_table")
        assert False, "Should raise an exception for a closed connection"
    except Exception as e:
        assert isinstance(e, psycopg.OperationalError)

def test_insert_when_database_unavailable():
    # Arrange
    # Start a test fixture using pytest's built-in fixture mechanism
    with pytest.raises(psycopg.OperationalError):
        db_conn = DataBaseConnection()
        conn = db_conn.get_connection()
        conn.close()

        # Act
        # Attempt to insert data when the database connection is not available
        data = {"alumno_id": 1, "clase_id": 2}
        alumnos_clases_instance = AlumnosClases()
        alumnos_clases_instance.insert_alumno_clase(data)

    # Assert
    # Ensure that an exception is raised when attempting to insert data with a closed connection

