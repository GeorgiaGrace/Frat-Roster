from flask import Flask, render_template
from excel import createlists, majorfinder

app = Flask(__name__)

@app.route("/")
def home():
    members = createlists()

    memberArray = []

    for i in range( 0 , len(members) ):

        memberArray.append(members[i])

    membersSorted = sorted( memberArray, key = lambda i : i["Name"])

    return render_template('index.html', members=membersSorted)

@app.route('/<major>')
def major(major):

    members = majorfinder(major)

    membersSorted = sorted( members, key = lambda i : i["Name"])

    return render_template('major.html', members=membersSorted, major=major)