import marshal
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for, session
from src import app
from src.models.inventario import InventarioModel

@app.route('/inventario', methods =['GET', 'POST'])
def inventario():
    if request.method == 'GET':
        inventarioModel = InventarioModel()
        inventarios = inventarioModel.traerTodos()
        precios_vendidos = inventarioModel.traerPreciosProductosVendidos()
        ganancia = 0
        f=0
        for e in precios_vendidos:
            f = (e[1]-e[0])*e[2]
            ganancia += f
        #Verificacion de url para usuarios no identificados
        #print(session['usuario'])
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
        f = (e[1]-e[0])*e[2]
        ganancia += f
    #Verificacion de url para usuarios no identificados
    #print(session['usuario'])
    return render_template('inventario/index.html', inventarios=inventarios, ganancia=ganancia)
    