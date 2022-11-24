from flask import render_template, request, redirect, url_for, session, flash
from src import *
from src.models.recuperacion_password import RecuperacionModel
from flask_mail import Mail, Message

@app.route('/recuperacion', methods =['GET', 'POST'])
def recuperacion():
    if request.method == 'GET':
        return render_template ('recuperacion_password/recuperacion_password.html')
    
    email = request.form.get('email')
    recuperacionModel = RecuperacionModel()
    #Validacion del correo a enviar la contraseña
    correo = recuperacionModel.traerEmail(email)
    if correo == []:
        mensaje = "El correo digitado no existe en la base de datos"
        return render_template ('recuperacion_password/recuperacion_password.html', mensaje=mensaje)
    else:
        #Traemos los datos de inicio de sesión
        datos = recuperacionModel.traerDatosAcceso(email)
        for i in datos:
            usuario = i[0]
            password = i[1]
        #Envio del emal si el correo ingresado está registrado
        with app.app_context():
            msg = Message(subject="Recuperacion de contraseña",
                sender=app.config.get("MAIL_USERNAME"),
                recipients=[email])
            msg.html = render_template('recuperacion_password/mensaje.html', usuario=usuario, password=password)
            mail.send(msg)
        mensaje = "Los datos se han enviado al email proporsionado"
        return render_template ('recuperacion_password/recuperacion_password.html', mensaje=mensaje)