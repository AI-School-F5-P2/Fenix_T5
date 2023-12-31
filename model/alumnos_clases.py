import psycopg
from db_connection import DataBaseConnection

class AlumnosClases():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()  # Obtiene la conexión de la clase DataBaseConnection

    def read_all_alumnos_clases(self):
        """
        CRUD READ. Lee todos los registros de la tabla Alumnos_clases
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "Alumnos_clases" """)
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores de lectura en la base de datos
            print("Error al leer los registros de la tabla Alumnos_clases:", e)
            return None

    def insert_alumno_clase(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Alumnos_clases
        :param data:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO "Alumnos_clases"(alumno_id, clase_id) 
                    VALUES (%(alumno_id)s, %(clase_id)s)
                """, data)
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al insertar registros en la base de datos
            print("Error al insertar el registro en la tabla Alumnos_clases:", e)

    def delete(self, alumno_id: int, clase_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Alumnos_Clases
        :param alumno_id: int
        :param clase_id: int
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM "Alumnos_clases" WHERE alumno_id = %(alumno_id)s AND clase_id = %(clase_id)s
                """, {"alumno_id": alumno_id, "clase_id": clase_id})
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al eliminar registros en la base de datos
            print("Error al eliminar el registro de la tabla Alumnos_clases:", e)



    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
