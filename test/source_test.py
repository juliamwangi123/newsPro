import unittest

from app.models import Articles



class ArticleTest(unittest.TestCase):

    def setUp(self):
        self.article_news = Articles('Flask is awesome','mike will','finding best tutorials','http://www.abc.net.au/news','https://cdn.vox-cdn.com/thumbor/OYrvaaOHBuEpdTeRO55nZnZdexs=/0x215:3000x1786/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/8937281/acastro_170726_1777_0007_v2.jpg','2022-04-08T16:02:52Z','Block and Blockstream are partnering with Tesla on an open-source, solar-powered Bitcoin mine')

    def test_instance(self):
        self.assertTrue(isinstance(self.article_news,Articles))    

if __name__ == '__main__':
    unittest.main()
