""" This file is for blah blah blah """
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Index Route """
    return "Hello Sammy!"
