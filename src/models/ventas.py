from src.config.db import DB
from src.controllers.home import index


class VentasModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT id_producto, nombres_provedor, nombre_marca, nombres_producto, precio_compra, precio_venta, ganancia  FROM productos INNER JOIN marcas ON productos.id_marca_producto = marcas.id_marca INNER JOIN provedores ON productos.id_provedor_producto = provedores.id_provedor')

        productos = cursor.fetchall()

        cursor.close()

        return productos
    def crear(self, n_factura, id_empleado_factura, id_cliente_factura, id_producto_factura, cantidad, total):
        cursor = DB.cursor()

        cursor.execute('insert into factura(n_factura, id_empleado_factura, id_cliente_factura, id_producto_factura, cantidad, total) values(?,?,?,?,?,?)', (n_factura, id_empleado_factura, id_cliente_factura, id_producto_factura, cantidad, total))
        
        cursor.close()

    def traerClientes(self):
        cursor = DB.cursor()

        cursor.execute('SELECT nombres_cliente  FROM clientes')

        clientes = cursor.fetchall()

        cursor.close()

        return clientes
    def traerIdCliente(self, cliente):
        cursor = DB.cursor()

        cursor.execute("SELECT id_cliente  FROM clientes where nombres_cliente = '"+ cliente +"'")

        id_cliente_factura = cursor.fetchall()

        cursor.close()

        return id_cliente_factura

    def traerProducto(self, id):
        cursor = DB.cursor()

        cursor.execute("SELECT nombres_producto  FROM productos where id_producto = ?",(id,))

        producto = cursor.fetchall()

        cursor.close()

        return producto

    def traerPrecio(self, id):
        cursor = DB.cursor()

        cursor.execute("SELECT precio_venta  FROM productos where id_producto = ?",(id,))

        precio = cursor.fetchall()

        cursor.close()

        return precio
    def traerFactura(self, n_factura):
        cursor = DB.cursor()

        cursor.execute("SELECT id_factura, nombres_producto, cantidad, total FROM factura INNER JOIN productos ON factura.id_producto_factura = productos.id_producto  where n_factura = '"+ n_factura +"'")

        facturas = cursor.fetchall()

        cursor.close()

        return facturas