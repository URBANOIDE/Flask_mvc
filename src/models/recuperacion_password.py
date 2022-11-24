from src.config.db import DB
from src.controllers.home import index


class RecuperacionModel():
    def traerEmail(self, email):
        cursor = DB.cursor()

        cursor.execute("SELECT email FROM acceso_admin WHERE email = '"+ email +"'")

        email = cursor.fetchall()

        cursor.close()

        return email
    def traerDatosAcceso(self, email):
        cursor = DB.cursor()

        cursor.execute("SELECT usuario, password FROM acceso_admin WHERE email = '"+ email +"'")

        datos = cursor.fetchall()

        cursor.close()

        return datos