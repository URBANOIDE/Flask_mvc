import marshal
from re import M
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for, session
from src import app
from src.models.marcas import MarcasModel

@app.route('/marcas')
def marcas():
    #verificacion de si se ha iniciado sesion, para que no puedan acceder a la ruta sin haberse logueado
    if session == {}:
        return render_template('login/login.html')

    marcasModel = MarcasModel()
    marcas = marcasModel.traerTodos()
    return render_template('marcas/index.html', marcas=marcas)

@app.route('/marcas/eliminado/<int:id>', methods=['GET', 'POST'])
def eliminar_marca(id):
    #verificacion de si se ha iniciado sesion, para que no puedan acceder a la ruta sin haberse logueado
    if session == {}:
        return render_template('login/login.html')

    marcasModel = MarcasModel()
    marcasModel.eliminar(id)
    marcas = marcasModel.traerTodos()
   
    return render_template('marcas/index.html', marcas= marcas)

@app.route('/marcas/crear', methods =['GET', 'POST'])
def crear_marca():
    #verificacion de si se ha iniciado sesion, para que no puedan acceder a la ruta sin haberse logueado
    if session == {}:
        return render_template('login/login.html')

    if request.method == 'GET':
        #TRAER LOS CARGOS PARA HACERLOS SELECCIONABLES AL CREAR UN PRODUCTO
        marcasModel = MarcasModel()
        nombreEmpresas = marcasModel.traerEmpresas()
        #mostramos el formulario de creacion
        return render_template('marcas/crear.html', nombreEmpresas = nombreEmpresas)

    nombreEmpresa = request.form.get('empresa')
    nombre_marca = request.form.get('marca')
    nacionalidad_marca = request.form.get('nacionalidad')
      
    marcasModel = MarcasModel()
    #Traemos el id de la empresa
    id_empresa_marca = marcasModel.traerIdEmpresa(nombreEmpresa)
    for e in id_empresa_marca:
        id_empresa_marca=e[0]

    marcasModel.crear(id_empresa_marca, nombre_marca, nacionalidad_marca)    
    
    #aca es la cracion del producto
    return redirect(url_for('marcas'))

@app.route('/marcas/editar/<int:id>', methods=['GET', 'POST'])
def editar_marca(id):
    #verificacion de si se ha iniciado sesion, para que no puedan acceder a la ruta sin haberse logueado
    if session == {}:
        return render_template('login/login.html')
        
    if request.method == 'GET':
        ########TRAER LOS CARGOS PARA HACERLOS SELECCIONABLES AL EDITAR UN PRODUCTO
        marcasModel = MarcasModel()
        nombreEmpresas = marcasModel.traerEmpresas()
        empresa = marcasModel.traerEmpresaSeleccionada(id)
        for t in empresa:
            empresa =t[0]
        #identificacion
        marcas = marcasModel.traerMarca(id)
        for m in marcas:
            marcas =m[0]
        #nombres
        nacionalidad = marcasModel.traerNacionalidad(id)
        for n in nacionalidad:
            nacionalidad =n[0]
        #mostramos el formulario de edicion
        return render_template('marcas/editar.html', nombreEmpresas=nombreEmpresas, empresa=empresa, marcas=marcas, nacionalidad=nacionalidad)

    nombreEmpresa = request.form.get('empresa')
    nombre_marca = request.form.get('marca')
    nacionalidad_marca = request.form.get('nacionalidad')
      
    marcasModel = MarcasModel()
    #Traemos el id de la empresa
    id_empresa_marca = marcasModel.traerIdEmpresa(nombreEmpresa)
    for e in id_empresa_marca:
        id_empresa_marca=e[0]

    marcasModel.editar(id, id_empresa_marca, nombre_marca, nacionalidad_marca)
    #aca es la creacion del producto
    return redirect(url_for('marcas'))