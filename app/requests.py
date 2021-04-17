import urllib.request,json
from .models import Article
from datetime import datetime


# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']


def get_articles(source):
    '''Function to that gets the json response to our url request'''

    get_articles_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['totalResults'] > 0:
            article_list = get_articles_response['articles']
            article_results = process_results(article_list)

    
    return article_results


def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain movie details

    Returns :
        article_results: A list of movie objects
    '''

    article_results = []

    for article_item in article_list:
        source = article_item['source'].get('name')
        author = article_item.get('author')
        art_title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage =article_item.get('urlToImage')
        publishedAt = datetime.strptime(article_item.get('publishedAt')[:10] , "%Y-%m-%d")
        publishedAt = str(publishedAt.day)+'-'+str(publishedAt.month)+'-'+str(publishedAt.year)      #formatted to 'd-mm-yyyy' 
        content = article_item.get('content')

        if urlToImage:
            article_object = Article(source,author,art_title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)


    return article_results
       
        






