# shop/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# set a secrete key
app.config["SECRET_KEY"] = "b6ee52d0deaf51e633f1b72e0da2cd4c"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///glofarmersMkt.db"

# Create a database instance
db = SQLAlchemy(app)

# Import routes after initializing app and db
from shop.admin import routes
