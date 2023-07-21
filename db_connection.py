import psycopg


class DataBaseConnection:

    def __init__(self):
        """
        Constructor. Conecta con la DB
        """
        try:
            self.conn = psycopg.connect(
                dbname="Fenix",
                user="neo",
                password="4972",
                host="localhost",
                port=5433
            )
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()
            raise

    def get_connection(self):
        """
        Conecta con la DB
        :return:
        """
        return self.conn
