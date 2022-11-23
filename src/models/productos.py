from src.config.db import DB
from src.controllers.home import index


class ProductosModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT id_producto, nombres_provedor, nombre_marca, nombres_producto, precio_compra, precio_venta, ganancia  FROM productos INNER JOIN marcas ON productos.id_marca_producto = marcas.id_marca INNER JOIN provedores ON productos.id_provedor_producto = provedores.id_provedor ORDER	BY id_producto  ASC')

        productos = cursor.fetchall()

        cursor.close()

        return productos
        
    def eliminar(self, id):
        cursor = DB.cursor()

        cursor.execute("""DELETE FROM productos WHERE id_producto = ?""", (id,))

        cursor.close()

    def crear(self, id_provedor_producto,id_marca_producto,nombres_producto,precio_compra,precio_venta,ganancia):
        cursor = DB.cursor()

        cursor.execute('insert into productos(id_provedor_producto,id_marca_producto,nombres_producto,precio_compra,precio_venta,ganancia) values(?,?,?,?,?,?)', (id_provedor_producto,id_marca_producto,nombres_producto,precio_compra,precio_venta,ganancia))
        
        cursor.close()

    def editar(self, id, id_provedor_producto,id_marca_producto,nombres_producto,precio_compra,precio_venta,ganancia):
        cursor = DB.cursor()

        cursor.execute(""" UPDATE productos SET id_provedor_producto = ?, id_marca_producto = ?, nombres_producto = ?, precio_compra = ?, precio_venta = ?, ganancia = ?  WHERE id_producto = ?""",(id_provedor_producto,id_marca_producto,nombres_producto,precio_compra,precio_venta,ganancia, id,))
        
        cursor.close()





    ######## Traemos los nombres de marca a mostrar en los textos de selección
    def traerMarcas(self):
        cursor = DB.cursor()

        cursor.execute('select nombre_marca from marcas')

        nombreMarcas = cursor.fetchall()

        cursor.close()

        return nombreMarcas
    ######## Traemos los nombres de productos a mostrar en los textos de selección
    def traerProveedores(self):
        cursor = DB.cursor()

        cursor.execute('select nombres_provedor from provedores')

        nombreProveedores = cursor.fetchall()

        cursor.close()

        return nombreProveedores
    ######## Traemos en id del provedor que se seleccionó
    def traerIdProvedor(self, nombreProvedor):
       
        cursor = DB.cursor()

        cursor.execute("select id_provedor from provedores where nombres_provedor = '"+ nombreProvedor +"'")

        id_provedor = cursor.fetchall()

        cursor.close()

        return id_provedor

    ######## Traemos en id del provedor que se seleccionó
    def traerIdMarca(self, nombreMarca):
        
        cursor = DB.cursor()

        cursor.execute("select id_marca from marcas where nombre_marca = '"+ nombreMarca +"'")

        id_marca = cursor.fetchall()

        cursor.close()

        return id_marca

    ##################
    #Requerimientos para editar, traer los datos ingresados para mostrar en el formulario y hacer su edicion
    ##################
    #marca
    def traerMarca(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombre_marca FROM productos INNER JOIN marcas ON productos.id_marca_producto = marcas.id_marca WHERE id_producto = ?""", (id,))

        marca = cursor.fetchall()

        cursor.close()

        return marca
    #provedor
    def traerProvedor(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombres_provedor FROM productos INNER JOIN provedores ON productos.id_provedor_producto = provedores.id_provedor WHERE id_producto = ?""", (id,))

        provedor = cursor.fetchall()

        cursor.close()

        return provedor
    #producto
    def traerProducto(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombres_producto FROM productos WHERE id_producto = ?""", (id,))

        producto = cursor.fetchall()

        cursor.close()

        return producto
    #precio_compra
    def traerPrecio_compra(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT precio_compra FROM productos WHERE id_producto = ?""", (id,))

        precio_compra = cursor.fetchall()

        cursor.close()

        return precio_compra
    #precio_venta
    def traerPrecio_venta(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT precio_venta FROM productos WHERE id_producto = ?""", (id,))

        precio_venta = cursor.fetchall()

        cursor.close()

        return precio_venta
    #precio_ganancias
    def traerGanancia(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT ganancia FROM productos WHERE id_producto = ?""", (id,))

        ganancia = cursor.fetchall()

        cursor.close()

        return ganancia
    ##################
    #Requerimientos para eliminar, eliminar la factura del producto eliminado
    ##################
    def eliminarFacturaProducto(self, id):
        cursor = DB.cursor()

        cursor.execute("""DELETE FROM factura WHERE id_producto_factura = ?""", (id,))

        cursor.close()