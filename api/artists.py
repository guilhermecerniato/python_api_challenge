from flask import request
from flask_restplus import Resource, fields

from api import song_api
from database.models import Artist

namespace = song_api.namespace('artist', description='artist list')

artist_model = song_api.model("artist", {
    "id": fields.String("id of the artist."),
    "name": fields.String("Name of the artist.")
})


@namespace.route('/')
class AllArtistsAPI(Resource):
    @namespace.marshal_with(artist_model)
    def get(self):
        """
        get all the artists
        """
        return Artist.select_all_artists(), 200


@namespace.route('/<artist_id>')
class ArtistAPI(Resource):
    @namespace.marshal_with(artist_model)
    def get(self, artist_id):
        """
        get details of an artist
        """
        return Artist.select_artist(artist_id)

    def put(self, artist_id):
        """
        change an artist details
        """
        name = request.get_json().get('name')
        return Artist.update_artist(artist_id, name)

    def delete(self, artist_id):
        """
        delete an artist
        """
        return Artist.delete_artist(artist_id)


@namespace.route('')
class ArtistInsertAPI(Resource):
    def post(self):
        """
        insert an artist
        """
        name = request.get_json().get('name')
        Artist.insert_artist(name=name)
        return 200
