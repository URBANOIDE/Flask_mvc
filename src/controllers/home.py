from flask import render_template
from src import app
from src.config.db import DB

@app.route('/')
def index():
    if(DB == False):
        return render_template('instalacion.html')
    return render_template('index.html')