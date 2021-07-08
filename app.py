from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story, silly_story, excited_story

STORIES = {"silly": silly_story, "excited": excited_story}


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def choose_story():
    """Allow user to choose story template"""
    return render_template('choose.html')

@app.route('/questions')
def questions():
    """Render questions on page"""
    story_choice = request.args["story"]
    prompts = STORIES[story_choice].prompts
    return render_template('questions.html',prompts=prompts,story_choice=story_choice)

@app.route('/results')
def result():
    """Renders story page with words from forms filled"""
    story_choice = request.args["story_choice"]
    return render_template('story.html',story=STORIES[story_choice].generate(request.args))

