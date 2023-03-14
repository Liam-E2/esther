from flask import Flask
App = Flask(__name__)

@App.route('/')
def hello():
    return "<h1>Hello, world!</h1>"
