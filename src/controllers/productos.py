from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    productosModel =ProductosModel()

    productos = productosModel.traerTodos()
   
    return render_template('productos/index.html', productos = productos)

@app.route('/productos/crear', methods =['GET', 'POST'])
def crear_producto():
   #esta funcion me sirve para mostrar el formulario de creacion
   #y tambien me sirve para crear un nuevo producto
   #estos pasos se identifican con los metodos 
    if request.method == 'GET':
       #mostramos el formulario de cracion
        return render_template('productos/crear.html')

    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_compra = request.form.get('precio_compra')
    precio_venta = request.form.get('precio_venta')
    ganancia = request.form.get('ganancia')
    estado = request.form.get('estado')
    
    if estado == '1':
        estado = 'Activo'
    else:
        estado = 'Inactivo'
      
    productosModel = ProductosModel() 

    productosModel.crear(nombre,descripcion,precio_compra,precio_venta,ganancia,estado)
    

    #aca es la cracion del producto
    return redirect(url_for('productos'))
###########################################################################
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):

    if request.method == 'GET':
       #mostramos el formulario de cracion
        return render_template('productos/editar.html')

    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_compra = request.form.get('precio_compra')
    precio_venta = request.form.get('precio_venta')
    ganancia = request.form.get('ganancia')
    estado = request.form.get('estado')
    
    if estado == '1':
        estado = 'Activo'
    else:
        estado = 'Inactivo'
      
    productosModel = ProductosModel()
    productosModel.editar(id,nombre,descripcion,precio_compra,precio_venta,ganancia,estado)

    

    #aca es la cracion del producto
    return redirect(url_for('productos'))