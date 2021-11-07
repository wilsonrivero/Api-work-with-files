from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import SECRET_KEY


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///storage.db'
app.secret_key = SECRET_KEY
db = SQLAlchemy(app)

from src.controllers import routes
