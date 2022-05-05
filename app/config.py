import os

class Config:
    '''
    General configuration parent class
    '''
    
    NEWS_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BBC_URL='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}'
    CNN_URL='https://newsapi.org/v2/top-headlines?sources=cnn-news&apiKey={}'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True