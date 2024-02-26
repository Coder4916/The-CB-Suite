from my_suite import my_database


class Game(my_database.Model):
    # The Game model
    id = my_database.Column(my_database.Integer, primary_key=True)
    game_name = my_database.Column(my_database.String(30), unique=True, nullable=False)
    tasks = my_database.relationship("Review", backref="game", cascade="all, delete", lazy=True)
    def __repr__(self):
        # represents itself
        return self.game_name



class Review(my_database.Model):
    # The Review model
    id = my_database.Column(my_database.Integer, primary_key=True)
    review_name = my_database.Column(my_database.String(30), unique=True, nullable=False)
    review = my_database.Column(my_database.Text, nullable=False)
    review_date = my_database.Column(my_database.Date, nullable=False)
    game_id = my_database.Column(my_database.Integer, my_database.ForeignKey("game.id", ondelete="CASCADE"), nullable=False)
    def __repr__(self):
        # represents itself
        return "#{0} Reviewer: {1} | Review: {2} | Date: {3}".format(
            self.id, self.review_name, self.review, self.review_date
        )