from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import SECRET_KEY
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///storage.db'
app.secret_key = SECRET_KEY
ma = Marshmallow(app)
CORS(app)
db = SQLAlchemy(app)


from src.controllers import routes
