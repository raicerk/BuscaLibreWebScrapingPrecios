import psycopg2

class database:

    connection = object
    link = ""

    def __init__(self): 
        self.connection = psycopg2.connect(
                user = "raicerk",
                password = "qwerty123",
                host="172.18.0.2",
                port="5432",
                database="buscalibreprecios"
            )

    def setLink(self):

        try:
            insert_query = "INSERT INTO LINK (link, estado) values ('{}',{})".format(self.link, True)
            cursor = self.connection.cursor()
            cursor.execute(insert_query)
            self.connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into mobile table")
            return count

        except (Exception, psycopg2.Error) as error:
            print(error)