from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# Home page -- render questions for the story
@app.route('/')
def questions():
	"""Render question page"""
	#get questions for the 
	prompts = silly_story.prompts
	
	return render_template('questions.html',prompts=prompts)


# Story page -- render story given the texts/prompts
@app.route('/results')
def result():
	"""Renders story page with words from forms filled"""
	# grab answers dynamically from form

	return render_template('story.html',story=silly_story.generate(request.args))