import unittest

from app.models import Source



class SourceTest(unittest.TestCase):
    
    def setUp(self):
        self.source_news = Source('abc','the best news channel','http://www.abc.net.au/news')

    def test_instance(self):
        
        self.assertTrue(isinstance(self.source_news,Source))    

if __name__ == '__main__':
    unittest.main()