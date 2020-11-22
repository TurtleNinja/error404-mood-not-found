from flask import Flask, render_template
from flaskr import app


@app.route('/')
def index():
    return render_template("homePage.html")


@app.route('/login')
def login():
    return render_template("LogInPage.html")

@app.route('/signup')
def signup():
    return render_template("SignUpPage.html")

@app.route('/mood_tracker')
def mood_randomizer():
    return render_template("moodtracker.html")

@app.route('/mood_rating')
def mood_rate():
    return render_template("moodrating.html")

@app.route('/mood_tracker')
def mood_tracker():
    return render_template("moodtracker.html")

@app.route('/mood_randomizer_home')
def mood_randomizer_home():
    return render_template("moodrandhome.html")

@app.route('/mood_randomizer_laugh')
def mood_randomizer_laugh():
    return render_template("MoodRandomizerLaugh.html")

@app.route('/mood_randomizer_relax')
def mood_randomizer_relax():
    return render_template("moodrandrelax.html")    

@app.route('/chat')
def chat():
    return render_template("example.html")
