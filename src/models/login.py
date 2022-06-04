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
