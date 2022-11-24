from flask import Flask
from flask_mail import Mail

app = Flask(__name__, template_folder='views')
app.secret_key = "my_secrret_key"

#Configuracion para correos
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'albertochind04@gmail.com',
    "MAIL_PASSWORD": 'oudqllymhvhxxgja'
}
app.config.update(mail_settings)
mail = Mail(app)

#importando controllers
from src.controllers import *



def create_app():
    app.run(debug=True)