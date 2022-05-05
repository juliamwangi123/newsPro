from flask import render_template
from app import app
from .requests import get_headlines
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    headlines=get_headlines()
    return render_template('index.html', headlines=headlines)