from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///glofarmersMkt.db"
# create a database instance
db = SQLAlchemy(app)

from shop import routes