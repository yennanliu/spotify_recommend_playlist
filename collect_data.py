
# python 3 


"""

modify from 
https://github.com/smyrbdr/make-your-own-Spotify-playlist-of-playlist-recommendations

"""

import os
# Spotify API wrapper, documentation here: http://spotipy.readthedocs.io/en/latest/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from spotipy import oauth2
import pandas as pd
import numpy as np


# UDF
from utility import * 
from load_creds import * 


# -------------------------------------------
# config 

try:
    SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET = get_spotify_client_id_secret() 
except:
    SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET'] 
else:
    print (' No API key , please set up  via : ')
    print (' https://developer.spotify.com/dashboard/applications ')


client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


cid =' ' # Client ID; copy this from your app 
secret = ' ' # Client Secret; copy this from your app
username = ' ' # Your Spotify username


# -------------------------------------------
# main func 

#Create a dataframe of your playlist including tracks' names and audio features

def collect_train_V1():
	sourcePlaylistID = '1fCOovfyVaAbUiPlqtRF09'
	sourcePlaylist = sp.user_playlist(username, sourcePlaylistID);
	tracks = sourcePlaylist["tracks"];
	songs = tracks["items"];

	track_ids = []
	track_names = []

	for i in range(0, len(songs)):
		if songs[i]['track']['id'] != None: # Removes the local tracks in your playlist if there is any
			track_ids.append(songs[i]['track']['id'])
			track_names.append(songs[i]['track']['name'])

	features = []
	for i in range(0,len(track_ids)):
		audio_features = sp.audio_features(track_ids[i])
		for track in audio_features:
			features.append(track)

	playlist_df = pd.DataFrame(features, index = track_names)
	print ('playlist_df train_df : ', playlist_df.head())
	return playlist_df


def collect_test_V1(playlist_df):
	# Now build your test set;
	# Generate a new dataframe for recommended tracks
	# Set recommendation limit as half the Playlist Length per track, you may change this as you like
	# Check documentation for  recommendations; https://beta.developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/
	rec_tracks = []
	for i in playlist_df['id'].values.tolist():
	    rec_tracks += sp.recommendations(seed_tracks=[i], limit=int(len(playlist_df)/2))['tracks'];

	rec_track_ids = []
	rec_track_names = []
	for i in rec_tracks:
	    rec_track_ids.append(i['id'])
	    rec_track_names.append(i['name'])

	rec_features = []
	for i in range(0,len(rec_track_ids)):
	    rec_audio_features = sp.audio_features(rec_track_ids[i])
	    for track in rec_audio_features:
	        rec_features.append(track)
	        
	rec_playlist_df = pd.DataFrame(rec_features, index = rec_track_ids)
	rec_playlist_df.head()
	print ('rec_playlist_df test_df : ', rec_playlist_df.head())
	return rec_playlist_df


# -------------------------------------------



if __name__ == '__main__':
	df_train = collect_train_V1()
	df_test = collect_test_V1(df_train)
	print ('='*70)
	print ('df_train :', df_train.head())
	print ('df_train :', df_train.head())
	print ('='*70)










