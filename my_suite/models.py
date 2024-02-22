from my_suite import my_database


class Game(my_database.Model):
    # The Game model
    id = my_database.Column(my_database.Integer, primary_key=True)
    game_name = my_database.Column(my_database.String(40), unique=True, nullable=False)
    reviews = my_database.relationship("Review", backref="game", cascade="all, delete", lazy=True)
    def __str__(self):
        # represents itself
        return self.game_name



class Review(my_database.Model):
    # The Review model
    id = my_database.Column(my_database.Integer, primary_key=True)
    review_owner = my_database.Column(my_database.String(40), unique=True, nullable=False)
    review_date = my_database.Column(my_database.Date, nullable=False) 
    game_id = my_database.Column(my_database.Integer, my_database.ForeignKey('game.id', ondelete="CASCADE"), nullable=False) 
    def __str__(self):
        # represents itself
        return "#{0} - Review: {1} | Score: {2}".format(
            self.id, self.review_name, self.review_stars
        )