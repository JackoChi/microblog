from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'username': 'Jacko'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Working on Sat'
		},
		{
			'author': {'username':' Annie'},
			'body': 'I am making music'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
	
