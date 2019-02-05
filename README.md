# Python Challenge RESTful API using third party API


Python API developed using REST concepts, GET/POST/PUT/DELETE HTTP verbs, HTTP status codes and a third party API (Spotify). The database contains two tables, Artist and Song. They exist on a 1:N relationship, in which a band can have many songs.

This API utilizes the Spotify API through client credentials authentication to insert data into the database, searching by song or artist name.

Swagger URL:
[http://localhost:5000/api/](http://localhost:5000/api/)

## Endpoints

[http://localhost:5000/api/artist/](http://localhost:5000/api/artist/) GET: gets all the artists

[http://localhost:5000/api/artist/](http://localhost:5000/api/artist/)<artist_id> GET: get details of an artist

[http://localhost:5000/api/artist/](http://localhost:5000/api/artist/)<artist_id> PUT: change the details of an artist

[http://localhost:5000/api/artist/](http://localhost:5000/api/artist/) POST: insert an artist 
`````json
{
    "name": "example name"
}
`````

[http://localhost:5000/api/artist/](http://localhost:5000/api/artist/)<artist_id> DELETE: delete an artist

[http://localhost:5000/api/song/](http://localhost:5000/api/song/) GET: gets all the songs

[http://localhost:5000/api/song/](http://localhost:5000/api/song/)<song_id> GET: get details of a song

[http://localhost:5000/api/song/](http://localhost:5000/api/song/)<song_id> PUT: change the details of a song

[http://localhost:5000/api/song/](http://localhost:5000/api/song/) POST: insert a song 
`````json
{
    "name": "example name",
    "artist_id": 0
}
`````

[http://localhost:5000/api/song/](http://localhost:5000/api/song/)<song_id> DELETE: delete a song

## Getting data from Spotify

Access [http://localhost:5000/api/spotify/song/](http://localhost:5000/api/spotify/song/) using GET sending the desired song name through JSON, all the results are then inserted into the database with their respective artists.

Access [http://localhost:5000/api/spotify/artist/](http://localhost:5000/api/spotify/artist/) using GET sending the desired artist name through JSON, the first result is then inserted into the database.

## Usage

Install project dependencies in the requirements.txt file using `pip install -r requirements.txt`

Run the project using `flask run`