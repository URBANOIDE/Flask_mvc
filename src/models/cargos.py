from select import select
from colorama import Cursor
from src.config.db import DB
from src.controllers.home import index


class CargosModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT id_cargo, nombre_empresa, nombre, sueldo FROM cargo INNER JOIN empresa ON cargo.id_empresa_cargo = empresa.id_empresa ORDER BY id_cargo ASC')

        cargos = cursor.fetchall()

        cursor.close()

        return cargos

    def eliminar(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM cargo WHERE id_cargo = ?',(id,))

        cursor.close()

    def crear(self, id_empresa_cargo, nombre, sueldo):
        cursor = DB.cursor()

        cursor.execute('INSERT INTO cargo (id_empresa_cargo, nombre, sueldo) values(?,?,?)',(id_empresa_cargo, nombre, sueldo))

        cursor.close()
        
    def editar(self, id, id_empresa_cargo, nombre, sueldo):
        
        cursor =DB.cursor()

        cursor.execute("""UPDATE cargo SET id_empresa_cargo = ?, nombre = ?, sueldo = ?  WHERE id_cargo = ? """,(id_empresa_cargo, nombre, sueldo,id,))
        
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

    #al borrar una marca tambien se eliminará su producto
    def eliminarEmpleadoCargo(self, id):
        cursor = DB.cursor()

        cursor.execute("""DELETE FROM empleados WHERE id_cargo_empleado = ?""", (id,))

        cursor.close()
    ###########Edicion
    ##################
    #Requerimientos para editar, traer los datos ingresados para mostrar en el formulario y hacer su edicion
    ##################
    #Empresa
    def traerEmpresaSeleccionada(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombre_empresa FROM cargo INNER JOIN empresa ON cargo.id_empresa_cargo = empresa.id_empresa WHERE id_cargo  = ?""", (id,))

        empresa = cursor.fetchall()

        cursor.close()

        return empresa
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
   
    
