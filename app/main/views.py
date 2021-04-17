from flask import render_template,request,redirect,url_for
from . import main
# from ..models import Article
from ..requests import get_articles



@main.route('/')
def index(): 
    '''Homepage route'''

    source_query = request.args.get('source_query')

    if source_query:
        return redirect(url_for('.source',source=source_query))
    else:
        return render_template('index.html')


@main.route('/sources/<source>')
def source(source):
    '''Routes you depending on the route source'''

    articles = get_articles(source)
    
    return render_template('news.html',article_list=articles)