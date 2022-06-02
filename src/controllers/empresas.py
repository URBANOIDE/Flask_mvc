import marshal
from re import M
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for
from src import app
from src.models.empresas import EmpresasModel

@app.route('/empresas')
def empresas():
    empresasModel = EmpresasModel()
    empresas = empresasModel.traerTodos()
    return render_template('empresas/index.html', empresas=empresas)

@app.route('/empresas/eliminado/<int:id>', methods=['GET', 'POST'])
def eliminar_empresa(id):
    empresasModel = EmpresasModel()
    empresasModel.eliminarCargoEmpresa(id)
    empresasModel.eliminarClienteEmpresa(id)
    empresasModel.eliminarMarcaEmpresa(id)
    empresasModel.eliminar(id)
    empresas = empresasModel.traerTodos()
   
    return render_template('empresas/index.html', empresas= empresas)

@app.route('/empresas/crear', methods =['GET', 'POST'])
def crear_empresa():
    if request.method == 'GET':
        return render_template('empresas/crear.html')

    nombre_empresa = request.form.get('empresa')
    nit_empresa = request.form.get('nit')
    lugar_empresa = request.form.get('nacionalidad')
      
    empresasModel = EmpresasModel()

    empresasModel.crear(nombre_empresa, nit_empresa, lugar_empresa)    
    
    #aca es la cracion del producto
    return redirect(url_for('empresas'))

@app.route('/empresas/editar/<int:id>', methods=['GET', 'POST'])
def editar_empresa(id):

    if request.method == 'GET':
        ########TRAER LOS CARGOS PARA HACERLOS SELECCIONABLES AL EDITAR UN PRODUCTO
        empresasModel = EmpresasModel()
        empresa = empresasModel.traerEmpresa(id)
        for t in empresa:
            empresa =t[0]
            print(empresa)
        #identificacion
        nit = empresasModel.traerNit(id)
        for m in nit:
            nit =m[0]
        #nombres
        nacionalidad = empresasModel.traerNacionalidad(id)
        for n in nacionalidad:
            nacionalidad =n[0]
        #mostramos el formulario de edicion
        return render_template('empresas/editar.html', empresa=empresa, nit=nit, nacionalidad=nacionalidad)

    nombre_empresa = request.form.get('empresa')
    nit_empresa = request.form.get('nit')
    lugar_empresa = request.form.get('nacionalidad')
      
    empresasModel = EmpresasModel()

    empresasModel.editar(id, nombre_empresa, nit_empresa, lugar_empresa)
    #aca es la creacion del producto
    return redirect(url_for('empresas'))