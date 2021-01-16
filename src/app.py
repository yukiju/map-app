from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hellow')
def hello_world():
    return 'Hello World'

@app.route('/hello')
def hello():
    return 'Hello, world'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)