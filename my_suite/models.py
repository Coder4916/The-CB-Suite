from my_suite import my_database


class Game(my_database.Model):
    # The Game model
    id = my_database.Column(my_database.Integer, primary_key=True)
    name = my_database.Column(my_database.String(50), nullable=False)
    genre = my_database.Column(my_database.String(50), nullable=False)
    platform = my_database.Column(my_database.String(50), nullable=False)
    developer = my_database.Column(my_database.String(50), nullable=False)
    release_date = my_database.Column(my_database.String(50), nullable=False)
    image = my_database.Column(my_database.Text, nullable=False)
    tasks = my_database.relationship("Review", backref="game", cascade="all, delete", lazy=True)
    def __repr__(self):
        # represents itself
        return self.name


class Review(my_database.Model):
    # The Review model
    id = my_database.Column(my_database.Integer, primary_key=True)
    username = my_database.Column(my_database.String(30), nullable=False)
    review = my_database.Column(my_database.Text, nullable=False)
    star_rating = my_database.Column(my_database.String(10), nullable=False)
    date = my_database.Column(my_database.Date, nullable=False)
    game_id = my_database.Column(my_database.Integer, my_database.ForeignKey("game.id", ondelete="CASCADE"), nullable=False)
    
    def __repr__(self):
        # represents itself
        return "#{0} Reviewer: {1} | Review: {2} | Date: {3}".format(
            self.id, self.name, self.review, self.date
        )