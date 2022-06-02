import marshal
from re import M
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for
from src import app
from src.models.cargos import CargosModel

@app.route('/cargos')
def cargos():
    cargosModel = CargosModel()
    cargos = cargosModel.traerTodos()
    return render_template('cargos/index.html', cargos=cargos)

@app.route('/cargos/eliminado/<int:id>', methods=['GET', 'POST'])
def eliminar_cargo(id):
    cargosModel = CargosModel()
    cargosModel.eliminarEmpleadoCargo(id)
    cargosModel.eliminar(id)
    cargos = cargosModel.traerTodos()
   
    return render_template('cargos/index.html', cargos= cargos)

@app.route('/cargos/crear', methods =['GET', 'POST'])
def crear_cargo():
    if request.method == 'GET':
        #TRAER LAS EMPRESAS PARA HACERLOS SELECCIONABLES AL CREAR UN PRODUCTO
        cargosModel = CargosModel()
        nombreEmpresas = cargosModel.traerEmpresas()
        #mostramos el formulario de creacion
        return render_template('cargos/crear.html', nombreEmpresas = nombreEmpresas)

    nombreEmpresa = request.form.get('empresa')
    nombre = request.form.get('cargo')
    sueldo = request.form.get('sueldo')
      
    cargosModel = CargosModel()
    #Traemos el id de la empresa
    id_empresa_cargo = cargosModel.traerIdEmpresa(nombreEmpresa)
    for e in id_empresa_cargo:
        id_empresa_cargo=e[0]

    cargosModel.crear(id_empresa_cargo, nombre, sueldo)    
    
    #aca es la cracion del producto
    return redirect(url_for('cargos'))

@app.route('/cargos/editar/<int:id>', methods=['GET', 'POST'])
def editar_cargo(id):

    if request.method == 'GET':
        ########TRAER LOS CARGOS PARA HACERLOS SELECCIONABLES AL EDITAR UN PRODUCTO
        cargosModel = CargosModel()
        nombreEmpresas = cargosModel.traerEmpresas()
        empresa = cargosModel.traerEmpresaSeleccionada(id)
        for t in empresa:
            empresa =t[0]
        #
        cargo = cargosModel.traerCargo(id)
        for m in cargo:
            cargo =m[0]
        #nombres
        sueldo = cargosModel.traerSueldo(id)
        for n in sueldo:
            sueldo =n[0]
        #mostramos el formulario de edicion
        return render_template('cargos/editar.html', nombreEmpresas=nombreEmpresas, empresa=empresa, cargo=cargo, sueldo=sueldo)

    nombreEmpresa = request.form.get('empresa')
    nombre = request.form.get('cargo')
    sueldo = request.form.get('sueldo')
      
    cargosModel = CargosModel()
    #Traemos el id de la empresa
    id_empresa_cargo = cargosModel.traerIdEmpresa(nombreEmpresa)
    for e in id_empresa_cargo:
        id_empresa_cargo=e[0]
        
    cargosModel.editar(id, id_empresa_cargo, nombre, sueldo)
    #aca es la creacion del producto
    return redirect(url_for('cargos'))