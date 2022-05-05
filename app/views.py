from turtle import title
from flask import render_template
from app import app
from .requests import get_headlines, get_bbc
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    headlines=get_headlines()
    return render_template('index.html', headlines=headlines, title="headlines")



@app.route('/bbc')
def bbc():

    bbcNews=get_bbc()
    return render_template('bbc.html', news=bbcNews, title='bbc')