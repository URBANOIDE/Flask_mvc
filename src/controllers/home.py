from xml.dom.minidom import Identified
from flask import render_template, request, redirect, url_for, session
from src import app
import random
from src.models.login import IngresosModel

@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('login/login.html')

@app.route('/entrar/admin', methods =['GET', 'POST'])
def login_admin():
  if request.method == 'GET':
     return render_template('login/inicio_admin.html')
  usuario = request.form.get('usuario')
  password = request.form.get('password')

  ingresosModel = IngresosModel()
  user = ingresosModel.iniciarAdmin(usuario, password)
  error = "Error de ingreso"
  #validacion de ingreso
  if user != None:
     #sesiones
     session['id'] = user[0]
     session['administrador'] = user[3]
     session['usuario'] = "administrador"
     return render_template('index_admin.html')
  else: return render_template('login/inicio_admin.html', error = error)

@app.route('/entrar/administrador', methods =['GET', 'POST'])
def admin():
   return render_template('index_admin.html')

@app.route('/entrar/user', methods =['GET', 'POST'])
def login_user():
  if request.method == 'GET':
     return render_template('login/inicio_user.html')
   
  usuario = request.form.get('usuario')
  password = request.form.get('password')
  ingresosModel = IngresosModel()
  user = ingresosModel.iniciarUser(usuario, password)
  
  error = "Error de ingreso"
  #validacion de ingreso
  if user != None:
     #sesiones
     session['id'] = user[0]
     session['identificacion'] = user[2]
     session['administrador'] = user[3]
     session['administradorA'] = user[4]
     session['usuario'] = "empleado"
     return render_template('index_user.html')
  else: return render_template('login/inicio_user.html', error = error)

@app.route('/entrar/empleado', methods =['GET', 'POST'])
def user():
   return render_template('index_user.html')

@app.route('/cerrar')
def logout():
   session.pop('usuario', None)
   session.pop('administradorA', None)
   session.pop('administrador', None)
   session.pop('id', None)
   session.pop('identificacion', None)

   return redirect(url_for('index'))

@app.route('/entrar/admin/password', methods =['GET', 'POST'])
def cambioPassword():
   #verificacion de si se ha iniciado sesion, para que no puedan acceder a la ruta sin haberse logueado
   if session == {}:
        return render_template('login/login.html')
   #aunque se haya logueado, solo el administrador podrá ingresar a la ruta
   if session['usuario'] == 'empleado':
        session.pop('usuario', None)
        session.pop('administradorA', None)
        session.pop('administrador', None)
        session.pop('id', None)
        session.pop('identificacion', None)
        return render_template('login/login.html')
   if request.method == 'GET':
      nombre = session['administrador']
      
      ingresosModel = IngresosModel()
      id_admin = session['id']
      user = ingresosModel.traerDatosAdmin(id_admin)
      for u in user:
         user = u[0]
         passwor = u[1]
         email = u[2]
      return render_template('login/cambio_password.html', nombre = nombre, user = user, passwor = passwor, email = email)
   nombre = request.form.get('nombre')
   usuario = request.form.get('usuario')
   password = request.form.get('password')
   email = request.form.get('email')

   id = session['id']

   ingresosModel = IngresosModel()
   ingresosModel.cambiarPassword(id, nombre, usuario, password, email)
   session.pop('usuario', None)
   session.pop('administradorA', None)
   session.pop('administrador', None)
   session.pop('id', None)
   
   return redirect(url_for('index'))