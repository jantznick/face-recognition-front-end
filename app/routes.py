from flask import Flask, flash, request, redirect, url_for, render_template, redirect
from app import app

import os
from werkzeug.utils import secure_filename

full_path = os.path.realpath(__file__)
UPLOAD_FOLDER = os.path.dirname(full_path) + '/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/submit-photo', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		# if user does not select file, browser also
		# submit an empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash(f'File Upload Successful {file.filename}')
			return redirect(request.url)
	return render_template('upload_successful.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return redirect('/')