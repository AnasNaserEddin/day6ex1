#!/usr/local/bin/python3
#
# basic_flask.py
# class_6

import flask
import random

app = flask.Flask("MyApp") # Creating a controller (the object that organizes everything)

@app.route('/roll/<int:number>')
def index(number):
    if(number not in range(1,101)):
        return "please roll a number between 1 and 100"
    else:
        rand_num=random.randint(1, 100)
        if(rand_num==number):
            return ("success")
        else:
            return ("failed ")


app.run(debug=True)