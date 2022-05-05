from turtle import title
from flask import render_template
from app import app
from .requests import get_headlines, get_sources_articles
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    headlines=get_headlines()
    return render_template('index.html', headlines=headlines, title="headlines")



@app.route('/sources/<id>')
def sources_articles(id):

    newsArticles=get_sources_articles(id)
    return render_template('source.html', news=newsArticles, title='bbc')