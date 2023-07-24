import psycopg
from db_connection import DataBaseConnection

class Clases():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()  # Obtiene la conexión de la clase DataBaseConnection

    # Lee todos los registros de la tabla Clases
    def read_all_clases(self):
        """
        CRUD READ. Lee todos los registros de la tabla Clases
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Clases" """)
            data = cur.fetchall()
            return data


    # Inserta un registro en la tabla Clases
    def insert(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Clases
        :param data:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                INSERT INTO "Clases"(nombre_clase, nivel_clase, precio_clase, pack) 
                VALUES (%(nombre_clase)s, %(nivel_clase)s, %(precio_clase)s, %(pack)s)
            """, data)
                self.conn.commit()
        except psycopg.Error as e:
            # En caso de error, deshacer cualquier cambio pendiente
            self.conn.rollback()
            return {"message": f"Error al crear el registro de alumno: {e}"}


    # Borra un registro específico en la tabla Clases
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


    # Actualiza un registro específico en la tabla Clases
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
                precio_clase = %(precio_clase)s,
                pack = %(pack)s
                WHERE clase_id = %(clase_id)s
            """, {"nombre_clase": update_data["nombre_clase"], "nivel_clase": update_data["nivel_clase"],
                  "precio_clase": update_data["precio_clase"], "pack": update_data["pack"], "clase_id": clase_id})
            self.conn.commit()


    # Busca todas las clases que tiene un profesor dado
    def clases_por_profesor(self, profesor_id: int):
        """
        Busca todas las clases que tiene un profesor dado
        :param profesor_id:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT nombre_clase, nivel_clase, pack  FROM "Clases"
                INNER JOIN "Profesores_clases" ON "Clases".clase_id = "Profesores_clases".clase_id
                WHERE "Profesores_clases".profesor_id = %(profesor_id)s
            """, {"profesor_id": profesor_id})
            data = cur.fetchall()
            return  data

    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
