from email.quoprimime import quote
from app.request import get_quotes
from . import main
from flask import render_template

@main.route('/')
def index():
   quote =get_quotes()
   
   return render_template('index.html', quote =quote)


