import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ['SPOTIPY_CLIENT_ID'] ='6cd8559242674fa9b7328a20116c4455'
os.environ['SPOTIPY_CLIENT_SECRET'] = '9a4cc4ae71454940bc3c563e3f00da81'
os.environ['SPOTIPY_CLIENT_URI'] = 'https://localhost:8888/callback'

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
results = spotify.next(results)
albums.extend(results['items'])

for album in albums:
print(album['name'])
