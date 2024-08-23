import mysql.connector
class Con:
    def __init__(self,host,username,password,database):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__database = database

        self.__db = mysql.connector.connect(
            host = self.__host,
            username = self.__username,
            passwd = self.__password,
            database = self.__database
        )

    def Database(self):
        return self.__db
    