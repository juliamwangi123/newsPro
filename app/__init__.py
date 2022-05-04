from flask import Flask
from .config import DevConfig

app=Flask(__name__)

from app import views