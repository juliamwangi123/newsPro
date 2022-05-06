from flask import Flask
from .config import DevConfig

app=Flask(__name__,instance_relative_config = True)
# Setting up configuration
app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')


from .requests import configure_request
configure_request(app)
from app import views