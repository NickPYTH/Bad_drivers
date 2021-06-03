import psycopg2
from contextlib import closing

class BadDriversSeed():
    """Class for seeding testing values"""
    __cursor = None
    __connection = None
    def __init__(self):
        self.__connection = psycopg2.connect(
                    user="hello_django",
                    password="hello_django",
                    host="127.0.0.1",
                    port="5432",
                    database="postgres")
        self.__cursor = self.__connection.cursor()

    def reports_car_table_seed(self, *args):
        if len(args) == 3:
            data_to_insert = []
            for arg in args:
                data_to_insert.append(arg)
            try:
                postgres_insert_query = """ INSERT INTO reports_car (car_number, car_region, car_country) VALUES (%s,%s,%s)"""
                self.__cursor.execute(postgres_insert_query, data_to_insert)
                self.__connection.commit()
                count = self.__cursor.rowcount
                print(count, "Success")

            except (Exception, psycopg2.Error) as error:
                print("Insert error: ", error)

            finally:
                if self.__connection:
                    self.__cursor.close()
                    self.__connection.close()
                    print("Conection is closed")

    def auth_users_table_seed(self, *args):
        if len(args) == 10:
            data_to_insert = []
            for arg in args:
                data_to_insert.append(arg)
            try:
                postgres_insert_query = """ INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff,
                              is_active, date_joined)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
                self.__cursor.execute(postgres_insert_query, data_to_insert)
                self.__connection.commit()
                count = self.__cursor.rowcount
                print(count, "Success")

            except (Exception, psycopg2.Error) as error:
                print("Insert error: ", error)

            finally:
                if self.__connection:
                    self.__cursor.close()
                    self.__connection.close()
                    print("Conection is closed")
    
    def reports_car_table_seed(self, *args):
        if len(args) == 3:
            data_to_insert = []
            for arg in args:
                data_to_insert.append(arg)
            try:
                postgres_insert_query = """ INSERT INTO reports_car (car_number, car_region, car_country) VALUES (%s,%s,%s)"""
                self.__cursor.execute(postgres_insert_query, data_to_insert)
                self.__connection.commit()
                count = self.__cursor.rowcount
                print(count, "Success")

            except (Exception, psycopg2.Error) as error:
                print("Insert error: ", error)

            finally:
                if self.__connection:
                    self.__cursor.close()
                    self.__connection.close()
                    print("Conection is closed")
        