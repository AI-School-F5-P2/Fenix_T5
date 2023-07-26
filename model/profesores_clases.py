import psycopg
from db_connection import DataBaseConnection

class ProfesoresClases():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()

    def read_all_profesores_clases(self):
        """
        CRUD READ. Lee todos los registros de la tabla Profesores_clases
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "Profesores_clases" """)
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores de lectura en la base de datos
            print("Error al leer los registros de la tabla Profesores_clases:", e)
            return None

    def insert_profesor_clase(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Profesores_clases
        :param data:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO "Profesores_clases"(profesor_id, clase_id) 
                    VALUES (%(profesor_id)s, %(clase_id)s)
                """, data)
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al insertar registros en la base de datos
            print("Error al insertar el registro en la tabla Profesores_clases:", e)

    def delete(self, profesor_id: int, clase_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Profesores_clases
        :param profesor_id:
        :param clase_id:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM "Profesores_clases" WHERE profesor_id = %(profesor_id)s AND clase_id = %(clase_id)s
                """, {"profesor_id": profesor_id, "clase_id": clase_id})
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al eliminar registros en la base de datos
            print("Error al eliminar el registro de la tabla Profesores_clases:", e)

    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
