from flask import render_template, request, redirect, url_for, session
from src import app
from src.models.proveedores import ProveedoresModel
from flask_mail import Mail, Message

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'Albertochind04@gmail.com'
app.config['MAIL_PASSWORD'] = 'oudqllymhvhxxgja'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/recuperacion')
def recuperacion():
    #verificacion de si se ha iniciado sesion, para que no puedan acceder a la ruta sin haberse logueado


    msg = Message(
    subject= 'Hola esto es una prueba',
    sender ='Albertochind04@gmail.com', 
    recipients = 'Albertochindoy2020@itp.edu.co',
    body= "Mensaje"
    )  
    mail.send(msg)
    return render_template ('login/login.html')