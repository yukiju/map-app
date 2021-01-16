from flask import Flask
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