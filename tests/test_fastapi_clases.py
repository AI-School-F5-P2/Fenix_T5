from fastapi.testclient import TestClient
import unittest
from main import app
from model.clases import Clases

client = TestClient(app)

class TestFastAPIClases(unittest.TestCase):

    def setUp(self):
        # Creamos una instancia de la clase Clases para usar en las pruebas
        self.clases_instance = Clases()

    def tearDown(self):
        # Limpiamos la base de datos después de cada prueba
        self.clases_instance.conn.rollback()

    def test_read_all_clases_integration(self):
        # Insertamos datos de prueba en la tabla "Clases" para las pruebas
        data = [
            {"nombre_clase": "Clase 1", "nivel_clase": "Nivel 1", "precio_clase": 50.0, "pack": 5},
            {"nombre_clase": "Clase 2", "nivel_clase": "Nivel 2", "precio_clase": 60.0, "pack": 10}
        ]
        for clase_data in data:
            self.clases_instance.insert(clase_data)

        # Prueba el endpoint GET /clases/read para obtener todos los registros
        response = client.get("/clases/read")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), len(data))

    def test_insert_clase_integration(self):
        # Datos de prueba para el registro a insertar
        clase_data = {"nombre_clase": "Test Clase", "nivel_clase": "Intermedio", "precio_clase": 50.0, "pack": 10}

        # Prueba el endpoint POST /clases/insert para insertar el registro
        response = client.post("/clases/insert", json=clase_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Registro añadido exitosamente"})

        # Verifica que el registro haya sido insertado correctamente en la base de datos
        inserted_clase = self.clases_instance.read_all_clases()
        self.assertEqual(len(inserted_clase), 1)
        self.assertEqual(inserted_clase[0]["nombre_clase"], clase_data["nombre_clase"])

    # Agregar más pruebas de integración para otros endpoints en main.py relacionados con Clases

if __name__ == '__main__':
    unittest.main()
