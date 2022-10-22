from select import select
from colorama import Cursor
from src.config.db import DB
#from src.controllers.home import index


class IngresosModel():
    def iniciarAdmin(self, usuario, password):
        cursor = DB.cursor()

        cursor.execute('select * from acceso_admin where usuario = ? and password = ?', (usuario, password,))

        user_exist = cursor.fetchone()

        cursor.close()

        return user_exist

    def iniciarUser(self, usuario, password):
        cursor = DB.cursor()

        cursor.execute('select * from empleados where cedula_empleado = ? and password = ?', (usuario, password))

        user_exist = cursor.fetchone()

        cursor.close()
        

        return user_exist
    def cambiarPassword(self, id, nombre, usuario, password):
        cursor = DB.cursor()

        cursor.execute(""" UPDATE acceso_admin SET usuario = ?, password = ?, nombre = ? WHERE id = ?""",(usuario, password, nombre, id,))
        
        cursor.close()

    def traerCC(self, id_admin):

        cursor = DB.cursor()

        cursor.execute('select usuario from acceso_admin WHERE id = ?', (id_admin,))
        
        user = cursor.fetchall()
        
        cursor.close()

        return user
    def traerPassword(self, id_admin):

        cursor = DB.cursor()

        cursor.execute('select password from acceso_admin WHERE id = ?', (id_admin,))
        
        passwor = cursor.fetchall()
        
        cursor.close()

        return passwor


