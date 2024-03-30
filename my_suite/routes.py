from flask import render_template, request, redirect, url_for
from my_suite import my_app, my_database
from my_suite.models import Review, Game


#Function to render the home/ blog template
@my_app.route("/")
def home():
    return render_template("home.html", page_title="Home")


# Function to render the games template, 
# presenting all games added to my_database, to the user
@my_app.route("/games")
def games():
    games = list(Game.query.order_by(Game.name).all())
    return render_template("games.html", page_title="Games", games=games)


# Function to render reviews template, 
# getting all reviews from my_database
# that have been added to the site and 
# displaying them to the user
@my_app.route("/reviews")
def reviews():
    reviews = list(Review.query.order_by(Review.id).all())
    return render_template("reviews.html", reviews=reviews, page_title="Game Reviews")


# Function to render an add_review template 
# monitoring a POST of form data when a 
# review is added to the site
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


# Function to render an edit_review template, 
# getting all existing review data from the database
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



