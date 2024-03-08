from flask import render_template, request, redirect, url_for
from my_suite import my_app, my_database
from my_suite.models import Review, Game
import json


@my_app.route("/")
def home():
    return render_template("home.html", page_title="Home")


@my_app.route("/games")
def games():
    data = []
    with open("my_suite/data/images.json", "r") as json_data:
        data = json.load(json_data)
    games = list(Game.query.order_by(Game.game_name).all())
    return render_template("games.html", page_title="Games", games=games, images=data)


@my_app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        game = Game(
            game_name=request.form.get("game_name"),
            game_genre=request.form.get("game_genre"),
            game_developer=request.form.get("game_developer"),
            game_release_date=request.form.get("game_release_date")
        )
        my_database.session.add(game)
        my_database.session.commit()
        return redirect(url_for("games"))
    return render_template("add_game.html", page_title="Add Game")
    

@my_app.route("/edit_game/<int:game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    game = Game.query.get_or_404(game_id)
    if request.method == "POST":
        game.game_name = request.form.get("game_name")
        my_database.session.commit()
        return redirect(url_for('games'))
    return render_template("edit_game.html", page_title="Edit game", game=game)


@my_app.route("/delete_game/<int:game_id>")
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    my_database.session.delete(game)
    my_database.session.commit()
    return redirect(url_for("games"))


@my_app.route("/reviews")
def reviews():
    return render_template("reviews.html", page_title="Reviews")


@my_app.route("/add_review", methods=["GET", "POST"])
def add_review():
    games = list(Game.query.order_by(Game.game_name).all())
    if request.method == "POST":
        review = Review(
            review_name=request.form.get("game_name"),
            review=request.form.get("game_genre"),
            review_date=request.form.get("game_release_date")
        )
        my_database.session.add(game)
        my_database.session.commit()
        return redirect(url_for("games"))
    return render_template("add_game.html", page_title="Add Game")



