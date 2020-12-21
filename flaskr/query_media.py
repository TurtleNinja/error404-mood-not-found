
#from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
#from flaskr import app
#from flaskr.models import Entry, User
#from flaskr.forms import SignUpForm, LoginForm
#from flaskr import db
import json


import sqlite3
import os
cwd = os.getcwd()
print("curr")
print(cwd)


#conn = sqlite3.connect('randomizer.db')
#c = conn.cursor()

def get_content(mood_str):
    #c.execute("SELECT * FROM randomizer WHERE mood_type=:Mood", {'Mood': mood_str})
    #SELECT * FROM table ORDER BY RANDOM() LIMIT 1;
    cwd = os.getcwd()
    print(cwd)
    conn = sqlite3.connect('randomizer.db')
    c = conn.cursor()

    #c = conn.cursor()
    #c.execute("SELECT * FROM randomizer LIMIT 5")
    c.execute("SELECT * FROM randomizer WHERE mood_type=:Mood ORDER BY RANDOM() LIMIT 1", {'Mood': mood_str})
    res = c.fetchall()

    conn.close()

    return res
#conn.close()

#def get_emps_by_name(lastname):
#    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
#    return c.fetchall()

#emps = get_emps_by_name('Doe')
#print(emps)

#print("Total rows are:  ", len(emps))
#print("Printing each row")
#for row in emps:
#    print("Mood: ", row[0])
#    print("Type of Media: ", row[1])
#    print("Link To Media: ", row[2])
#    print("Title: ", row[3])
#    print(row)




