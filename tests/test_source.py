import unittest
from app.models import Source

class TestSource(unittest.TestCase):
    '''Test class for model Source class'''

    def setUp(self):
        '''Instantiate Source class'''
        self.objSource = Source('cnn.com')

    def test_instance(self):
        '''Test whether class Source class instantiate objs accordingly'''

        self.assertTrue(isinstance(self.objSource,Source)) 

    