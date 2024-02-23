import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env # noqa


my_app = Flask(__name__)
my_app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
my_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URL')

my_database = SQLAlchemy(my_app)

from my_suite import routes # noqa