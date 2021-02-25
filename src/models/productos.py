from src.config.db import DB


class ProductosModel():

    def traerTodos(self):
        cursor= DB.cursor()

        cursor.execute('select * from productos')

        productos = cursor.fetchall()

        cursor.close

        return productos
    def crear(self, data):
        pass