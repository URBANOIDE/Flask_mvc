from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    productosModel = ProductosModel()
    productos = productosModel.traerTodos()

    print(productos)

    return 'productos'