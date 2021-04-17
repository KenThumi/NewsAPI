class Source:
    '''Class that handles news sources'''
    def __init__(self,url):
        self.url = url


class Article:
    '''Class that handles articles including their structure'''


    def __init__(self,source,author,art_title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.author = author
        self.art_title = art_title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
