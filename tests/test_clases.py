import unittest
from model.clases import Clases

class TestClasesModel(unittest.TestCase):

    def setUp(self):
        # Creamos una instancia de la clase Clases para usar en las pruebas
        self.clases_instance = Clases()

    def test_read_all_clases(self):
        # Prueba que se puedan leer todos los registros de la tabla "Clases"
        data = [
            (1, "Clase 1", "Nivel 1", 50.0, 5),
            (2, "Clase 2", "Nivel 2", 60.0, 10),
            # Agregar más datos de prueba según sea necesario
        ]

        # Mock de la función de lectura de la base de datos
        self.clases_instance.conn.cursor().fetchall.return_value = data

        result = self.clases_instance.read_all_clases()

        self.assertEqual(len(result), len(data))
        self.assertEqual(result[0]["nombre_clase"], "Clase 1")
        self.assertEqual(result[1]["precio_clase"], 60.0)

    def test_insert_clase(self):
        # Prueba que se pueda insertar un nuevo registro en la tabla "Clases"
        data = {
            "nombre_clase": "Test Clase",
            "nivel_clase": "Intermedio",
            "precio_clase": 50.0,
            "pack": 10
        }

        # Mock de la función de inserción en la base de datos
        self.clases_instance.conn.cursor().execute.return_value = None

        result = self.clases_instance.insert(data)

        # Verificar que no se devuelve ningún resultado
        self.assertIsNone(result)

    def test_delete_clase(self):
        # Prueba que se pueda borrar un registro específico de la tabla "Clases"
        clase_id = 1

        # Mock de la función de borrado en la base de datos
        self.clases_instance.conn.cursor().execute.return_value = None

        self.clases_instance.delete(clase_id)

        # Verificar que la función de borrado fue llamada con el parámetro correcto
        self.clases_instance.conn.cursor().execute.assert_called_once_with(
            "DELETE FROM \"Clases\" WHERE clase_id = %(clase_id)s",
            {"clase_id": clase_id}
        )

    # Agregar más pruebas unitarias para otros métodos en Clases si es necesario

if __name__ == '__main__':
    unittest.main()
