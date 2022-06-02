import marshal
from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    productosModel =ProductosModel()

    productos = productosModel.traerTodos()
   
    return render_template('productos/index.html', productos = productos)


@app.route('/productos/eliminado/<int:id>', methods=['GET', 'POST'])
def eliminar_producto(id):
    productosModel =ProductosModel()

    productosModel.eliminarFacturaProducto(id)
    productosModel.eliminar(id)
    productos = productosModel.traerTodos()
   
    return render_template('productos/index.html', productos = productos)

@app.route('/productos/crear', methods =['GET', 'POST'])
def crear_producto():
   #esta funcion me sirve para mostrar el formulario de creacion
   #y tambien me sirve para crear un nuevo producto
   #estos pasos se identifican con los metodos 
    if request.method == 'GET':
        ########TRAER LAS MARCAS Y PROVEDORES PARA HACERLOS SELECCIONABLES AL CREAR UN PRODUCTO
        productosModel = ProductosModel()
        nombreMarcas = productosModel.traerMarcas()
        nombreProveedores = productosModel.traerProveedores()
        #mostramos el formulario de creacion
        return render_template('productos/crear.html', nombreMarcas = nombreMarcas, nombreProveedores = nombreProveedores)

    nombreProvedor = request.form.get('provedor')
    nombreMarca = request.form.get('marca')
    nombres_producto = request.form.get('producto')
    precio_compra = request.form.get('precio_compra')
    precio_venta = request.form.get('precio_venta')
    ganancia = request.form.get('ganancia')
          
    productosModel = ProductosModel()
    #######TRAER EL ID DEL PROVEDOR PARA INSERTARLO EN LA TABLA PRODUCTOS
    id_provedor = productosModel.traerIdProvedor(nombreProvedor)
    for i in id_provedor:
        id_provedor_producto=i[0]
    #######TRAER EL ID DE LA MARCA PARA INSERTARLO EN LA TABLA PRODUCTOS
    id_marca = productosModel.traerIdMarca(nombreMarca)
    for r in id_marca:
        id_marca_producto=r[0]
        
    productosModel.crear(id_provedor_producto,id_marca_producto,nombres_producto,precio_compra,precio_venta,ganancia)
    

    #### Una vez creado el producto, nos redirecciona a la pagina productos
    return redirect(url_for('productos'))
###########################################################################
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):

    if request.method == 'GET':
        ########TRAER LAS MARCAS Y PROVEDORES PARA HACERLOS SELECCIONABLES AL EDITAR UN PRODUCTO
        productosModel = ProductosModel()
        nombreMarcas = productosModel.traerMarcas()
        nombreProveedores = productosModel.traerProveedores()
        # Traer los registros de la bd mostrarlos cuando se haga la edicion
        #provedor
        provedor = productosModel.traerProvedor(id)
        for t in provedor:
            provedor =t[0]
        #marca
        marca = productosModel.traerMarca(id)
        for p in marca:
            marca =p[0]
        #producto
        producto = productosModel.traerProducto(id)
        for s in producto:
            producto =s[0]
        #precio_compra
        precio_compra = productosModel.traerPrecio_compra(id)
        for w in precio_compra:
            precio_compra =w[0]
        #precio_venta
        precio_venta = productosModel.traerPrecio_venta(id)
        for z in precio_venta:
            precio_venta =z[0]
        #ganancia
        ganancia = productosModel.traerGanancia(id)
        for d in ganancia:
            ganancia =d[0]
        #mostramos el formulario de edicion
        return render_template('productos/editar.html', nombreMarcas=nombreMarcas, nombreProveedores=nombreProveedores, marca=marca, provedor=provedor, producto=producto, precio_compra=precio_compra, precio_venta=precio_venta, ganancia=ganancia)

    nombreProvedor = request.form.get('provedor')
    nombreMarca = request.form.get('marca')
    nombres_producto = request.form.get('producto')
    precio_compra = request.form.get('precio_compra')
    precio_venta = request.form.get('precio_venta')
    ganancia = request.form.get('ganancia')
    
    productosModel = ProductosModel()
    #######TRAER EL ID DEL PROVEDOR PARA INSERTARLO EN LA TABLA PRODUCTOS
    id_provedor = productosModel.traerIdProvedor(nombreProvedor)
    for i in id_provedor:
        id_provedor_producto=i[0]
    #######TRAER EL ID DE LA MARCA PARA INSERTARLO EN LA TABLA PRODUCTOS
    id_marca = productosModel.traerIdMarca(nombreMarca)
    for r in id_marca:
        id_marca_producto=r[0]
        
    productosModel.editar(id,id_provedor_producto,id_marca_producto,nombres_producto,precio_compra,precio_venta,ganancia)

    

    #aca es la cracion del producto
    return redirect(url_for('productos'))