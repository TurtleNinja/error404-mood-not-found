
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_login import current_user, login_user, logout_user, login_required
from flaskr import app, db
from flaskr.models import Entry, User
from flaskr.forms import SignUpForm, LoginForm
from werkzeug.urls import url_parse
import json, sqlite3

from flaskr.query_media import get_content
#from flaskr.chatbot import chatbot


@app.route('/')
def index():
    return render_template("homePage.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm(request.form)
    message = None
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()

            if not user or not user.check_password(request.form['password']):
                message = "Username or password is incorrect."
                flash(message, 'failure')
                form.username.data = ""
            else:
                login_user(user, remember=True)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    return redirect(url_for('index'))
                return redirect(next_page)

    return render_template("LogInPage.html", title="Log in", form=form, message=message)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    message = None
    if request.method == "POST":
        if form.validate_on_submit():
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            # check if the username already exists
            if User.query.filter_by(username=username).all():
                message = f"Username {username} already exists."
                flash(message, 'failure')

            # check if the email already exists
            if User.query.filter_by(email=email).all():
                message = f"Email {email} already exists."
                flash(message, 'failure')

            if not message:
                # create a data instance
                u = User(username=username, email=email)
                u.set_password(password)

                # add to the database
                db.session.add(u)
                db.session.commit()
                return redirect(url_for('index'))

    return render_template("SignUpPage.html", title="Sign Up", form=form, message=message)

@app.route('/mood_rating', methods=['POST','GET'])
@login_required
def mood_rate():
    if request.method == 'POST':
        rating = request.form['rating']
        journal = request.form['entrytext']

        title = journal.split('\n')[0]
        entryList = journal.split('\n')[1:]
        entry = ""
        entry = entry.join(entryList)
        print(current_user)
        new_entry = Entry(mood_rate=rating, title=title, journal=entry, author=current_user)

        # add to database
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('mood_tracker'))
    return render_template("moodrating.html")

@app.route('/mood_rating/<int:id>', methods=['POST', 'GET'])
@login_required
def edit(id):
    getEntry = Entry.query.get_or_404(id)
    print("retrieved Entry: ", getEntry.title)
    print("retrieved Entry: ", getEntry.journal)
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
@login_required
def delete(id):
    deleteEntry = Entry.query.get_or_404(id)

    db.session.delete(deleteEntry)
    db.session.commit()
    return redirect(url_for('mood_tracker'))

@app.route('/mood_tracker', methods=['POST', 'GET'])
@login_required
def mood_tracker():
    print("successful")
    if current_user.is_authenticated:
        get_user_id = User.query.filter_by(username=current_user.username).first().id
        print(get_user_id)
        allEntries = Entry.query.filter_by(author_id=get_user_id).order_by(Entry.id.desc()).all()
        return render_template("moodtracker.html", entryData=allEntries)
    else:
        return render_template("moodtracker.html")

@app.route('/get_data', methods=['GET'])
def get_data():
    if current_user.is_authenticated:
        get_user_id = User.query.filter_by(username=current_user.username).first().id
        print(get_user_id)
        allEntries = Entry.query.filter_by(author_id=get_user_id).all()
        dateList = []
        rateList = []
        for data in allEntries:
            # date for x-axis
            label = data.date.strftime("%x")
            dateList.append(label)
            # rating for y-axis
            data = data.mood_rate
            rateList.append(data)

        # get only last 7 recent date and rating to display on chart
        recentDateList = dateList[-7:]
        recentRatings = rateList[-7:]
        return jsonify({'mood':json.dumps({'data':recentRatings, 'labels':recentDateList})})

    else:
        return jsonify({'mood':json.dumps({'data':[], 'labels':[]})})


@app.route('/mood_randomizer_home')
def mood_randomizer_home():
    moods = ["Relaxed", "Amused", "Motivated", "Optimistic", "Energized"]
    return render_template("moodrandhome.html", moods=moods)



@app.route('/mood_randomizer/<string:mood>')
def mood_randomizer(mood):
    data = get_content(mood.title())
    print(mood, data)

    if data == []:
        return render_template('moodRandomizerTemplate.html', content=data), 404

    content=data[0]
    mood_content = {'mood': content[0],
                    'type': content[1],
                    'link': content[2],
                    'title': content[3]}
    print(mood_content)
    print(jsonify(mood_content))

    return render_template('moodRandomizerTemplate.html', content=mood_content)


#@app.route('/mood_randomizer_amazed')
#def mood_randomizer_amazed():
#    rand_content = get_content('Amazed')


#    for element in rand_content:
#        media_type=element[1]
#        media_link=element[2]
#        media_title=element[3]

#    return render_template('MoodRandomizerAmazed.html', media=media_type, title=media_title, link=media_link)


#@app.route('/mood_randomizer_intrigued')
#def mood_randomizer_intrigued():
#    rand_content = get_content('Intrigued')


#    for element in rand_content:
#        media_type=element[1]
#        media_link=element[2]
#        media_title=element[3]

#    return render_template('MoodRandomizerIntrigued.html', media=media_type, title=media_title, link=media_link)


#@app.route('/mood_randomizer_optimistic')
#def mood_randomizer_optimistic():
#    rand_content = get_content('Optimistic')


#    for element in rand_content:
#        media_type=element[1]
#        media_link=element[2]
#        media_title=element[3]

#    return render_template('MoodRandomizerOptimistic.html', media=media_type, title=media_title, link=media_link)


#@app.route('/mood_randomizer_energized')
#def mood_randomizer_energized():
#    rand_content = get_content('Energized')


#    for element in rand_content:
#        media_type=element[1]
#        media_link=element[2]
#        media_title=element[3]

#    return render_template('MoodRandomizerEnergized.html', media=media_type, title=media_title, link=media_link)



#@app.route("/get")
#def get_bot_response():
#    userText = request.args.get('msg')
#    return str(chatbot.get_response(userText))

@app.route('/chatbot')
@login_required
def chat():
    return render_template("JoyBotPage.html")

@app.route('/temp_chatbot')
def temp_chat():
    return render_template("temp_JoyBotPage.html")
