import psycopg
from db_connection import DataBaseConnection

class ProfesoresClases():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()  # Obtiene la conexión de la clase DataBaseConnection

    def read_all_profesores_clases(self):
        """
        CRUD READ. Lee todos los registros de la tabla Profesores_clases
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Profesores_clases" """)
            data = cur.fetchall()
            return data

    def insert_profesor_clase(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Profesores_clases
        :param data:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "Profesores_clases"(profesor_id, clase_id) 
                VALUES (%(profesor_id)s, %(clase_id)s)
            """, data)
            self.conn.commit()

    def delete(self, profesor_id: int, clase_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Profesores_clases
        :param profesor_id:
        :param clase_id:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "Profesores_clases" WHERE profesor_id = %(profesor_id)s AND clase_id = %(clase_id)s
            """, {"profesor_id": profesor_id, "clase_id": clase_id})
            self.conn.commit()



    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()