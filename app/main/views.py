from flask import render_template,request,url_for
from . import main
from ..request import get_images

@main.route('/')
def index():
    fashion =get_images('fashion')
    business=get_images('business')
    health=get_images('health')
    religion=get_images('religion')
    title = 'Home Welcome to the one minute pitch app'
    return render_template('index.html',title =title,fashion=fashion,business=business,religion=religion,health=health)
