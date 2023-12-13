from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>')
def name_page(name):
  return f'<p>Hello, {escape(name.title())}!</p>'

@app.route('/home')
def home():
    return '<h1>This is your home page</h1>'

with app.test_request_context():
   print(url_for('home'))