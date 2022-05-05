from app import app
import urllib.request
import json
from app.models import Headlines


# Getting api key
api_key=None

# getting the base url
base_url=None

def configure_request(app):
    """Configures the request by getting the api_key and base_url"""
    global api_key, base_url
    api_key=app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_BASE_URL']


def get_headlines():
    headlines_url=base_url.format(api_key)

    with urllib.request.urlopen(headlines_url) as url:
        
        get_headlines_news_data = url.read()
        
        headlines_response = json.loads(get_headlines_news_data)
        if headlines_response["articles"]:
            
            results_list = headlines_response["articles"]
            news_results = process_results(results_list)
        
    return news_results

def process_results(news_list):
    
    """
    function that process results and cast data as my headlines class property
    
    """ 
    
    news_results = []
    
    for news_item in news_list:
        
        title = news_item.get("title")
        description = news_item.get("description")
        url = news_item.get("url")
        url_to_image = news_item.get("urlToImage")
        published_at = news_item.get("publishedAt")
        content=news_item.get("content")
        
        if title:
            headline_object = Headlines(title, description,content, url, url_to_image, published_at)
            news_results.append(headline_object)
        
       
    return news_results 