from app import app
import urllib.request
import json
from app.models import Headlines


# Getting api key
api_key = app.config['NEWS_API_KEY']

# getting the base url
base_url=app.config['NEWS_BASE_URL']