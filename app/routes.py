from flask import render_template
from app import app


@app.route('/')  # route decorator
@app.route('/index')
def index():
    user = {'username': 'Jeph'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, title="Home", posts=posts)
