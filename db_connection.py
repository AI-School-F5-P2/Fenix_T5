import os
import psycopg
from dotenv import load_dotenv


class DataBaseConnection:

    def __init__(self):
        """
        Constructor. Conecta con la DB
        """
        load_dotenv()  # Carga las variables de entorno desde el archivo .env
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")

        try:
            self.conn = psycopg.connect(
                dbname="fenix_dance",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
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
