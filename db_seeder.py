import psycopg2
from contextlib import closing

class BadDriversSeed():
    __cursor = None
    __connection = None
    def __init__(self):
        self.__connection = psycopg2.connect(
                    user="hello_django",
                    password="hello_django",
                    host="127.0.0.1",
                    port="5432",
                    database="hello_django_dev")
        self.__cursor = self.__connection.cursor()

    def reports_car_table_seed(self): #add args
        try:
            postgres_insert_query = """ INSERT INTO reports_car (car_number, car_region, car_country) VALUES (%s,%s,%s)"""
            record_to_insert = (5, 1, 950)
            self.__cursor.execute(postgres_insert_query, record_to_insert)
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

a = BadDriversSeed()

a.reports_car_table_seed()