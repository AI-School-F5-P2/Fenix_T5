import psycopg
from db_connection import DataBaseConnection

class Alumnos():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()  # Obtiene la conexión de la clase DataBaseConnection

    def read_all_alumnos(self):
        """
        CRUD READ. Lee todos los registros de la tabla Alumnos
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "Alumnos" """)
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores de lectura en la base de datos
            print("Error al leer los registros de la tabla Alumnos:", e)
            return None

    def insert_alumno(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Alumnos
        :param data:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO "Alumnos"(nombre_alumno, apellidos_alumno, edad_alumno, telefono_alumno, email_alumno, familiar) 
                    VALUES (%(nombre_alumno)s, %(apellidos_alumno)s, %(edad_alumno)s, %(telefono_alumno)s, %(email_alumno)s, %(familiar)s )
                """, data)
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al insertar registros en la base de datos
            print("Error al insertar el registro en la tabla Alumnos:", e)


    def delete(self, alumno_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Alumnos
        :param clase_id:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM "Alumnos" WHERE alumno_id = %(alumno_id)s
                """, {"alumno_id": alumno_id})
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al eliminar registros en la base de datos
            print("Error al eliminar el registro de la tabla Alumnos:", e)


    def update(self, alumno_id: int, updated_data):
        """
        CRUD UPDATE. Actualiza un registro específico en la tabla Alumnos
        :param clase_id:
        :param updated_data:
        :return:
        """
        update_data = updated_data.dict()
        update_data["alumno_id"] = alumno_id
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE "Alumnos" SET
                    nombre_alumno = %(nombre_alumno)s,
                    apellidos_alumno = %(apellidos_alumno)s,
                    edad_alumno = %(edad_alumno)s,
                    telefono_alumno = %(telefono_alumno)s,
                    email_alumno = %(email_alumno)s,
                    familiar = %(familiar)s
                    WHERE alumno_id = %(alumno_id)s
                """, {
                    "nombre_alumno": update_data["nombre_alumno"],
                    "apellidos_alumno": update_data["apellidos_alumno"],
                    "edad_alumno": update_data["edad_alumno"],
                    "telefono_alumno": update_data["telefono_alumno"],
                    "email_alumno": update_data["email_alumno"],
                    "familiar": update_data["familiar"],
                    "alumno_id": alumno_id
                })
                self.conn.commit()
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores al actualizar registros en la base de datos
            print("Error al actualizar el registro de la tabla Alumnos:", e)


    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
