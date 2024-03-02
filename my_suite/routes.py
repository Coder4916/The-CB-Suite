from flask import render_template, request, redirect, url_for
from my_suite import my_app, my_database
from my_suite.models import Review, Game
import json


@my_app.route("/")
def home():
    return render_template("home.html")


@my_app.route("/games")
def games():
    data = []
    with open("my_suite/data/games.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("games.html", games=data)


@my_app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = Review(review_name=request.form.get("review_name"))
        my_database.session.add(review)
        my_database.session.commit()
        return redirect(url_for("reviews"))
    return render_template("add_review.html")


@my_app.route("/reviews")
def reviews():
    return render_template("review.html")
