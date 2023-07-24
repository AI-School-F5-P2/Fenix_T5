import psycopg


class DataBaseConnection:

    def __init__(self):
        """
        Constructor. Conecta con la DB
        """
        try:
            self.conn = psycopg.connect(
                dbname="fenix_dance",
                user="postgres",
                password="1234",
                host="localhost",
                port=5432
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
