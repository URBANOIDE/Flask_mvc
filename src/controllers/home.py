from flask import render_template, request, redirect, url_for
from src import app
from src.config.db import CONEXION_PATH, createDB, instalarDB
from os import path
import json
import src.config.globals as globals

@app.route('/')
def index():
    if(globals.DB == False):
        return render_template('instalacion.html')
    
    return render_template('index.html')

@app.route('/instalacion', methods=['POST'])
def instalacion():
    datos = {
        "database": request.form.get('base_datos'),
        "user": request.form.get('usuario'),
        "password": request.form.get('contrasena'),
        "host": request.form.get('host'),
        "port": int(request.form.get('puerto')),
    }
    
    conexion = open(CONEXION_PATH, 'w')

    conexion.write(json.dumps(datos))

    conexion.close()

    createDB()
    instalarDB()

    return redirect(url_for('index'))