import os
from dotenv import load_dotenv
from mysql import MySQLConnection


class engine:
    def __init__(self, schema) -> None:
        self.__HOST = os.environ.get("DB_HOST")
        self.__PORT = os.environ.get("DB_PORT")
        self.__USER = os.environ.get("DB_USER")
        self.__PASS = os.environ.get("DB_PASS")
        self.__SCHEMA = schema
        self.__create_connection()

    def __create_connection(self):
        self.__connection = MySQLConnection(
            user=self.__USER,
            password=self.__PASS,
            host=self.__HOST,
            port=self.__PORT,
            database=self.__SCHEMA
        )

    def close_connection(self):
        self.__connection.close()
        self.__connection = None

    def restart_engine(self):
        self.close_connection()
        self.__create_connection()

    def execute_query(self, query):
        with self.__connection.cursor as cursor:
            cursor.execute(query)
            raw = cursor.fetchall()
            results = list(raw)
            raw_columns = cursor.column_names
            results = list(raw_columns)
        return

    def test_connection(self):
        query = "SELECT NOW()"
