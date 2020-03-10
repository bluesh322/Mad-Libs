from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = 'agooddaytodie@ramranch'
debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """Show list of stories"""
    return render_template('index.html',
     stories=stories.values())

@app.route('/form')
def form():
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts
    return render_template('form.html',
     prompts=prompts,
     title=story.title,
     story_id=story_id,
     stories=stories.values())

@app.route('/madlib')
def show_madlib():
    story_id = request.args["story_id"]
    story = stories[story_id]

    madlib_text = story.generate(request.args)
    return render_template('madlib.html',
    madlib_text=madlib_text,
    title=story.title,
    story_id=story_id,
    stories=stories.values())