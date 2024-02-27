from flask import render_template, request, redirect, url_for
from my_suite import my_app, my_database
from my_suite.models import Review, Game


@my_app.route("/")
def home():
    return render_template("home.html")


@my_app.route("/games")
def games():
    return render_template("games.html")


@my_app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        game = Game(game_name=request.form.get("game_name"))
        my_database.session.add(game)
        my_database.session.commit()
        return redirect(url_for("games"))
    return render_template("add_game.html")


@my_app.route("/reviews")
def reviews():
    return render_template("review.html")
