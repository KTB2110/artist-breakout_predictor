import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
)

artist = sp.artist("1vCWHaC5f2uS3yhpwWbIA6")  # Avicii's Spotify artist ID
print("Artist Name: ", artist['name'])
print("Followers: ", artist['followers']['total'])
print("Genres: ", artist['genres'])
print("Popularity: ", artist['popularity'])
