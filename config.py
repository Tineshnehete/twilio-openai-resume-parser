from flask import Flask
from decouple import config
from models import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app

TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN", default="")
OPENAI_API_KEY = config("OPENAI_API_KEY")
