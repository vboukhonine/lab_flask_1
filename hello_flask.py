# run with: flask --app hello_flask --debug run

"""
Lab — Flask, Part 1
CST 205
Vera Boukhonine
07/06/2024
"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

boostrap = Bootstrap5(app)


# Task 2
# route decorator binds a function to a URL
@app.route("/")
def hello():
    hello_world = "<p>Genevieve M. : afaik</p>"
    return hello_world


# Task 3
@app.route("/vera")
def vera():
    return render_template("template.html")


# Task 4
@app.route("/mytemplate")
def t_test():
    return render_template("index.html")
# Task 5
# Link to git repo: https://github.com/vboukhonine/lab_flask_1

"""
Lab Completion Report: 
I wasn't able to complete task 2 I didn't give myself enough time to ask anyone else in the class what their favorite acronyms 
are and procrastinated too much due to fatigue from the heat wave.

References: 
https://www.tutorialspoint.com/How-to-set-Text-alignment-in-HTML
"""
