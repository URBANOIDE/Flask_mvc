from select import select
from colorama import Cursor
from src.config.db import DB
from src.controllers.home import index


class ClientesModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT id_cliente, nombre_empresa, cedula_cliente, nombres_cliente, apellidos_cliente, telefono_cliente, direccion_cliente, sexo_cliente FROM clientes INNER JOIN empresa ON clientes.id_empresa_cliente = empresa.id_empresa ORDER BY id_cliente ASC')

        clientes = cursor.fetchall()

        cursor.close()

        return clientes

    def eliminar(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM clientes WHERE id_cliente = ?',(id,))

        cursor.close()

    def crear(self, id_empresa_cliente, cedula_cliente, nombres_cliente, apellidos_cliente, telefono_cliente, direccion_cliente, sexo_cliente):
        cursor = DB.cursor()

        cursor.execute('INSERT INTO clientes (id_empresa_cliente, cedula_cliente, nombres_cliente, apellidos_cliente, telefono_cliente, direccion_cliente, sexo_cliente) values(?,?,?,?,?,?,?)',(id_empresa_cliente, cedula_cliente, nombres_cliente, apellidos_cliente, telefono_cliente, direccion_cliente, sexo_cliente))

        cursor.close()
        
    def editar(self, id, id_empresa_cliente, cedula_cliente, nombres_cliente, apellidos_cliente, telefono_cliente, direccion_cliente, sexo_cliente):
        
        cursor =DB.cursor()

        cursor.execute("""UPDATE clientes SET id_empresa_cliente = ?, cedula_cliente = ?, nombres_cliente = ?, apellidos_cliente = ?, telefono_cliente = ?, direccion_cliente = ?, sexo_cliente = ?  WHERE id_cliente = ? """,(id_empresa_cliente, cedula_cliente, nombres_cliente, apellidos_cliente, telefono_cliente, direccion_cliente, sexo_cliente,id,))
        
        cursor.close()

    #Traer nombre de las empresas a mostrar en el formulario de creacion
    def traerEmpresas(self):
        cursor = DB.cursor()

        cursor.execute('SELECT nombre_empresa FROM empresa')

        nombreEmpresas = cursor.fetchall()

        cursor.close()

        return nombreEmpresas

    #Traer id de empresa seleccionada
    def traerIdEmpresa(self, nombreEmpresa):
        cursor = DB.cursor()

        cursor.execute("SELECT id_empresa FROM empresa WHERE nombre_empresa = '"+ nombreEmpresa +"'")

        id_empresa_cliente=cursor.fetchall()

        cursor.close()

        return id_empresa_cliente
        
    ###########Edicion
    #Requisitos para formulario de edicion de provedor
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

        cursor.execute("""SELECT nombre_empresa FROM clientes INNER JOIN empresa ON clientes.id_empresa_cliente = empresa.id_empresa WHERE id_cliente = ?""", (id,))

        empresa = cursor.fetchall()

        cursor.close()

        return empresa
    #identificación
    def traerIdentifacion(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT cedula_cliente FROM clientes WHERE id_cliente = ?""", (id,))

        identificacion = cursor.fetchall()

        cursor.close()

        return identificacion
    #nombres
    def traerNombres(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT nombres_cliente FROM clientes WHERE id_cliente = ?""", (id,))

        nombres = cursor.fetchall()

        cursor.close()

        return nombres
    #apellidos
    def traerApellidos(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT apellidos_cliente FROM clientes WHERE id_cliente = ?""", (id,))

        apellidos = cursor.fetchall()

        cursor.close()

        return apellidos
    #telefono
    def traerTelefono(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT telefono_cliente FROM clientes WHERE id_cliente = ?""", (id,))

        telefono = cursor.fetchall()

        cursor.close()

        return telefono
    #direccion
    def traerDireccion(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT direccion_cliente FROM clientes WHERE id_cliente = ?""", (id,))

        direccion = cursor.fetchall()

        cursor.close()

        return direccion
    #genero
    def traerGenero(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT sexo_cliente FROM clientes WHERE id_cliente = ?""", (id,))

        genero = cursor.fetchall()

        cursor.close()

        return genero
