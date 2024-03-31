from flask import Flask
from flask_migrate import Migrate

from app.config import AppConfig, DatabaseConfig

from app.database import db


app = Flask(__name__)
app.config.from_object(AppConfig)
app.config.from_object(DatabaseConfig)


# initializing the database
db.init_app(app)

from app.models.user import User
from app.models.theme import Theme
from app.models.topic import Topic
from app.models.message import Message

migrate = Migrate(app, db)

