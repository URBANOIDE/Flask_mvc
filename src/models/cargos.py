from select import select
from colorama import Cursor
from src.config.db import DB
from src.controllers.home import index


class CargosModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT * FROM cargo ORDER BY id_cargo ASC')

        cargos = cursor.fetchall()

        cursor.close()

        return cargos

    def eliminar(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM cargo WHERE id_cargo = ?',(id,))

        cursor.close()

    def crear(self, nombre, sueldo):
        cursor = DB.cursor()

        cursor.execute('INSERT INTO cargo (nombre, sueldo) values(?,?)',(nombre, sueldo))

        cursor.close()
        
    def editar(self, id, nombre, sueldo):
        
        cursor =DB.cursor()

        cursor.execute("""UPDATE cargo SET nombre = ?, sueldo = ?  WHERE id_cargo = ? """,(nombre, sueldo,id,))
        
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
    
    #Cargo
    def traerCargo(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombre FROM cargo WHERE id_cargo = ?""", (id,))

        cargo = cursor.fetchall()

        cursor.close()

        return cargo
    #Salario
    def traerSueldo(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT sueldo FROM cargo WHERE id_cargo = ?""", (id,))

        nacionalidad = cursor.fetchall()

        cursor.close()

        return nacionalidad
   
    
