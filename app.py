from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<string:username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))