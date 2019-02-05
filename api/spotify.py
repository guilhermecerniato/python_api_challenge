import requests
from flask import request
from flask_restplus import Resource

from api import song_api
from database.models import Artist, Song

namespace = song_api.namespace('spotify', description='spotify functions')


@namespace.route('/artist/')
class GetArtistsSpotify(Resource):
    def post(self):
        """
        insert artist by name from the spotify API
        """
        artist_name = request.get_json().get('name')
        spotify_json = artist_search(artist_name)
        Artist.insert_artist(name=spotify_json.get('artists').get('items')[0].get('name'))

        return 200


@namespace.route('/song/')
class GetSongsSpotify(Resource):
    def post(self):
        """
        insert artist by name from the spotify API
        """
        song_name = request.get_json().get('name')
        spotify_json = song_search(song_name)

        for item in spotify_json.get('tracks').get('items'):
            artist_name = item.get('album').get('artists')[0].get('name')
            artist = Artist.insert_artist(name=artist_name)
            Song.insert_song(name=item.get('name'), artist_id=artist.id)

        return 200


def artist_search(artist):
    return spotify_search(artist, "artist")


def song_search(song):
    return spotify_search(song, "track")


def spotify_search(search_text, search_type):
    url = 'https://api.spotify.com/v1/search?'
    body_params = {"q": search_text, "type": search_type}
    headers = {"Authorization": "Bearer %s" % (spotify_auth())}

    return requests.get(url, params=body_params, headers=headers).json()


def spotify_auth():
    url = 'https://accounts.spotify.com/api/token'
    client_id = '1a3d92b3b01e4d939b14234277879bda'
    client_secret = '277cfb16fbb1457a96170516b6bd5f96'
    body_params = {'grant_type': 'client_credentials'}

    response = requests.post(url, data=body_params, auth=(client_id, client_secret))

    return response.json().get('access_token')
