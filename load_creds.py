# python 3 
import yaml
import os


with open('.creds.yml') as f:
    config = yaml.load(f)

SPOTIPY_CLIENT_ID = config['spotify_api']['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = config['spotify_api']['SPOTIPY_CLIENT_SECRET'] 

def get_spotify_client_id_secret():
	print (' SPOTIPY_CLIENT_ID = ', SPOTIPY_CLIENT_ID)
	print (' SPOTIPY_CLIENT_SECRET = ', SPOTIPY_CLIENT_SECRET)
	return SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

