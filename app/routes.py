from app import app
from flask import render_template

@app.route("/")
@app.route("/home")

def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')