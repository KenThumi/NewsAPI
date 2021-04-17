class Source:
    pass
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


    # def __repr__(self):
    #     return "<Article {0} {1} {2} {3} {4} {5} {6} {7}>".format(self.source,self.author,self.art_title,self.description,self.url,self.urlToImage,self.publishedAt,self.content)