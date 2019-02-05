from sqlalchemy import Column
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Artist(db.Model):
    __tablename__ = 'Artist'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(250), nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def select_all_artists():
        return Artist.query.all()

    @staticmethod
    def select_artist(id):
        artist = Artist.query.filter(Artist.id == id).first()
        if artist:
            return artist
        else:
            return 'artist not found.', 404

    @staticmethod
    def insert_artist(name):
        new_artist = Artist(name=name)
        db.session.add(new_artist)
        db.session.commit()
        return new_artist

    @staticmethod
    def update_artist(id, name):
        artist = Artist.query.filter(Artist.id == id).first()
        if artist:
            if name:
                artist.name = name
            db.session.commit()
            return 200
        else:
            return 'artist not found.', 404

    @staticmethod
    def delete_artist(id):
        artist = Artist.query.filter(Artist.id == id).first()
        if artist:
            db.session.delete(artist)
            db.session.commit()
            return 200
        else:
            return 'artist not found.', 404


class Song(db.Model):
    __tablename__ = 'Song'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(250))
    artist_id = Column(db.Integer, db.ForeignKey('Artist.id'))
    artist = relationship(Artist)

    def __init__(self, name, artist_id):
        self.name = name
        self.artist_id = artist_id

    @staticmethod
    def select_all_songs():
        return Song.query.all()

    @staticmethod
    def select_song(id):
        song = Song.query.filter(Song.id == id).first()
        if song:
            return song
        else:
            return 'song not found.', 404

    @staticmethod
    def insert_song(name, artist_id):
        new_song = Song(name=name, artist_id=artist_id)
        db.session.add(new_song)
        db.session.commit()

        return new_song

    @staticmethod
    def update_song(id, name, artist):
        song = Song.query.filter(Song.id == id).first()

        if song:
            if name:
                song.name = name
            if artist:
                song.artist = artist

            db.session.commit()
            return song
        else:
            return 'song not found.', 404

    @staticmethod
    def delete_song(id):
        song = Song.query.filter(Song.id == id).first()
        if song:
            db.session.delete(song)
            db.session.commit()
            return 200
        else:
            return 'song not found.', 404
