import marshal
from turtle import circle
import pdfkit
import random
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for, session, make_response
from src import app
from src.models.ventas import VentasModel

@app.route('/ventas', methods =['GET', 'POST'])
def ventas():
    if request.method == 'GET':
        #TRAER LOS CARGOS PARA HACERLOS SELECCIONABLES AL CREAR UN PRODUCTO
        ventasModel = VentasModel()
        clientes = ventasModel.traerClientes()
        longitud = 10
        #caracteres a seleccionar aleaotorios
        caracter = "abcdefghijklmñopqrstuvwxyz1234567890"
        #4 caracteres aleatorios, guardar en bd como url_corta
        codigo = ""
        codigo = codigo.join(random.choice(caracter) for i in range(longitud))
        #mostramos el formulario de creacion
        return render_template('ventas/cliente.html', clientes = clientes, codigo=codigo)
    n_factura = request.form.get('codigo')
    cliente = request.form.get('cliente')

    ventasModel = VentasModel()
    productos = ventasModel.traerTodos()
    return render_template('ventas/index.html', productos = productos, n_factura=n_factura, cliente=cliente)

@app.route('/ventas/registro/<int:id>/<string:cliente>/<string:n_factura>', methods =['GET', 'POST'])
def ventasRegistro(id, cliente, n_factura):
    if request.method == 'GET':
        ventasModel = VentasModel()
        producto = ventasModel.traerProducto(id)
        for p in producto:
            producto = p[0]
        precio = ventasModel.traerPrecio(id)
        for pr in precio:
            precio = pr[0]
        return render_template('ventas/total.html', producto = producto, precio=precio)

    id_empleado_factura = session['id']
    id_producto_factura = id

    ventasModel = VentasModel()
    id_cliente_factura = ventasModel.traerIdCliente(cliente)
    for c in id_cliente_factura:
        id_cliente_factura = c[0]

    cantidad = request.form.get('cantidad')
    total = request.form.get('total')

    ventasModel.crear(n_factura, id_empleado_factura, id_cliente_factura, id_producto_factura, cantidad, total)
    productos = ventasModel.traerTodos()
    

    #volver a pasarle los parametros (cliente, codigo) para volver a crear otro rgistro
    return render_template('ventas/index.html', productos=productos, n_factura=n_factura, cliente=cliente )


@app.route('/facturas/registro/<string:cliente>/<string:n_factura>', methods =['GET', 'POST'])
def factura(cliente, n_factura):
    if request.method == 'GET':
        id_empleado = session['iden']
        nombre_empleado = session['administrador']
        apellido_empleado = session['administradorA']

        ventasModel = VentasModel()
        datos_cliente = ventasModel.datosClientes(cliente)
        for datos in datos_cliente:
            id_cliente = datos[0]
            nombre_cliente = datos[1]
            apellido_cliente = datos [2]
        
        facturas = ventasModel.traerFactura(n_factura)

        #suma del total del precio de los productos almacenado en la variable total
        total = 0
        for e in facturas:
            f = e[4]
            total += e[4]        
        return render_template('ventas/factura.html', n_factura=n_factura, facturas=facturas, id_empleado=id_empleado, cliente=cliente, total=total, nombre_empleado=nombre_empleado, apellido_empleado=apellido_empleado, id_cliente=id_cliente, nombre_cliente=nombre_cliente, apellido_cliente=apellido_cliente)

    