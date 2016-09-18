from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/story')
def story():
	return render_template('story.html')

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.route('/whyevyavan')
def why():
	return render_template('whyevyavan.html')

@app.route('/princetonplus')
def princetonplus():
	return render_template('princetonplus.html')

@app.route('/relationships')
def relationships():
	return render_template('relationships.html')

@app.route('/theknown')
def theknown():
	return render_template('theknown.html')

@app.route('/theunknown')
def theunknown():
	return render_template('theunknown.html')

@app.route('/legal')
def legal():
	return render_template('legal.html')