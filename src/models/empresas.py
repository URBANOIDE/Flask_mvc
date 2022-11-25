from select import select
from colorama import Cursor
from src.config.db import DB
from src.controllers.home import index


class EmpresasModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT * FROM empresa')

        empresas = cursor.fetchall()

        cursor.close()

        return empresas

    def eliminar(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM empresa WHERE id_empresa = ?',(id,))

        cursor.close()

    def crear(self, nombre_empresa, nit_empresa, lugar_empresa):
        cursor = DB.cursor()

        cursor.execute('INSERT INTO empresa (nombre_empresa, nit_empresa, lugar_empresa) values(?,?,?)',(nombre_empresa, nit_empresa, lugar_empresa))

        cursor.close()
        
    def editar(self, id, nombre_empresa, nit_empresa, lugar_empresa):
        
        cursor =DB.cursor()

        cursor.execute("""UPDATE empresa SET nombre_empresa = ?, nit_empresa = ?, lugar_empresa = ?  WHERE id_empresa = ? """,(nombre_empresa, nit_empresa, lugar_empresa,id,))
        
        cursor.close()
        
    ###########Edicion
    ##################
    #Requerimientos para editar, traer los datos ingresados para mostrar en el formulario y hacer su edicion
    ##################
    #Empresa
    def traerEmpresa(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombre_empresa FROM empresa WHERE id_empresa  = ?""", (id,))

        empresa = cursor.fetchall()

        cursor.close()

        return empresa
    #Nit
    def traerNit(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nit_empresa FROM empresa WHERE id_empresa = ?""", (id,))

        nit = cursor.fetchall()

        cursor.close()

        return nit
    #nombres
    def traerNacionalidad(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT lugar_empresa FROM empresa WHERE id_empresa = ?""", (id,))

        nacionalidad = cursor.fetchall()

        cursor.close()

        return nacionalidad
   
    
