from flask import render_template
from my_suite import my_app, my_database


@my_app.route("/")
def base():
    return render_template("base.html")