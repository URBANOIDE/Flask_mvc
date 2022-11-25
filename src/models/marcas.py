from select import select
from colorama import Cursor
from src.config.db import DB
from src.controllers.home import index


class MarcasModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT id_marca, nombre_empresa, nombre_marca, nacionalidad_marca FROM marcas INNER JOIN empresa ON marcas.id_empresa_marca = empresa.id_empresa ORDER BY id_marca ASC')

        marcas = cursor.fetchall()

        cursor.close()

        return marcas

    def eliminar(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM marcas WHERE id_marca = ?',(id,))

        cursor.close()

    def crear(self, id_empresa_marca, nombre_marca, nacionalidad_marca):
        cursor = DB.cursor()

        cursor.execute('INSERT INTO marcas (id_empresa_marca, nombre_marca, nacionalidad_marca) values(?,?,?)',(id_empresa_marca, nombre_marca, nacionalidad_marca))

        cursor.close()
        
    def editar(self, id, id_empresa_marca, nombre_marca, nacionalidad_marca):
        
        cursor =DB.cursor()

        cursor.execute("""UPDATE marcas SET id_empresa_marca = ?, nombre_marca = ?, nacionalidad_marca = ?  WHERE id_marca = ? """,(id_empresa_marca, nombre_marca, nacionalidad_marca,id,))
        
        cursor.close()

    #Traer nombre de las empresas a mostrar en el formulario de creacion
    def traerEmpresas(self):
        cursor = DB.cursor()

        cursor.execute('SELECT nombre_empresa FROM empresa')

        nombreEmpresas = cursor.fetchall()

        cursor.close()

        return nombreEmpresas

    #Traer id de la marca seleccionada
    def traerIdEmpresa(self, nombreEmpresa):
        cursor = DB.cursor()

        cursor.execute("SELECT id_empresa FROM empresa WHERE nombre_empresa = '"+ nombreEmpresa +"'")

        id_marca_empresa=cursor.fetchall()

        cursor.close()

        return id_marca_empresa

    ###########Edicion
    ##################
    #Requerimientos para editar, traer los datos ingresados para mostrar en el formulario y hacer su edicion
    ##################
    #Empresa
    def traerEmpresaSeleccionada(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombre_empresa FROM marcas INNER JOIN empresa ON marcas.id_empresa_marca = empresa.id_empresa WHERE id_marca  = ?""", (id,))

        empresa = cursor.fetchall()

        cursor.close()

        return empresa
    #identificación
    def traerMarca(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombre_marca FROM marcas WHERE id_marca = ?""", (id,))

        marca = cursor.fetchall()

        cursor.close()

        return marca
    #nombres
    def traerNacionalidad(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT nacionalidad_marca FROM marcas WHERE id_marca = ?""", (id,))

        nacionalidad = cursor.fetchall()

        cursor.close()

        return nacionalidad
   
    
