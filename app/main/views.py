from flask import render_template,request,redirect,url_for
from . import main
# from ..models import Article
from ..requests import get_articles



@main.route('/')
def index(): 
    '''Home route'''

    articles = get_articles('aljazeera.com')

    return render_template('index.html',article_list=articles)


@main.route('/sources/<source>')
def source(source):
    '''Routes you depending on the route source'''

    articles = get_articles(source)

    return render_template('news.html',article_list=articles)