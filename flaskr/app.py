
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flaskr import app
from flaskr.models import Entry, User
from flaskr.forms import SignUpForm, LoginForm
from flaskr import db
import json
import sqlite3

from flaskr.query_media import get_content


@app.route('/')
def index():
    return render_template("homePage.html")


@app.route('/login')
def login():
    return render_template("LogInPage.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            # check if the username already exists
            print(User.query.filter_by(username=username).all())
            if User.query.filter_by(username=username):
                message = f"Username {username} already exists."
                flash(message, 'failure')
            
            if User.query.filter_by(email=email):
                message = f"Email {email} already exists."
                flash(message, 'failure')

            if not message:
                # create a data instance
                u = User(username=username)
                u.set_password(password)

                # add to the database
                db.session.add(u)
                db.session.commit()
                return redirect(url_for('index'))
        
    return render_template("SignUpPage.html", title="Sign Up", form=form)

@app.route('/mood_rating', methods=['POST','GET'])
def mood_rate():
    if request.method == 'POST':
        rating = request.form['rating']
        journal = request.form['entrytext']
        print("journal", journal)
        title = journal.split('\n')[0]
        entryList = journal.split('\n')[1:]
        entry = ""
        entry = entry.join(entryList)
        new_entry = Entry(mood_rate=rating, title=title, journal=entry)
        print(new_entry)

        # add to database
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('mood_tracker'))
    return render_template("moodrating.html")

@app.route('/mood_rating/<int:id>', methods=['POST', 'GET'])
def edit(id):
    getEntry = Entry.query.get_or_404(id)
    print("retrieved Entry: ", getEntry)
    if request.method == 'POST':
        getEntry.mood_rate = request.form['rating']

        # get whole entry and split into 'title' and 'journal'
        fullEntryText = request.form['entrytext']
        getEntry.title = fullEntryText.split('\n')[0]
        entryList = fullEntryText.split('\n')[1:]
        entry = ""
        getEntry.journal = entry.join(entryList)

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

@app.route('/get_data', methods=['GET'])
def get_data():
    allEntries = Entry.query.all()
    dateList = []
    rateList = []
    for data in allEntries:
        # date for x-axis
        label = data.date.strftime("%x")
        dateList.append(label)
        # rating for y-axis
        data = data.mood_rate
        rateList.append(data)
    # dict = {'Date': dateList,
    #        'Rating': rateList}
    # df = pd.DataFrame(dict)
    # df.groupby([df['Date'].dt.date]).mean()
    # print(df)
    return jsonify({'mood':json.dumps({'data':rateList, 'labels':dateList})})


@app.route('/mood_randomizer_home')
def mood_randomizer_home():
    return render_template("moodrandhome.html")

@app.route('/mood_randomizer_amused')
def mood_rand_amused():
    rand_content = get_content('Amused')


    for element in rand_content:
        media_type=element[1]
        media_link=element[2]
        media_title=element[3]

    return render_template('moodrandrelax.html', media=media_type, title=media_title, link=media_link)

@app.route('/mood_randomizer_relax')
def mood_randomizer_relax():
    rand_content = get_content('Relaxed')


    for element in rand_content:
        media_type=element[1]
        media_link=element[2]
        media_title=element[3]

    return render_template('moodrandrelax.html', media=media_type, title=media_title, link=media_link)

@app.route('/chat')
def chat():
    return render_template("example.html")
