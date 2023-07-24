import psycopg
from db_connection import DataBaseConnection

class Clases():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()

    def read_all_clases(self):
        """
        CRUD READ. Lee todos los registros de la tabla Clases
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "Clases" """)
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores de lectura en la base de datos
            print("Error al leer los registros de la tabla Clases:", e)
            return None

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
            # Manejo de la excepción específica para errores al insertar registros en la base de datos
            print("Error al insertar el registro en la tabla Clases:", e)

    def delete(self, clase_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Clases
        :param clase_id:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM "Clases" WHERE clase_id = %(clase_id)s
                """, {"clase_id": clase_id})
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al eliminar registros en la base de datos
            print("Error al eliminar el registro de la tabla Clases:", e)

    def update(self, clase_id: int, updated_data):
        """
        CRUD UPDATE. Actualiza un registro específico en la tabla Clases
        :param clase_id:
        :param updated_data:
        :return:
        """
        update_data = updated_data.dict()
        update_data["clase_id"] = clase_id
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE "Clases" SET
                    nombre_clase = %(nombre_clase)s,
                    nivel_clase = %(nivel_clase)s,
                    precio_clase = %(precio_clase)s,
                    pack = %(pack)s
                    WHERE clase_id = %(clase_id)s
                """, {
                    "nombre_clase": update_data["nombre_clase"],
                    "nivel_clase": update_data["nivel_clase"],
                    "precio_clase": update_data["precio_clase"],
                    "pack": update_data["pack"],
                    "clase_id": clase_id
                })
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al actualizar registros en la base de datos
            print("Error al actualizar el registro de la tabla Clases:", e)

    def clases_por_profesor(self, profesor_id: int):
        """
        Busca todas las clases que tiene un profesor dado
        :param profesor_id:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT nombre_clase, nivel_clase, pack  FROM "Clases"
                    INNER JOIN "Profesores_clases" ON "Clases".clase_id = "Profesores_clases".clase_id
                    WHERE "Profesores_clases".profesor_id = %(profesor_id)s
                """, {"profesor_id": profesor_id})
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores de consulta en la base de datos
            print("Error al buscar las clases del profesor en la tabla Clases:", e)
            return None

    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
