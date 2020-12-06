from flask import Flask, render_template, request, redirect, url_for
from flaskr import app
from flaskr.models import Entry, User
from flaskr.forms import SignUpForm, LoginForm
from flaskr import db

@app.route('/')
def index():
    return render_template("homePage.html")


@app.route('/login')
def login():
    return render_template("LogInPage.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    else:
        return render_template("SignUpPage.html", title="Sign Up", form=form)

@app.route('/mood_rating', methods=['POST','GET'])
def mood_rate():
    if request.method == 'POST':
        rating = request.form['rating']
        journal = request.form['entrytext']
        new_entry = Entry(mood_rate=rating, journal=journal)
        print(new_entry)

        # add to database
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('mood_tracker'))
    return render_template("moodrating.html")

@app.route('/mood_rating/<int:id>', methods=['POST', 'GET'])
def edit(id):
    # https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
    getEntry = Entry.query.get_or_404(id)
    print("retrieved Entry: ", getEntry)
    if request.method == 'POST':
        getEntry.mood_rate = request.form['rating']
        getEntry.journal = request.form['entrytext']

        db.session.commit()
        return redirect(url_for('mood_tracker'))
    return render_template("moodrating_edit.html", getEntry=getEntry)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    deleteEntry = Entry.query.get_or_404(id)
    print("retrieved Entry: ", deleteEntry)
    db.session.delete(deleteEntry)
    db.session.commit()
    return redirect(url_for('mood_tracker'))

@app.route('/mood_tracker', methods=['POST', 'GET'])
def mood_tracker():
    print("successful")
    allEntries = Entry.query.order_by(Entry.date.desc()).all()
    print("Stored Entries ", allEntries)
    return render_template("moodtracker.html", entryData=allEntries)

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
