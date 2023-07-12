import psycopg


class DataBaseConnection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=Fenix user=postgres password=9527 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def __def__(self):
        self.conn.close()
