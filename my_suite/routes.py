from flask import render_template, request
from my_suite import my_app, my_database
from my_suite.models import Review, Game

@my_app.route("/")
def home():
    return render_template("home.html")

@my_app.route("/reviews")
def reviews():
    return render_template("reviews.html")

@my_app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = Review()
    return render_template("add_review.html")
