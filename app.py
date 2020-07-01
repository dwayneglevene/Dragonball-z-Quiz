#clou# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template, redirect
from flask import request
from datetime import datetime
from model import getProperties

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",time=datetime.now())


# @app.route('/greeting', methods=["POST", "GET"])

@app.route('/character',methods=["POST", "get"])


def choose():
    if request.method == "POST":
        print(request.form)
        name = request.form["nickname"]
        if name == "":
            props = getProperties({"hour": "hour","mode":"cloud","hv":"bad"})
        else:
            props = getProperties(request.form)
        print(name)
        #print(hour)
        #print(poll)
        return render_template('character.html', person=name,props=props)
    else:
        print("PB & J")
        
        return "You shouldnt be here"

    
