import psycopg
# from db_connection import DataBaseConnection
#
#
# class Clases():
#     conn = None
#
#     def __init__(self):
#         try:
#             self.conn = psycopg.connect("dbname=Fenix user=postgres password=9527 host=localhost port=5432")
#         except psycopg.OperationalError as err:
#             print(err)
#             self.conn.close()


def read_all_clases(self):
    with self.conn.cursor() as cur:
        data = cur.execute(
            """
                        SELECT * FROM "Clases" 
                        """)
        return data.fetchall()


def write(self, data):
    with self.conn.cursor() as cur:
        cur.execute(
            """
                        INSERT INTO "Clases"(nombre_clase, nivel_clase, precio_clase) VALUES(
                        %(nombre_clase)s, %(nivel_clase)s, %(precio_clase)s)
                        """, data)
        self.conn.commit()


def __def__(self):
    self.conn.close()
