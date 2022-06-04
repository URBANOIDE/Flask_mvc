from flask import Flask

app = Flask(__name__, template_folder='views')
app.secret_key = "my_secrret_key"
#importando controllers
from src.controllers import *



def create_app():
    app.run(debug=True)