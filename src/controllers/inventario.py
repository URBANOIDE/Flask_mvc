import marshal
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for, session
from src import app
from src.models.inventario import InventarioModel

@app.route('/inventario', methods =['GET', 'POST'])
def inventario():
    #verificacion de si se ha iniciado sesion, para que no puedan acceder a la ruta sin haberse logueado
    if session == {}:
        return render_template('login/login.html')
    #aunque se haya logueado, solo el administrador podrá ingresar a la ruta
    if session['usuario'] == 'empleado':
        session.pop('usuario', None)
        session.pop('administradorA', None)
        session.pop('administrador', None)
        session.pop('id', None)
        session.pop('identificacion', None)
        return render_template('login/login.html')
    if request.method == 'GET':
        inventarioModel = InventarioModel()
        inventarios = inventarioModel.traerTodos()
        precios_vendidos = inventarioModel.traerPreciosProductosVendidos()
        ganancia = 0
        f=0
        for e in precios_vendidos:
            f = ((e[1]+e[3])*e[2])-(e[0]*e[2])
            ganancia += f
        return render_template('inventario/index.html', inventarios=inventarios, ganancia=ganancia)

    #### Cuando viene por metodo POST, para hacer una busqueda con las fechas
    fechaInicial = request.form.get('fecha_inicio')
    fechaFinal = request.form.get('fecha_final')

    inventarioModel = InventarioModel()
    inventarios = inventarioModel.traerTodosFecha(fechaInicial, fechaFinal)
    precios_vendidos = inventarioModel.traerPreciosProductosVendidosFecha( fechaInicial, fechaFinal)
    ganancia = 0
    f=0
    for e in precios_vendidos:
        f = ((e[1]+e[3])*e[2])-(e[0]*e[2])
        ganancia += f
    return render_template('inventario/index.html', inventarios=inventarios, ganancia=ganancia, fechaFinal=fechaFinal, fechaInicial=fechaInicial)
    