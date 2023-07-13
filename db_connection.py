import psycopg


class DataBaseConnection:

    def __init__(self):
        try:
            self.conn = psycopg.connect(
                dbname="Fenix",
                user="postgres",
                password="9527",
                host="localhost",
                port=5432
            )
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()
            raise

    # def __del__(self):
    #     self.conn.close()

    def get_connection(self):
        return self.conn
