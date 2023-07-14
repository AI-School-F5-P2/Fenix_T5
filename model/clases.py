import psycopg
from db_connection import DataBaseConnection

class Clases():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()  # Obtiene la conexión de la clase DataBaseConnection

    def read_all_clases(self):
        """
        CRUD READ. Lee todos los registros de la tabla Clases
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Clases" """)
            data = cur.fetchall()
            return data

    def insert(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Clases
        :param data:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                INSERT INTO "Clases"(nombre_clase, nivel_clase, precio_clase) 
                VALUES (%(nombre_clase)s, %(nivel_clase)s, %(precio_clase)s)
            """, data)
                self.conn.commit()
        except psycopg.Error as e:
            # En caso de error, deshacer cualquier cambio pendiente
            connection.rollback()
            return {"message": f"Error al crear el registro de alumno: {e}"}



    def delete(self, clase_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Clases
        :param clase_id:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "Clases" WHERE clase_id = %(clase_id)s
            """, {"clase_id": clase_id})
            self.conn.commit()


    def update(self, clase_id: int, updated_data):
        """
        CRUD UPDATE. Actualiza un registro específico en la tabla Clases
        :param clase_id:
        :param updated_data:
        :return:
        """
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
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
