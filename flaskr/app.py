from flask import Flask, render_template, request, redirect, url_for, jsonify
from flaskr import app
from flaskr.models import Entry, User
from flaskr.forms import SignUpForm, LoginForm
from flaskr import db
import json

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
def mood_randomizer_laugh():
    return render_template("MoodRandomizerLaugh.html")

@app.route('/mood_randomizer_relax')
def mood_randomizer_relax():
    return render_template("moodrandrelax.html")

@app.route('/chat')
def chat():
    return render_template("example.html")
