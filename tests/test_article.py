import unittest
from app.models import Article

class TestSource(unittest.TestCase):
    '''Test class for model Article class'''

    def setUp(self):
        '''Instantiate article class'''
        objSArticle = Article('cnn.com','Mr Mike','Example Article Title','This is an article description','http://cnn.com','http://cnn.com','2012-05-03','This article content, read and be informed')

    def test_instance(self):
        '''Test whether class Source class instantiate objs accordingly'''

        self.assertTrue(isinstance(self.objArticle,Article)) 

    