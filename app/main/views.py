from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():
    lorem = 'lorem Ipsum'
    return render_template('index.html',lorem='lorem')