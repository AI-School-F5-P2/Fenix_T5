import psycopg
from psycopg import Error
from db_connection import DataBaseConnection


class Pagos():
    def __init__(self):
        self.conn = DataBaseConnection().get_connection()  # Obtiene la conexión de la clase DataBaseConnection

    def read_all_pagos(self):
        """
        CRUD READ. Lee todos los registros de la tabla Pagos
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "Pagos" """)
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            # Manejo de la excepción específica para errores de lectura en la base de datos
            print("Error al leer los registros de la tabla Pagos:", e)
            raise  # Re-lanzar la excepción para que se capture en la API

def insert(self, data):
    """
    CRUD CREATE. Inserta un registro en la tabla Pagos.
    Antes de insertar el registro, calcula el descuento que le corresponde al alumno
    :param data:
    :return:
    """
    try:
        alumno_id = data["alumno_id"]
        clase_id = data["clase_id"]
        fecha_pago = data["fecha_pago"]

# Insertar alumno_id y clase_id en Tabla Alumnos_clases
# Necesario ya que es una tabla intermmedia y los dos
# campos que tiene, alumno_id y clase_id deben estar presentes
# antes de poder insertar un campo en la Tabla Pagos        

        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO  "Alumnos_clases"(alumno_id, clase_id)
                VALUES (%(alumno_id)s, %(clase_id)s)
                """, {"alumno_id": alumno_id, "clase_id": clase_id})
            self.conn.commit()

        
        # Obtener el precio de la clase de la tabla Clases
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT precio_clase FROM "Clases" WHERE clase_id = %(clase_id)s
                """, {"clase_id": clase_id})
            precio_clase = cur.fetchone()[0]

        
        # Obtener el tipo de pack de la clase de la tabla Clases
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT pack FROM "Clases" WHERE clase_id = %(clase_id)s
                """, {"clase_id": clase_id})
            tipo_pack = cur.fetchone()[0]


        
        # Consulta para obtener el número de clases inscritas para el alumno por pack
        # clases_por_pack es una lista de tuplas que contiene los valores de alumno_id, pack y clases_inscritas
        # [(alumno_id, pack,clases_inscritas)]
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT "Pagos".alumno_id, "Clases".pack, COUNT(*) AS clases_inscritas
                FROM "Pagos"
                JOIN "Clases" ON "Pagos".clase_id = "Clases".clase_id
                WHERE "Pagos".alumno_id = %s 
                GROUP BY "Pagos".alumno_id, "Clases".pack;
                """, (alumno_id,)
            )
            clases_por_pack = cur.fetchall()

        
        # Obtener valor de familiar de la tabla Alumnos
        with self.conn.cursor() as cur:
            cur.execute(
                """
                SELECT familiar FROM "Alumnos" WHERE alumno_id = %(alumno_id)s
                """, {"alumno_id": alumno_id})
            es_familiar = cur.fetchone()[0]

        
        # Se calculan los descuentos
        if tipo_pack in [pack for _, pack, _ in clases_por_pack] and tipo_pack != 0:
            clases_inscritas_pack = clases_inscritas_pack = next(clases for _, pack, clases in clases_por_pack if pack == tipo_pack)
            clases_inscritas_pack += 1
            if clases_inscritas_pack < 2:
                descuento = 0.0
                if es_familiar:
                    descuento = 0.1
                    es_familiar = False
            elif 2 <= clases_inscritas_pack <= 3:
                descuento = 0.5
                if es_familiar:
                    descuento = (1 - 0.5) * (1 - 0.1)
                    es_familiar = False
            elif clases_inscritas_pack > 3:
                descuento = (1 - 0.75)
                if es_familiar:
                    descuento = (1 - 0.75) * (1 - 0.1)
                    es_familiar = False
        else:
            descuento = 1
            if es_familiar:
                descuento = (1 - 0.1)
                es_familiar = False


        # Calcular el importe pagado con el descuento aplicado
        importe_pagado_descuento = precio_clase * descuento

        
        # Actualizar el diccionario de datos con el importe pagado calculado
        data["importe_pagado"] = importe_pagado_descuento

        
        # Insertar el registro en la tabla "Pagos" con el importe pagado calculado
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "Pagos"(importe_pagado, alumno_id, clase_id, fecha_pago) 
                VALUES (%(importe_pagado)s, %(alumno_id)s, %(clase_id)s, %(fecha_pago)s)
            """, data)
            self.conn.commit()
      
        # Actualizar a "false" el campo familiar en la tabla Alumnos.
        if not es_familiar:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE "Alumnos" SET familiar = false 
                    WHERE alumno_id = %(alumno_id)s
                """, {"alumno_id": alumno_id})
                self.conn.commit()

    except psycopg.Error as e:
        print("Error al insertar el registro en la tabla Pagos:", e)
        raise





    def delete(self, pago_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Pagos
        :param pago_id:
        :return:
        """
        # Hay que borrar primero el registro correspondiente en la tabla
        # Alumnos_clases

        # Se selecciona el alumno_id y clase_id para saber que registro se va a borrar
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT alumno_id, clase_id FROM "Pagos" 
                    WHERE pago_id = %(pago_id)s
                    """, {"pago_id": pago_id})# Combinamos los parámetros en un solo diccionario
                # Obtenemos los valores encontrados de los campos alumno_id y clase_id
                result = cur.fetchone()

                # Guardamos los valores encontrados en variables separadas
                alumno_id_encontrado = result[0]# Primer elemento del resultado es alumno_id
                clase_id_encontrado = result[1]# Segundo elemento del resultado es clase_id
            
            # Se procede a borrar el registro en la tabla Alumnos_clases
            with self.conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM "Alumnos_clases" WHERE alumno_id = %(alumno_id)s AND clase_id = %(clase_id)s
                """, {"alumno_id": alumno_id_encontrado, "clase_id": clase_id_encontrado})
                self.conn.commit()

            # Ahora sí se puede borrar el registr en la tabla Pagos
            with self.conn.cursor() as cur:
                cur.execute("""
                    DELETE FROM "Pagos" WHERE pago_id = %(pago_id)s
                """, {"pago_id": pago_id})
                self.conn.commit()

        except psycopg.Error as e:
            print("Error al eliminar el registro de la tabla Pagos:", e)
            raise



    def update(self, pago_id: int, updated_data):
        """
        CRUD UPDATE. Actualiza un registro específico en la tabla Pagos
        :param pago_id:
        :param updated_data:
        :return:
        """
        update_data = updated_data.dict()
        update_data["pago_id"] = pago_id # Agregar clase_id al diccionario de datos a actualizar
        try:
            with self.conn.cursor() as cur:  # Actualización de los valores en la base de datos
                cur.execute("""
                    UPDATE "Pagos" SET
                    importe_pagado = %(importe_pagado)s,
                    alumno_id = %(alumno_id)s,
                    clase_id = %(clase_id)s,
                    fecha_pago = %(fecha_pago)s
                    WHERE pago_id = %(pago_id)s
                """, {"importe_pagado": update_data["importe_pagado"],
                    "alumno_id": update_data["alumno_id"],
                    "clase_id": update_data["clase_id"],
                    "fecha_pago": update_data["fecha_pago"],
                    "pago_id": pago_id})
                self.conn.commit()

        except psycopg.Error as e:
            print("Error al actualizar el registro de la tabla Pagos:", e)
            raise



    def pagos_by_alumnos(self, alumno_id):
        """
        Obtiene todos los registros de la Tabla "Pagos" para un alumno específico
        :param alumno_id:
        :return:
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT alumno_id, clase_id, importe_pagado, fecha_pago
                    FROM "Pagos"
                    WHERE alumno_id = %(alumno_id)s
                    """, {"alumno_id": alumno_id})
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            print("Error al obtener los registros de la tabla Pagos para el alumno:", e)
            raise



    def total_pagado_alumno(self, alumno_id):
        """
        Función que calcula el total pagado por el alumno
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute(
                """
                   SELECT alumno_id, SUM(importe_pagado) AS total_pagado
                   FROM "Pagos"
                   WHERE alumno_id = %(alumno_id)s  
                   GROUP BY alumno_id              
                """, {"alumno_id": alumno_id})
            data = cur.fetchall()
            return data


    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()


