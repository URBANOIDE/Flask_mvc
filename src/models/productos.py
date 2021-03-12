from src.config.globals as globals


class ProductosModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('select * from productos ')

        productos = cursor.fetchall()

        cursor.close()

        return productos

    def crear(self, nombre,descripcion,precio_compra, precio_venta, ganancia, estado):
        cursor = DB.cursor()

        cursor.execute('insert into productos(nombre,descripcion,precio_compra,precio_venta, ganancia, estado) values(?,?,?,?,?,?)', (nombre,descripcion,precio_compra,precio_venta,ganancia,estado))
        
        cursor.close()

    def editar(self, id, nombre, descripcion, precio_venta, ganancia, precio_compra, estado):
        cursor = DB.cursor()

        cursor.execute(""" UPDATE productos SET nombre = ?, descripcion = ?, precio_compra = ?, precio_venta = ?, ganancia = ?, estado = ?  WHERE id = ?""",(nombre, descripcion, precio_compra, precio_venta, ganancia, estado, id,))
        
        cursor.close()
    
        
        