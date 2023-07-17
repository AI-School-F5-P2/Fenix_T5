import psycopg
from db_connection import DataBaseConnection

class Profesores():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()  # Obtiene la conexión de la clase DataBaseConnection

    def read_all_profesores(self):
        """
        CRUD READ. Lee todos los registros de la tabla Profesores
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Profesores" """)
            data = cur.fetchall()
            return data

    def insert_profesor(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Profesores
        :param data:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "Profesores"(nombre_profesor) 
                VALUES (%(nombre_profesor)s)
            """, data)
            self.conn.commit()

    def delete(self, profesor_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Profesores
        :param profesor_id:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "Profesores" WHERE profesor_id = %(profesor_id)s
            """, {"profesor_id": profesor_id})
            self.conn.commit()


    def update(self, profesor_id: int, updated_data):
        """
        CRUD UPDATE. Actualiza un registro específico en la tabla Profesores
        :param profesor_id:
        :param updated_data:
        :return:
        """
        update_data = updated_data.dict()
        update_data["profesor_id"] = profesor_id  # Agregar profesor_id al diccionario de datos a actualizar
        with self.conn.cursor() as cur:     # Actualización de los valores en la base de datos
            cur.execute("""                 
                UPDATE "Profesores" SET
                nombre_profesor = %(nombre_profesor)s
                WHERE profesor_id = %(profesor_id)s
            """, {"nombre_profesor": update_data["nombre_profesor"], "profesor_id": profesor_id})
            self.conn.commit()


    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
