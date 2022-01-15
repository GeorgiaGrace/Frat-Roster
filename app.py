from flask import Flask, render_template
from excel import createlists, majorfinder, getMajors

app = Flask(__name__)

@app.route("/")
def home():

    return render_template('home.html')

@app.route("/majors")
def majors():
    members = createlists()

    memberArray = []

    for i in range( 0 , len(members) ):

        memberArray.append(members[i])

    membersSorted = sorted( memberArray, key = lambda i : i["Name"])

    return render_template('majors.html', members=membersSorted, majors=getMajors())

@app.route("/brothers")
def brothers():
    members = createlists()

    memberArray = []

    for i in range( 0 , len(members) ):

        memberArray.append(members[i])

    membersSorted = sorted( memberArray, key = lambda i : i["Name"])

    return render_template('brothers.html', members=membersSorted)

@app.route('/<major>')
def major(major):

    members = majorfinder(major)

    membersSorted = sorted( members, key = lambda i : i["Name"])

    return render_template('major.html', members=membersSorted, major=major)