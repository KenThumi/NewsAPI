from flask import render_template,request,redirect,url_for
from . import main
# from ..models import Article
from ..requests import get_articles



@main.route('/')
def index(): 
    '''Home route'''

    articles = get_articles('aljazeera.com')

    return render_template('index.html',article_list=articles)