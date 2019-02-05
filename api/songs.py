from flask import request
from flask_restplus import Resource, fields

from api import song_api
from database.models import Song

namespace = song_api.namespace('song', description='song list')

song_model = song_api.model("song", {
    "id": fields.Integer("id of the song"),
    "name": fields.String("name of the song."),
    "artist_id": fields.String("id of the artist.")
})


@namespace.route('/')
class AllSongsAPI(Resource):
    @namespace.marshal_with(song_model)
    def get(self):
        """
        get all the songs
        """
        return Song.select_all_songs(), 200


@namespace.route('/<song_id>')
class SongAPI(Resource):
    @namespace.marshal_with(song_model)
    def get(self, song_id):
        """
        get details of a song
        """
        return Song.select_song(song_id), 200

    @namespace.marshal_with(song_model)
    def put(self, song_id):
        """
        change the song details
        """
        name = request.get_json().get('name')
        artist_id = request.get_json().get('artist_id')
        return Song.update_song(song_id, name, artist_id), 200

    def delete(self, song_id):
        """
        delete the song
        """
        return Song.delete_song(song_id)


@namespace.route('')
class SongInsertAPI(Resource):
    def post(self):
        """
        insert a song
        """
        name = request.get_json().get('name')
        artist_id = request.get_json().get('artist_id')

        return Song.insert_song(name=name, artist_id=artist_id), 200
