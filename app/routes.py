from flask import render_template, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect('/')