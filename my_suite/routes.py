from flask import render_template, request, redirect, url_for
from my_suite import my_app, my_database
from my_suite.models import Review, Game


#Function to render home/ blog template
@my_app.route("/")
def home():
    return render_template("home.html", page_title="Home")


#Function to render games template, getting all games added to the site
@my_app.route("/games")
def games():
    games = list(Game.query.order_by(Game.name).all())
    return render_template("games.html", page_title="Games", games=games)


#Function to render add_game template with a POST method to add game data
@my_app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        game = Game(
            name=request.form.get("name"),
            genre=request.form.get("genre"),
            platform=request.form.get("platform"),
            developer=request.form.get("developer"),
            release_date=request.form.get("release_date"),
            image=request.form.get("image")
        )
        my_database.session.add(game)
        my_database.session.commit()
        return redirect(url_for("games"))
    return render_template("add_game.html", page_title="Add Game")
    

#Query game name = Have you used this name before? Add to function

#Function to render edit_game template and gets the selected game to edit
@my_app.route("/edit_game/<int:game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    game = Game.query.get_or_404(game_id)
    if request.method == "POST":
        game.name = request.form.get("name"),
        game.genre = request.form.get("genre"),
        game.platform = request.form.get("platform"),
        game.developer = request.form.get("developer"),
        game.release_date = request.form.get("release_date"),
        game.image = request.form.get("image")
        my_database.session.commit()
        return redirect(url_for("games"))
    return render_template("edit_game.html", page_title="Edit game", game=game)


#Function to delete_game
@my_app.route("/delete_game/<int:game_id>")
def delete_game(game_id):
    game = Game.query.get_or_404(game_id)
    my_database.session.delete(game)
    my_database.session.commit()
    return redirect(url_for("games"))


#Function to render reviews template, getting all reviews added to the site
@my_app.route("/reviews")
def reviews():
    reviews = list(Review.query.order_by(Review.id).all())
    return render_template("reviews.html", reviews=reviews, page_title="Game Reviews")


#Query review name = Have you used this name before? Add to function

#Function to render add_review template and POST review inputs to the site
@my_app.route("/add_review", methods=["GET", "POST"])
def add_review():
    games = list(Game.query.order_by(Game.name).all())
    if request.method == "POST":
        review = Review(
            username=request.form.get("username"),
            review=request.form.get("review"),
            star_rating=request.form.get("stars"),
            date=request.form.get("date"),
            game_id=request.form.get("game_id")
        )
        my_database.session.add(review)
        my_database.session.commit()
        return redirect(url_for("reviews"))
    return render_template("add_review.html", games=games, page_title="Add Review")


#Function to render edit_review template, getting all games and the selected review to edit
@my_app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)
    games = list(Game.query.order_by(Game.name).all())
    if request.method == "POST":
        review.username=request.form.get("username"),
        review.review=request.form.get("review"),
        review.star_rating=request.form.get("stars"),
        review.date=request.form.get("date"),
        review.game_id=request.form.get("game_id")
        my_database.session.commit()
        return redirect(url_for("reviews"))
    return render_template("edit_review.html", review=review, games=games, page_title="Edit Review")


#Function to delete_review 
@my_app.route("/delete_review/<int:review_id>")
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    my_database.session.delete(review)
    my_database.session.commit()
    return redirect(url_for("reviews"))



