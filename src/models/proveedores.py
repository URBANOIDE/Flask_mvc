from colorama import Cursor
from src.config.db import DB
from src.controllers.home import index


class ProveedoresModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT id_provedor, nombre_empresa, cedula_provedor, nombres_provedor, apellidos_provedor, telefono_provedor, direccion_provedor, sexo_provedor  FROM provedores INNER JOIN empresa ON provedores.id_empresa_provedor = empresa.id_empresa ORDER BY id_provedor ASC')

        proveedores = cursor.fetchall()

        cursor.close()

        return proveedores

    def crear(self, id_empresa, cedula, nombres_provedor, apellidos_provedor, telefono_provedor, direccion_provedor, sexo_provedor):
        cursor = DB.cursor()

        cursor.execute('insert into provedores(id_empresa_provedor, cedula_provedor, nombres_provedor, apellidos_provedor, telefono_provedor, direccion_provedor, sexo_provedor) values(?,?,?,?,?,?,?)', (id_empresa, cedula, nombres_provedor, apellidos_provedor, telefono_provedor, direccion_provedor, sexo_provedor))
        
        cursor.close()

    def eliminar(self, id):
        cursor = DB.cursor()

        cursor.execute(""" DELETE FROM provedores where id_provedor = ? """,(id,))
        
        cursor.close()

    def editar(self, id, id_empresa, cedula, nombres_provedor, apellidos_provedor, telefono_provedor, direccion_provedor, sexo_provedor):
        
        cursor =DB.cursor()

        cursor.execute(""" UPDATE provedores SET id_empresa_provedor = ?, cedula_provedor = ?, nombres_provedor = ?, apellidos_provedor = ?, telefono_provedor = ?, direccion_provedor = ?, sexo_provedor = ?  WHERE id_provedor = ? """,(id_empresa, cedula, nombres_provedor, apellidos_provedor, telefono_provedor, direccion_provedor, sexo_provedor, id,))
        
        cursor.close()
        
    #Requisitos para formulario de creacion de provedor
    #Traer empresa para mostrar como seleccionable
    def traerEmpresa(self):
        cursor = DB.cursor()

        cursor.execute('select nombre_empresa from empresa')

        nombreEmpresa = cursor.fetchall()

        cursor.close()

        return nombreEmpresa
    ######## Traemos en id de la empresa que se seleccionó
    def traerIdEmpresa(self, nombreEmpresa):
       
        cursor = DB.cursor()

        cursor.execute("select id_empresa from empresa where nombre_empresa = '"+ nombreEmpresa +"'")

        id_empresa = cursor.fetchall()

        cursor.close()

        return id_empresa
    ##################
    #Requerimientos para editar, traer los datos ingresados para mostrar en el formulario y hacer su edicion
    ##################
    #Empresa
    def traerEmpresaSeleccionada(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombre_empresa FROM provedores INNER JOIN empresa ON provedores.id_empresa_provedor = empresa.id_empresa WHERE id_provedor = ?""", (id,))

        empresa = cursor.fetchall()

        cursor.close()

        return empresa
    #identificación
    def traerIdentifacion(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT cedula_provedor FROM provedores WHERE id_provedor = ?""", (id,))

        identificacion = cursor.fetchall()

        cursor.close()

        return identificacion
    #nombres
    def traerNombres(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT nombres_provedor FROM provedores WHERE id_provedor = ?""", (id,))

        nombres = cursor.fetchall()

        cursor.close()

        return nombres
    #apellidos
    def traerApellidos(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT apellidos_provedor FROM provedores WHERE id_provedor = ?""", (id,))

        apellidos = cursor.fetchall()

        cursor.close()

        return apellidos
    #telefono
    def traerTelefono(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT telefono_provedor FROM provedores WHERE id_provedor = ?""", (id,))

        telefono = cursor.fetchall()

        cursor.close()

        return telefono
    #direccion
    def traerDireccion(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT direccion_provedor FROM provedores WHERE id_provedor = ?""", (id,))

        direccion = cursor.fetchall()

        cursor.close()

        return direccion
    #genero
    def traerGenero(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT sexo_provedor FROM provedores WHERE id_provedor = ?""", (id,))

        genero = cursor.fetchall()

        cursor.close()

        return genero