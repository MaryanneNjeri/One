from flask import render_template,request,url_for
from . import main
from ..request import get_images

@main.route('/')
def index():
    animals =get_images('animals')
    title = 'Home Welcome to the one minute pitch app'
    return render_template('index.html',title =title,animals=animals)
