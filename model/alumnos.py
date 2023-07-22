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
        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Alumnos" """)
            data = cur.fetchall()
            return data

    def insert_alumno(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Alumnos
        :param data:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "Alumnos"(nombre_alumno, apellidos_alumno, edad_alumno, telefono_alumno, email_alumno, familiar_alumno) 
                VALUES (%(nombre_alumno)s, %(apellidos_alumno)s, %(edad_alumno)s, %(telefono_alumno)s, %(email_alumno)s, %(familiar_alumno)s )
            """, data)
            self.conn.commit()


    def delete(self, alumno_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Alumnos
        :param clase_id:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "Alumnos" WHERE alumno_id = %(alumno_id)s
            """, {"alumno_id": alumno_id})
            self.conn.commit()


    def update(self, alumno_id: int, updated_data):
        """
        CRUD UPDATE. Actualiza un registro específico en la tabla Alumnos
        :param clase_id:
        :param updated_data:
        :return:
        """
        update_data = updated_data.dict()
        update_data["alumno_id"] = alumno_id  # Agregar alumno_id al diccionario de datos a actualizar
        with self.conn.cursor() as cur:     # Actualización de los valores en la base de datos
            cur.execute("""                 
                UPDATE "Alumnos" SET
                nombre_alumno = %(nombre_alumno)s,
                apellidos_alumno = %(apellidos_alumno)s,
                edad_alumno = %(edad_alumno)s,
                telefono_alumno = %(telefono_alumno)s,
                email_alumno = %(email_alumno)s,
                familiar = %(familiar)s
                WHERE alumno_id = %(alumno_id)s
            """, {"nombre_alumno": update_data["nombre_alumno"], "apellidos_alumno": update_data["apellidos_alumno"],
                  "edad_alumno": update_data["edad_alumno"], "telefono_alumno": update_data["telefono_alumno"],
                  "email_alumno": update_data["email_alumno"], "familiar": update_data["familiar"], "alumno_id": alumno_id})
            self.conn.commit()


    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
