from app import app
from flask import render_template

@app.route("/")
@app.route("/index")

def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

def testimonials():
    """testinomials URL"""
    return render_template('index.html', section_anchor='testimonials')


@app.route("/about")

def about():
    """about URL"""
    return render_template('about.html', title='About Page')

@app.route("/modal")

def modal():
    """modal URL"""
    return render_template('modal.html', title='modal Page')