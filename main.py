from os import environ

client_id, client_secret = environ.get('SPOTIFY_CLIENT_ID'), environ.get('SPOTIFY_CLIENT_SECRET')
print('id, secret')
print(client_id, client_secret)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])