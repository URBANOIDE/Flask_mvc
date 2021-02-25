from flask import Flask, render_template
from src import app


@app.route('/productos')
def productos():
    return 'productos'