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
        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM "Pagos" """)
            data = cur.fetchall()
            return data

    def insert(self, data):
        """
        CRUD CREATE. Inserta un registro en la tabla Pagos
        :param data:
        :return:
        """

        #importe_pagado = data["importe_pagado"]
        alumno_id = data["alumno_id"]
        clase_id = data["clase_id"]
        fecha_pago = data["fecha_pago"]


        # Obtener el precio de la clase de la tabla Clases
        with self.conn.cursor() as cur:
            cur.execute(
                """
                    SELECT precio_clase FROM "Clases" WHERE clase_id = %(clase_id)s
                """,{"clase_id": clase_id})
            precio_clase = cur.fetchone()[0]

        # Consulta para obtener el número de clases inscritas para el alumno
        # with self.conn.cursor() as cur:
        #     cur.execute(
        #         """
        #             SELECT COUNT(*) FROM "Pagos" WHERE alumno_id = %s
        #         """, (alumno_id,))
        #     clases_inscritas = cur.fetchone()[0]
        #     clases_inscritas += 1

        # Obtener el tipo de pack de la clase de la tabla Clases
        with self.conn.cursor() as cur:
            cur.execute(
                """
                    SELECT pack FROM "Clases" WHERE clase_id = %(clase_id)s
                """, {"clase_id": clase_id})
            tipo_pack = cur.fetchone()[0]

        # Consulta para obtener el número de clases inscritas para el alumno
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


        if tipo_pack in [pack for _, pack, _ in clases_por_pack] and tipo_pack != 0:
            clases_inscritas_pack = clases_inscritas_pack = next(clases for _, pack, clases in clases_por_pack if pack == tipo_pack)
            clases_inscritas_pack += 1
            if clases_inscritas_pack < 2:
                descuento = 0.0
                if es_familiar:
                    descuento = 0.1
            elif 2 <= clases_inscritas_pack <= 3:
                descuento = 0.5
                if es_familiar:
                    descuento = (1 - 0.5) * (1 - 0.1)
            elif clases_inscritas_pack > 3:
                descuento = (1- 0.75)
                if es_familiar:
                    descuento = (1 - 0.75) * (1 - 0.1)
        else:
            descuento = 0.0
            if es_familiar:
                descuento = 0.1



        # Verificar si se aplica descuento basado en un pack de clases, el nro. de clases inscritas y el familiar
        # if tipo_pack > nro_packs:
        #     descuento = 0.0  # lo correcto es guardarlo como campo en una tabla
        #     if es_familiar:
        #         descuento = 0.1
        # else:
        #     match tipo_pack:
        #         case 1:
        #             if clases_pack_1 < 2:
        #                 descuento = 0.0
        #                 if es_familiar:
        #                     descuento = 0.1
        #             elif 2 <= clases_pack_1 <= 3:
        #                 descuento = 0.5
        #                 if es_familiar:
        #                     descuento = (1 - 0.5) * (1 - 0.1)
        #             elif clases_pack_1 > 3:
        #                 descuento = 0.75
        #                 if es_familiar:
        #                     descuento = (1 - 0.75) * (1 - 0.1)
        #         case 2:
        #             if clases_pack_2 < 2:
        #                 descuento = 0.0
        #                 if es_familiar:
        #                     descuento = 0.1
        #             elif 2 <= clases_pack_2 <= 3:
        #                 descuento = 0.5
        #                 if es_familiar:
        #                     descuento = (1 - 0.5) * (1 - 0.1)
        #             elif clases_pack_2 > 3:
        #                 descuento = 0.75
        #                 if es_familiar:
        #                     descuento = (1 - 0.75) * (1 - 0.1)
        #         case 3:
        #             if clases_pack_3 < 2:
        #                 descuento = 0.0
        #                 if es_familiar:
        #                     descuento = 0.1
        #             elif 2 <= clases_pack_3 <= 3:
        #                 descuento = 0.5
        #                 if es_familiar:
        #                     descuento = (1 - 0.5) * (1 - 0.1)
        #             elif clases_pack_3 > 3:
        #                 descuento = 0.75
        #                 if es_familiar:
        #                     descuento = (1 - 0.75) * (1 - 0.1)
        #         case 0:
        #             if es_familiar:
        #                 descuento = 0.1


        # Calcular el importe pagado con el descuento aplicado
        importe_pagado_descuento = precio_clase *  descuento

        # Actualizar el diccionario de datos con el importe pagado calculado
        data["importe_pagado"] = importe_pagado_descuento

        # Insertar el registro en la tabla "Pagos" con el importe pagado calculado

        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "Pagos"(importe_pagado, alumno_id, clase_id, fecha_pago) 
                VALUES (%(importe_pagado)s, %(alumno_id)s, %(clase_id)s, %(fecha_pago)s )
            """, data)
            self.conn.commit()


    def delete(self, pago_id: int):
        """
        CRUD DELETE. Borra un registro específico en la tabla Pagos
        :param pago_id:
        :return:
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                    DELETE FROM "Pagos" WHERE pago_id = %(pago_id)s
                """, {"pago_id": pago_id})
            self.conn.commit()


    def update(self, pago_id: int, updated_data):
        """
        CRUD UPDATE. Actualiza un registro específico en la tabla Pagos
        :param pago_id:
        :param updated_data:
        :return:
        """
        update_data = updated_data.dict()
        update_data["pago_id"] = pago_id  # Agregar clase_id al diccionario de datos a actualizar
        with self.conn.cursor() as cur:     # Actualización de los valores en la base de datos
            cur.execute("""
                    UPDATE "Pagos" SET
                    importe_pagado = %(importe_pagado)s,
                    alumno_id = %(alumno_id)s,
                    clase_id = %(clase_id)s,
                    fecha_pago = %(fecha_pago)s
                    WHERE pago_id = %(pago_id)s
                """, {"importe_pagado": update_data["importe_pagado"], "alumno_id": update_data["alumno_id"],
                      "clase_id": update_data["clase_id"], "fecha_pago": update_data["fecha_pago"],"pago_id": pago_id})
            self.conn.commit()


    def pagos_by_alumnos(self, alumno_id):
        with self.conn.cursor() as cur:
            cur.execute(
                """
                   SELECT alumno_id, clase_id, importe_pagado, fecha_pago
                   FROM "Pagos"
                   WHERE alumno_id = %(alumno_id)s
                """, {"alumno_id": alumno_id})
            data = cur.fetchall()
            return data
            self.conn.commit()

    def calculo_descuento_pack(self):
        """
        Función que calcula el descuento por packs
        :return:
        """
        pass


    def __del__(self):
        """
        Cierra la base de datos
        :return:
        """
        if self.conn is not None and not self.conn.closed:
            self.conn.close()


