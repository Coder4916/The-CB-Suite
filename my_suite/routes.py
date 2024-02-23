from flask import render_template
from my_suite import my_app, my_database
from my_suite.models import Game, Review

@my_app.route("/")
def home():
    return render_template("home.html")

@my_app.route("/reviews")
def reviews():
    return render_template("reviews.html")

@my_app.route("/add_review", methods=["GET", "POST"])
def add_review():
    return render_template("add_review.html")

@my_app.route("/games")
def games():
    return render_template("games.html")