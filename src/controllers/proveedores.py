from flask import render_template, request, redirect, url_for, session
from src import app
from src.models.proveedores import ProveedoresModel

@app.route('/proveedores')
def proveedores():
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
        
    proveedoresModel =ProveedoresModel()

    proveedores = proveedoresModel.traerTodos()
   
    return render_template('proveedores/index.html', proveedores = proveedores)

@app.route('/proveedor/crear', methods =['GET', 'POST'])
def crear_proveedor():
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

    #esta funcion me sirve para mostrar el formulario de creacion
    #y tambien me sirve para crear un nuevo producto
    #estos pasos se identifican con los metodos 
    if request.method == 'GET':
        #Traer nombre de la empresa
        proveedoresModel = ProveedoresModel()
        nombreEmpresas = proveedoresModel.traerEmpresa()
        #mostramos el formulario de creacion
        return render_template('proveedores/crear.html', nombreEmpresas=nombreEmpresas)

    nombreEmpresa = request.form.get('empresa')
    cedula = request.form.get('identificacion')
    nombres_provedor = request.form.get('nombres')
    apellidos_provedor = request.form.get('apellidos')
    telefono_provedor = request.form.get('telefono')
    direccion_provedor = request.form.get('direccion')
    sexo_provedor = request.form.get('genero')
      
    proveedoresModel = ProveedoresModel()
    #Traemos el id de la empresa
    id_empresa = proveedoresModel.traerIdEmpresa(nombreEmpresa)
    for i in id_empresa:
        id_empresa=i[0]

    proveedoresModel.crear(id_empresa, cedula, nombres_provedor, apellidos_provedor, telefono_provedor, direccion_provedor, sexo_provedor)    
    
    #aca es la cracion del producto
    return redirect(url_for('proveedores'))
###########################################################################
@app.route('/proveedor/editar/<int:id>', methods=['GET', 'POST'])
def editar_proveedor(id):
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
        ########TRAER LAS MARCAS Y PROVEDORES PARA HACERLOS SELECCIONABLES AL EDITAR UN PRODUCTO
        proveedoresModel = ProveedoresModel()
        nombreEmpresas = proveedoresModel.traerEmpresa()
        # Traer los registros de la bd mostrarlos cuando se haga la edicion
        #provedor
        empresa = proveedoresModel.traerEmpresaSeleccionada(id)
        for t in empresa:
            empresa =t[0]
        #identificacion
        identificacion = proveedoresModel.traerIdentifacion(id)
        for m in identificacion:
            identificacion =m[0]
        #nombres
        nombres = proveedoresModel.traerNombres(id)
        for n in nombres:
            nombres =n[0]
        #apellidos
        apellidos = proveedoresModel.traerApellidos(id)
        for a in apellidos:
            apellidos =a[0]
        #telefono
        telefono = proveedoresModel.traerTelefono(id)
        for i in telefono:
            telefono =i[0]
        #direccion
        direccion = proveedoresModel.traerDireccion(id)
        for d in direccion:
            direccion =d[0]
        #genero
        genero = proveedoresModel.traerGenero(id)
        for g in genero:
            genero =g[0]
        if genero=="F":
            genero="Femenino"
        else:
            genero="Masculino"
        
        #mostramos el formulario de edicion
        return render_template('proveedores/editar.html', nombreEmpresas=nombreEmpresas, empresa=empresa, identificacion=identificacion, genero=genero, nombres=nombres, apellidos=apellidos, telefono=telefono, direccion=direccion)

    nombreEmpresa = request.form.get('empresa')
    cedula = request.form.get('identificacion')
    nombres_provedor = request.form.get('nombres')
    apellidos_provedor = request.form.get('apellidos')
    telefono_provedor = request.form.get('telefono')
    direccion_provedor = request.form.get('direccion')
    sexo_provedor = request.form.get('genero')
      
    proveedoresModel = ProveedoresModel()
    #Traemos el id de la empresa
    id_empresa = proveedoresModel.traerIdEmpresa(nombreEmpresa)
    for i in id_empresa:
        id_empresa=i[0]
        
    proveedoresModel.editar(id, id_empresa, cedula, nombres_provedor, apellidos_provedor, telefono_provedor, direccion_provedor, sexo_provedor)
    
    #aca es la creacion del producto
    return redirect(url_for('proveedores'))

@app.route('/provedor/eliminado/<int:id>', methods=['GET', 'POST'])
def eliminar_proveedor(id):
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
        
    proveedoresModel = ProveedoresModel()
    proveedoresModel.eliminar(id)
    proveedores = proveedoresModel.traerTodos()
   
    return render_template('proveedores/index.html', proveedores = proveedores)