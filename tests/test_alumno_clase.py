# tests/test_alumno_clase.py

from model.alumnos_clases import AlumnosClases

def test_insert_alumno_clase():
    # Arrange
    alumnos_clases_instance = AlumnosClases()
    data = {"alumno_id": 1, "clase_id": 2}

    # Act
    alumnos_clases_instance.insert_alumno_clase(data)

    # Assert
    all_alumnos_clases = alumnos_clases_instance.read_all_alumnos_clases()
    assert len(all_alumnos_clases) > 0
    assert (data["alumno_id"], data["clase_id"]) in all_alumnos_clases

def test_delete():
    # Arrange
    alumnos_clases_instance = AlumnosClases()
    alumno_id = 1
    clase_id = 2

    # Act
    alumnos_clases_instance.delete(alumno_id, clase_id)

    # Assert
    all_alumnos_clases = alumnos_clases_instance.read_all_alumnos_clases()
    assert (alumno_id, clase_id) not in all_alumnos_clases

def test_read_all_alumnos_clases_no_records():
    # Arrange
    alumnos_clases_instance = AlumnosClases()

    # Act
    all_alumnos_clases = alumnos_clases_instance.read_all_alumnos_clases()

    # Assert
    assert len(all_alumnos_clases) == 0

def test_read_all_alumnos_clases_with_records():
    # Arrange
    alumnos_clases_instance = AlumnosClases()
    data1 = {"alumno_id": 1, "clase_id": 2}
    data2 = {"alumno_id": 3, "clase_id": 4}
    alumnos_clases_instance.insert_alumno_clase(data1)
    alumnos_clases_instance.insert_alumno_clase(data2)

    # Act
    all_alumnos_clases = alumnos_clases_instance.read_all_alumnos_clases()

    # Assert
    assert len(all_alumnos_clases) == 2
    assert (data1["alumno_id"], data1["clase_id"]) in all_alumnos_clases
    assert (data2["alumno_id"], data2["clase_id"]) in all_alumnos_clases

def test_delete_non_existent_record():
    # Arrange
    alumnos_clases_instance = AlumnosClases()
    alumno_id = 10
    clase_id = 20

    # Act
    alumnos_clases_instance.delete(alumno_id, clase_id)

    # Assert
    # Ensure that no exceptions are raised when trying to delete a non-existent record

def test_insert_invalid_data():
    # Arrange
    alumnos_clases_instance = AlumnosClases()
    invalid_data = {"invalid_key": "invalid_value"}  # Data with incorrect keys

    # Act and Assert
    try:
        alumnos_clases_instance.insert_alumno_clase(invalid_data)
        assert False, "Should raise an exception for invalid data"
    except KeyError:
        assert True

def test_delete_invalid_record():
    # Arrange
    alumnos_clases_instance = AlumnosClases()
    invalid_alumno_id = 100
    invalid_clase_id = 200

    # Act
    alumnos_clases_instance.delete(invalid_alumno_id, invalid_clase_id)

    # Assert
    # Ensure that no exceptions are raised when trying to delete a non-existent record

def test_insert_duplicate_record():
    # Arrange
    alumnos_clases_instance = AlumnosClases()
    data = {"alumno_id": 1, "clase_id": 2}

    # Act
    alumnos_clases_instance.insert_alumno_clase(data)

    # Assert
    try:
        alumnos_clases_instance.insert_alumno_clase(data)
        assert False, "Should raise an exception for duplicate record"
    except Exception:
        assert True

# Additional tests for other methods can also be added here, such as testing the behavior
# when inserting records with invalid data, handling duplicate records, and more.
