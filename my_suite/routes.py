from flask import render_template
from my_suite import my_app, my_database
from my_suite.models import Game, Review

@my_app.route("/base.html")
def base():
    return render_template("base.html")