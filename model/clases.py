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

    def insert(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "Clases"(nombre_clase, nivel_clase, precio_clase) 
                VALUES (%(nombre_clase)s, %(nivel_clase)s, %(precio_clase)s)
            """, data)
            self.conn.commit()

    def delete(self, clase_id: int):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "Clases" WHERE clase_id = %(clase_id)s
            """, {"clase_id": clase_id})
            self.conn.commit()


    def update(self, clase_id: int, updated_data):
        update_data = updated_data.dict()
        update_data["clase_id"] = clase_id  # Agregar clase_id al diccionario de datos a actualizar
        with self.conn.cursor() as cur:     # Actualización de los valores en la base de datos
            cur.execute("""                 
                UPDATE "Clases" SET
                nombre_clase = %(nombre_clase)s,
                nivel_clase = %(nivel_clase)s,
                precio_clase = %(precio_clase)s
                WHERE clase_id = %(clase_id)s
            """, {"nombre_clase": update_data["nombre_clase"], "nivel_clase": update_data["nivel_clase"], "precio_clase": update_data["precio_clase"], "clase_id": clase_id})
            self.conn.commit()


    def __del__(self):
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
