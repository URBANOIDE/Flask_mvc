import marshal
from re import M
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for, session
from src import app
from src.models.cargos import CargosModel

@app.route('/cargos')
def cargos():
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

    cargosModel = CargosModel()
    cargos = cargosModel.traerTodos()
    return render_template('cargos/index.html', cargos=cargos)

@app.route('/cargos/eliminado/<int:id>', methods=['GET', 'POST'])
def eliminar_cargo(id):
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

    cargosModel = CargosModel()
    cargosModel.eliminarEmpleadoCargo(id)
    cargosModel.eliminar(id)
    cargos = cargosModel.traerTodos()
   
    return render_template('cargos/index.html', cargos= cargos)

@app.route('/cargos/crear', methods =['GET', 'POST'])
def crear_cargo():
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
        cargosModel = CargosModel()
        #mostramos el formulario de creacion
        return render_template('cargos/crear.html')

    nombre = request.form.get('cargo')
    sueldo = request.form.get('sueldo')
      
    cargosModel = CargosModel()

    cargosModel.crear(nombre, sueldo)    
    
    #aca es la cracion del producto
    return redirect(url_for('cargos'))

@app.route('/cargos/editar/<int:id>', methods=['GET', 'POST'])
def editar_cargo(id):
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
        ########TRAER LOS CARGOS PARA HACERLOS SELECCIONABLES AL EDITAR UN PRODUCTO
        cargosModel = CargosModel()
        #cargo
        cargo = cargosModel.traerCargo(id)
        for m in cargo:
            cargo =m[0]
        #nombres
        sueldo = cargosModel.traerSueldo(id)
        for n in sueldo:
            sueldo =n[0]
        #mostramos el formulario de edicion
        return render_template('cargos/editar.html',cargo=cargo, sueldo=sueldo)

    nombre = request.form.get('cargo')
    sueldo = request.form.get('sueldo')
      
    cargosModel = CargosModel()
        
    cargosModel.editar(id, nombre, sueldo)
    #aca es la creacion del producto
    return redirect(url_for('cargos'))