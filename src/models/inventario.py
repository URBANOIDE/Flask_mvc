from select import select
from colorama import Cursor
from src.config.db import DB
from src.controllers.home import index


class InventarioModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT n_factura, cedula_cliente, nombres_producto, cantidad, precio_compra, precio_venta, ganancia, total, total_con_iva, (((precio_venta + ganancia)*cantidad) - (precio_compra * cantidad)) AS ganancia, fecha FROM factura INNER JOIN productos ON factura.id_producto_factura = productos.id_producto INNER	JOIN clientes ON factura.id_cliente_factura = clientes.id_cliente')

        inventario = cursor.fetchall()

        cursor.close()

        return inventario

    def traerPreciosProductosVendidos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT precio_compra, precio_venta, cantidad, ganancia FROM factura INNER JOIN productos ON factura.id_producto_factura = productos.id_producto INNER	JOIN clientes ON factura.id_cliente_factura = clientes.id_cliente')

        precios_vendidos = cursor.fetchall()

        cursor.close()

        return precios_vendidos
    def traerTodosFecha(self, fechaInicial, fechaFinal):
        cursor = DB.cursor()

        cursor.execute('SELECT n_factura, cedula_cliente, nombres_producto, cantidad, precio_compra, precio_venta, ganancia, total, (((precio_venta + ganancia)*cantidad) - (precio_compra * cantidad)) AS ganancia, fecha FROM factura INNER JOIN productos ON factura.id_producto_factura = productos.id_producto INNER	JOIN clientes ON factura.id_cliente_factura = clientes.id_cliente WHERE((fecha  >= ?) AND (fecha <= ?))', (fechaInicial, fechaFinal))

        inventario = cursor.fetchall()

        cursor.close()

        return inventario

    def traerPreciosProductosVendidosFecha(self, fechaInicial, fechaFinal):
        cursor = DB.cursor()

        cursor.execute('SELECT precio_compra, precio_venta, cantidad, ganancia FROM factura INNER JOIN productos ON factura.id_producto_factura = productos.id_producto INNER	JOIN clientes ON factura.id_cliente_factura = clientes.id_cliente WHERE((fecha  >= ?) AND (fecha <= ?))', (fechaInicial, fechaFinal))

        precios_vendidos = cursor.fetchall()

        cursor.close()

        return precios_vendidos