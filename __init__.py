from flask import Flask, Blueprint
from flask_migrate import Migrate

from api import song_api
from api.artists import namespace as artist_namespace
from api.songs import namespace as song_namespace
from api.spotify import namespace as spotify_namespace
from config import Config
from database.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    api_blueprint = Blueprint('api', __name__, url_prefix="/api")
    song_api.init_app(api_blueprint)
    song_api.add_namespace(song_namespace)
    song_api.add_namespace(artist_namespace)
    song_api.add_namespace(spotify_namespace)

    app.register_blueprint(api_blueprint)

    return app
