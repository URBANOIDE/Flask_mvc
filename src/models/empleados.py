from select import select
from colorama import Cursor
from src.config.db import DB
from src.controllers.home import index


class EmpleadosModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('SELECT id_empleado, nombre, cedula_empleado, nombres_empleado, apellidos_empleado, telefono_empleado, direccion_empleado, sexo_empleado FROM empleados INNER JOIN cargo ON empleados.id_cargo_empleado = cargo.id_cargo ORDER BY id_empleado ASC')

        empleados = cursor.fetchall()

        cursor.close()

        return empleados

    def eliminar(self, id):
        cursor = DB.cursor()

        cursor.execute('DELETE FROM empleados WHERE id_empleado = ?',(id,))

        cursor.close()

    def crear(self, id_cargo_empleado, cedula_empleado, nombres_empleado, apellidos_empleado, telefono_empleado, direccion_empleado, sexo_empleado):
        cursor = DB.cursor()

        cursor.execute('INSERT INTO empleados (id_cargo_empleado, cedula_empleado, nombres_empleado, apellidos_empleado, telefono_empleado, direccion_empleado, sexo_empleado) values(?,?,?,?,?,?,?)',(id_cargo_empleado, cedula_empleado, nombres_empleado, apellidos_empleado, telefono_empleado, direccion_empleado, sexo_empleado))

        cursor.close()
        
    def editar(self, id, id_cargo_empleado, cedula_empleado, nombres_empleado, apellidos_empleado, telefono_empleado, direccion_empleado, sexo_empleado):
        
        cursor =DB.cursor()

        cursor.execute("""UPDATE empleados SET id_cargo_empleado = ?, cedula_empleado =?, nombres_empleado = ?, apellidos_empleado = ?, telefono_empleado = ?, direccion_empleado = ?, sexo_empleado = ?  WHERE id_empleado = ? """,(id_cargo_empleado, cedula_empleado, nombres_empleado, apellidos_empleado, telefono_empleado, direccion_empleado, sexo_empleado,id,))
        
        cursor.close()

    #Traer nombre de las empresas a mostrar en el formulario de creacion
    def traerEmpresas(self):
        cursor = DB.cursor()

        cursor.execute('SELECT nombre_empresa FROM empresa')

        nombreEmpresas = cursor.fetchall()

        cursor.close()

        return nombreEmpresas

    #Traer id del cargo seleccionada
    def traerIdCargo(self, nombreCargo):
        cursor = DB.cursor()

        cursor.execute("SELECT id_cargo FROM cargo WHERE nombre = '"+ nombreCargo +"'")

        id_cargo_empleado=cursor.fetchall()

        cursor.close()

        return id_cargo_empleado
    #al borrar un cliente tambien se eliminará su registro de factura
    def eliminarFacturaEmpleado(self, id):
        cursor = DB.cursor()

        cursor.execute("""DELETE FROM factura WHERE id_empleado_factura = ?""", (id,))

        cursor.close()
    ###########Edicion
    #Requisitos para formulario de edicion de provedor
    #Traer los cargos para mostrar como seleccionable
    def traerCargos(self):
        cursor = DB.cursor()

        cursor.execute('select nombre from cargo')

        nombreCargos = cursor.fetchall()

        cursor.close()

        return nombreCargos
    ######## Traemos en id de la empresa que se seleccionó
    def traerIdCargo(self, nombreCargo):
       
        cursor = DB.cursor()

        cursor.execute("select id_cargo from cargo where nombre = '"+ nombreCargo +"'")

        id_empresa = cursor.fetchall()

        cursor.close()

        return id_empresa
    ##################
    #Requerimientos para editar, traer los datos ingresados para mostrar en el formulario y hacer su edicion
    ##################
    #Empresa
    def traerCargoSeleccionado(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT nombre FROM empleados INNER JOIN cargo ON empleados.id_cargo_empleado = cargo.id_cargo WHERE id_empleado = ?""", (id,))

        cargo = cursor.fetchall()

        cursor.close()

        return cargo
    #identificación
    def traerIdentifacion(self, id):
        
        cursor = DB.cursor()

        cursor.execute("""SELECT cedula_empleado FROM empleados WHERE id_empleado = ?""", (id,))

        identificacion = cursor.fetchall()

        cursor.close()

        return identificacion
    #nombres
    def traerNombres(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT nombres_empleado FROM empleados WHERE id_empleado = ?""", (id,))

        nombres = cursor.fetchall()

        cursor.close()

        return nombres
    #apellidos
    def traerApellidos(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT apellidos_empleado FROM empleados WHERE id_empleado = ?""", (id,))

        apellidos = cursor.fetchall()

        cursor.close()

        return apellidos
    #telefono
    def traerTelefono(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT telefono_empleado FROM empleados WHERE id_empleado = ?""", (id,))

        telefono = cursor.fetchall()

        cursor.close()

        return telefono
    #direccion
    def traerDireccion(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT direccion_empleado FROM empleados WHERE id_empleado = ?""", (id,))

        direccion = cursor.fetchall()

        cursor.close()

        return direccion
    #genero
    def traerGenero(self, id):
        cursor = DB.cursor()

        cursor.execute("""SELECT sexo_empleado FROM empleados WHERE id_empleado = ?""", (id,))

        genero = cursor.fetchall()

        cursor.close()

        return genero
