from flask import render_template, request, redirect, url_for, session
from src import app
from src.models.proveedores import ProveedoresModel
from flask_mail import Mail, Message

@app.route('/recuperacion')
def recuperacion():
    
    return render_template ('login/login.html')