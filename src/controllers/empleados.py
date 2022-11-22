import marshal
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for, session
from src import app
from src.models.empleados import EmpleadosModel

@app.route('/empleados')
def empleados():
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

    empleadosModel = EmpleadosModel()
    empleados = empleadosModel.traerTodos()
    return render_template('empleados/index.html', empleados=empleados)

@app.route('/empleados/eliminado/<int:id>', methods=['GET', 'POST'])
def eliminar_empleado(id):
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

    empleadosModel = EmpleadosModel()
    empleadosModel.eliminarFacturaEmpleado(id)
    empleadosModel.eliminar(id)
    empleados = empleadosModel.traerTodos()
   
    return render_template('empleados/index.html', empleados= empleados)

@app.route('/empleados/crear', methods =['GET', 'POST'])
def crear_empleado():
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
        #TRAER LAS MARCAS Y PROVEDORES PARA HACERLOS SELECCIONABLES AL CREAR UN PRODUCTO
        empleadosModel = EmpleadosModel()
        nombreCargos = empleadosModel.traerCargos()
        #mostramos el formulario de creacion
        return render_template('empleados/crear.html', nombreCargos = nombreCargos)

    nombreCargo = request.form.get('cargo')
    cedula_empleado = request.form.get('identificacion')
    nombres_empleado = request.form.get('nombres')
    apellidos_empleado = request.form.get('apellidos')
    telefono_empleado = request.form.get('telefono')
    direccion_empleado = request.form.get('direccion')
    sexo_empleado = request.form.get('genero')
    password = request.form.get('password')
      
    empleadosModel = EmpleadosModel()
    #Traemos el id del cargo
    id_cargo_empleado = empleadosModel.traerIdCargo(nombreCargo)
    for e in id_cargo_empleado:
        id_cargo_empleado=e[0]

    empleadosModel.crear(id_cargo_empleado, cedula_empleado, nombres_empleado, apellidos_empleado, telefono_empleado, direccion_empleado, sexo_empleado, password)    
    
    #aca es la cracion del producto
    return redirect(url_for('empleados'))

@app.route('/empleados/editar/<int:id>', methods=['GET', 'POST'])
def editar_empleado(id):
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
        empleadosModel = EmpleadosModel()
        nombreCargos = empleadosModel.traerCargos()
        # Traer los registros de la bd mostrarlos cuando se haga la edicion
        #provedor
        cargo = empleadosModel.traerCargoSeleccionado(id)
        for t in cargo:
            cargo =t[0]
        #identificacion
        identificacion = empleadosModel.traerIdentifacion(id)
        for m in identificacion:
            identificacion =m[0]
        #nombres
        nombres = empleadosModel.traerNombres(id)
        for n in nombres:
            nombres =n[0]
        #apellidos
        apellidos = empleadosModel.traerApellidos(id)
        for a in apellidos:
            apellidos =a[0]
        #telefono
        telefono = empleadosModel.traerTelefono(id)
        for i in telefono:
            telefono =i[0]
        #direccion
        direccion = empleadosModel.traerDireccion(id)
        for d in direccion:
            direccion =d[0]
        #genero
        genero = empleadosModel.traerGenero(id)
        for g in genero:
            genero =g[0]
        if genero=="F":
            genero="Femenino"
        else:
            genero="Masculino"
        #password
        password = empleadosModel.traerPassword(id)
        for p in password:
            password = p[0]
        #mostramos el formulario de edicion
        return render_template('empleados/editar.html', nombreCargos=nombreCargos, cargo=cargo, identificacion=identificacion, genero=genero, nombres=nombres, apellidos=apellidos, telefono=telefono, direccion=direccion, password=password)

    nombreCargo = request.form.get('cargo')
    cedula_empleado = request.form.get('identificacion')
    nombres_empleado = request.form.get('nombres')
    apellidos_empleado = request.form.get('apellidos')
    telefono_empleado = request.form.get('telefono')
    direccion_empleado = request.form.get('direccion')
    sexo_empleado = request.form.get('genero')
    password = request.form.get('password')
      
    empleadosModel = EmpleadosModel()
    #Traemos el id del cargo
    id_cargo_empleado = empleadosModel.traerIdCargo(nombreCargo)
    for e in id_cargo_empleado:
        id_cargo_empleado=e[0]
        
    empleadosModel.editar(id, id_cargo_empleado, cedula_empleado, nombres_empleado, apellidos_empleado, telefono_empleado, direccion_empleado, sexo_empleado, password)
    
    #aca es la creacion del producto
    return redirect(url_for('empleados'))