from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    productosModel = ProductosModel()

    productos = productosModel.traerTodos()

    return render_template('productos/index.html', productos = productos)


@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    #esta funcion me sirve para  mostrar el formulario de creacion
    #Tambien me sirve para crear un nuevo producto
    if request.method == 'GET':
        #mostarmos el formulario de creacion
        return render_template('productos/crear.html')
    
    #aca es la creacion del producto
    nombre = request.form.get('nombre')

    productosModel = ProductosModel()


    productosModel.crear(nombre)
    
    return redirect(url_for('productos'))