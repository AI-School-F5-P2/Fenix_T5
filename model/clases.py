import psycopg
from db_connection import DataBaseConnection

class Clases():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()  # Obtiene la conexión de la clase DataBaseConnection

    def read_all_clases(self):
        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Clases" """)
            data = cur.fetchall()
            return data

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "Clases"(nombre_clase, nivel_clase, precio_clase) 
                VALUES (%(nombre_clase)s, %(nivel_clase)s, %(precio_clase)s)
            """, data)
            self.conn.commit()

    def __del__(self):
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
