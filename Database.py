import psycopg2
import Scraping as scraping
import time

class database:

    connection = object
    idlink = 0
    link = ""
    nombre=""
    autor=""
    fecha=''
    precio = 0

    def __init__(self): 
        self.connection = psycopg2.connect(
                user = "raicerk",
                password = "qwerty123",
                host="127.0.0.1",
                port="5432",
                database="buscalibre"
            )

    def setPrecio(self):

        try:
            insert_query = "INSERT INTO precio (idlink, precio, fecha, nuevo) values ({}, {}, '{}', {}) RETURNING id;".format(self.idlink, self.precio, self.fecha, True)
            cursor = self.connection.cursor()
            cursor.execute(insert_query)
            id_inserted = cursor.fetchone()[0]
            self.connection.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into table")
            print (id_inserted, "ID inserted successfully into table")
            return id_inserted

        except (Exception, psycopg2.Error) as error:
            print(error)

    def getListalink(self):

        try:
            print("::::::: Comenzando scraping :::::::")
            
            self.updatePrecioNuevo()

            select_query = '''SELECT link.id,
                link.link        
            FROM public.link AS link
            '''
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            datos = cursor.fetchall()                
            self.connection.commit()
            arrayprecios = []
            for row in datos:

                scr = scraping.scraping()
                scr.url = row[1]
                result = scr.scrap()

                select_query_precio_anterior = '''
                    SELECT precio.precio
                    FROM public.precio as precio
                    where precio.idlink = {} and
                    precio.nuevo = false
                    order by precio.fecha desc
                    limit 1
                '''.format(row[0])

                cursor2 = self.connection.cursor()
                cursor2.execute(select_query_precio_anterior)
                datas = cursor2.fetchone()               
                self.connection.commit()
                self.precio = scr.price
                self.idlink = row[0]
                self.fecha = time.strftime("%Y-%m-%d")
                if(datas is None):
                    arrayprecios.append(self.setPrecio())
                elif((scr.price != datas[0])):
                    arrayprecios.append(self.setPrecio())

            return arrayprecios
        except (Exception, psycopg2.Error) as error:
            print(error)

    def updatePrecioNuevo(self):

        try:
            
            update_query = "UPDATE public.precio SET nuevo=false"
            cursor = self.connection.cursor()
            cursor.execute(update_query)
            self.connection.commit()
            count = cursor.rowcount
            return count

        except (Exception, psycopg2.Error) as error:
            print(error)