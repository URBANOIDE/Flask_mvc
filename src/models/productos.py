import src.config.globals as globals
from src.controllers.home import index


class ProductosModel():
    def traerTodos(self):
        cursor = globals.DB.cursor()

        cursor.execute('select * from productos')

        productos = cursor.fetchall()

        cursor.close()

        return productos

    def crear(self, nombre,descripcion,precio_compra, precio_venta, ganancia, estado):
        cursor = globals.DB.cursor()

        cursor.execute('insert into productos(nombre,descripcion,precio_compra,precio_venta, ganancia, estado) values(?,?,?,?,?,?)', (nombre,descripcion,precio_compra,precio_venta,ganancia,estado))
        
        cursor.close()

    def editar(self, id, nombre, descripcion, precio_venta, ganancia, precio_compra, estado):
        cursor = globals.DB.cursor()

        cursor.execute(""" UPDATE productos SET nombre = ?, descripcion = ?, precio_compra = ?, precio_venta = ?, ganancia = ?, estado = ?  WHERE id = ?""",(nombre, descripcion, precio_compra, precio_venta, ganancia, estado, id,))
        
        cursor.close()
    
    def mostrar():
        cursor = globals.DB.cursor()
        
        cursor.execute("show databases")
        bases = cursor.fetchall()
        cursor.close()
        return index
        
        