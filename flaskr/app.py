from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("homePage.html")


@app.route('/login')
def login():
    return "login page"


@app.route('/mood_randomizer')
def mood_randomizer():
    return render_template("mood.html")


@app.route('/mood_rating')
def mood_rate():
    return render_template("rate.html")
