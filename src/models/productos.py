from src.config.db import DB


class ProductosModel():

    def traerTodos(self):
        cursor= DB.cursor()

        cursor.execute('select * from productos')

        productos = cursor.fetchall()

        cursor.close()

        return productos
    def crear(self, nombre):
        cursor = DB.cursor()

        cursor.execute('insert into productos(nombre) values(?)', (nombre,))
        cursor.close()