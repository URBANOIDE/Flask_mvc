import marshal
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for
from src import app
from src.models.clientes import ClientesModel

@app.route('/clientes')
def clientes():
    clientesModel = ClientesModel()
    clientes = clientesModel.traerTodos()
    return render_template('clientes/index.html', clientes=clientes)

@app.route('/clientes/eliminado/<int:id>', methods=['GET', 'POST'])
def eliminar_cliente(id):

    clientesModel = ClientesModel()
    clientesModel.eliminarFacturaCliente(id)
    clientesModel.eliminar(id)
    clientes = clientesModel.traerTodos()
   
    return render_template('clientes/index.html', clientes= clientes)

@app.route('/clientes/crear', methods =['GET', 'POST'])
def crear_cliente():
    if request.method == 'GET':
        #TRAER LAS MARCAS Y PROVEDORES PARA HACERLOS SELECCIONABLES AL CREAR UN PRODUCTO
        clientesModel = ClientesModel()
        nombreEmpresas = clientesModel.traerEmpresas()
        #mostramos el formulario de creacion
        return render_template('clientes/crear.html', nombreEmpresas = nombreEmpresas)

    nombreEmpresa = request.form.get('empresa')
    cedula_cliente = request.form.get('identificacion')
    nombres_cliente = request.form.get('nombres')
    apellidos_cliente = request.form.get('apellidos')
    telefono_cliente = request.form.get('telefono')
    direccion_cliente = request.form.get('direccion')
    sexo_cliente = request.form.get('genero')
      
    clientesModel = ClientesModel()
    #Traemos el id de la empresa
    id_empresa_cliente = clientesModel.traerIdEmpresa(nombreEmpresa)
    for e in id_empresa_cliente:
        id_empresa_cliente=e[0]

    clientesModel.crear(id_empresa_cliente, cedula_cliente, nombres_cliente, apellidos_cliente, telefono_cliente, direccion_cliente, sexo_cliente)    
    
    #aca es la cracion del producto
    return redirect(url_for('clientes'))
@app.route('/cliente/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):

    if request.method == 'GET':
        ########TRAER LAS MARCAS Y PROVEDORES PARA HACERLOS SELECCIONABLES AL EDITAR UN PRODUCTO
        clientesModel = ClientesModel()
        nombreEmpresas = clientesModel.traerEmpresa()
        # Traer los registros de la bd mostrarlos cuando se haga la edicion
        #provedor
        empresa = clientesModel.traerEmpresaSeleccionada(id)
        for t in empresa:
            empresa =t[0]
        #identificacion
        identificacion = clientesModel.traerIdentifacion(id)
        for m in identificacion:
            identificacion =m[0]
        #nombres
        nombres = clientesModel.traerNombres(id)
        for n in nombres:
            nombres =n[0]
        #apellidos
        apellidos = clientesModel.traerApellidos(id)
        for a in apellidos:
            apellidos =a[0]
        #telefono
        telefono = clientesModel.traerTelefono(id)
        for i in telefono:
            telefono =i[0]
        #direccion
        direccion = clientesModel.traerDireccion(id)
        for d in direccion:
            direccion =d[0]
        #genero
        genero = clientesModel.traerGenero(id)
        for g in genero:
            genero =g[0]
        if genero=="F":
            genero="Femenino"
        else:
            genero="Masculino"
        #mostramos el formulario de edicion
        return render_template('clientes/editar.html', nombreEmpresas=nombreEmpresas, empresa=empresa, identificacion=identificacion, genero=genero, nombres=nombres, apellidos=apellidos, telefono=telefono, direccion=direccion)

    nombreEmpresa = request.form.get('empresa')
    cedula_cliente = request.form.get('identificacion')
    nombres_cliente = request.form.get('nombres')
    apellidos_cliente = request.form.get('apellidos')
    telefono_cliente = request.form.get('telefono')
    direccion_cliente = request.form.get('direccion')
    sexo_cliente = request.form.get('genero')
      
    clientesModel = ClientesModel()
    #Traemos el id de la empresa
    id_empresa_cliente = clientesModel.traerIdEmpresa(nombreEmpresa)
    for e in id_empresa_cliente:
        id_empresa_cliente=e[0]
        
    clientesModel.editar(id, id_empresa_cliente, cedula_cliente, nombres_cliente, apellidos_cliente, telefono_cliente, direccion_cliente, sexo_cliente)
    
    #aca es la creacion del producto
    return redirect(url_for('clientes'))