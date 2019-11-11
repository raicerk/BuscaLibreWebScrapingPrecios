import psycopg2

class database:

    def setLink(self):
        print("si llego")
        try:
            connection = psycopg2.connect(
                user = "raicerk",
                password = "qwerty123",
                host="172.18.0.2",
                port="5432",
                database="buscalibreprecios"
            )

            cursor = connection.cursor()

            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("listo", record)
            return record

        except (Exception, psycopg2.Error) as error:
            print(error)