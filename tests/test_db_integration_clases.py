import unittest
import psycopg
from model.clases import Clases
from db_connection import DataBaseConnection

class TestDbIntegrationClases(unittest.TestCase):

    def setUp(self):
        # Configuramos la base de datos para pruebas
        self.test_db_name = "test_db"  # Nombre de la base de datos de prueba
        self.db_conn = DataBaseConnection(
            db_name=self.test_db_name,
            db_user="test_user",
            db_password="test_password",
            db_host="localhost",
            db_port="5432"
        )
        self.conn = self.db_conn.get_connection()
        self.create_test_table()

        # Creamos una instancia de la clase Clases para usar en las pruebas
        self.clases_instance = Clases()

    def tearDown(self):
        # Cerramos la conexión de la base de datos de prueba y la eliminamos
        if self.conn is not None and not self.conn.closed:
            self.conn.close()

        self.drop_test_table()

    def create_test_table(self):
        # Creamos una tabla de prueba en la base de datos de prueba
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS "Clases" (
                    clase_id SERIAL PRIMARY KEY,
                    nombre_clase VARCHAR(100) NOT NULL,
                    nivel_clase VARCHAR(50) NOT NULL,
                    precio_clase NUMERIC(10, 2) NOT NULL,
                    pack INTEGER NOT NULL
                )
            """)
            self.conn.commit()

    def drop_test_table(self):
        # Eliminamos la tabla de prueba de la base de datos de prueba
        with self.conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS \"Clases\"")
            self.conn.commit()

    def test_insert_clase(self):
        # Prueba que se pueda insertar un nuevo registro en la tabla "Clases"
        data = {
            "nombre_clase": "Test Clase",
            "nivel_clase": "Intermedio",
            "precio_clase": 50.0,
            "pack": 10
        }
        self.clases_instance.insert(data)

        # Verificar que el registro se haya insertado correctamente
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM \"Clases\"")
            result = cur.fetchall()
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0][1], "Test Clase")
            self.assertEqual(result[0][2], "Intermedio")
            self.assertEqual(result[0][3], 50.0)
            self.assertEqual(result[0][4], 10)

    def test_delete_clase(self):
        # Prueba que se pueda borrar un registro específico de la tabla "Clases"
        data = {
            "nombre_clase": "Test Clase",
            "nivel_clase": "Intermedio",
            "precio_clase": 50.0,
            "pack": 10
        }
        self.clases_instance.insert(data)

        # Obtenemos el clase_id del registro insertado
        with self.conn.cursor() as cur:
            cur.execute("SELECT clase_id FROM \"Clases\"")
            clase_id = cur.fetchone()[0]

        self.clases_instance.delete(clase_id)

        # Verificar que el registro se haya borrado correctamente
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM \"Clases\"")
            result = cur.fetchall()
            self.assertEqual(len(result), 0)

    # Agregar más pruebas de integración para otros métodos en Clases si es necesario

if __name__ == '__main__':
    unittest.main()
