from flask import render_template, request, redirect, url_for
from src import app
import random

@app.route('/')
def index():
    return render_template('index.html')