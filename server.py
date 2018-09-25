# -*- coding: utf-8 -*-
# python 3 

import os
from flask import Flask, request, render_template, jsonify
# Spotify API wrapper, documentation here: http://spotipy.readthedocs.io/en/latest/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from spotipy import oauth2
# UDF
from utility import * 





#------------------------------------
# config 
# Authenticate with Spotify using the Client Credentials flow

try:
    SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET'] 
except:
    print (' No API key , please set up  via : ')
    print (' https://developer.spotify.com/dashboard/applications ')




client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
app = Flask(__name__, static_folder='templates', template_folder='templates')



#------------------------------------

@app.route('/')
def homepage():
    # Displays homepage
    # return access_token when load the landing page 
    access_token = generate_token(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
    print ('access_token : ', access_token)
    return render_template('index.html')


#------------------------------------

@app.route('/new_releases', methods=['GET'])
def new_releases():
  
    # Use the country from the query parameters, if provided
    if 'country' in request.args:
        country = request.args['country']
    else:
        country = 'SE'
    
    # Send request to the Spotify API
    new_releases = sp.new_releases(country=country, limit=20, offset=0)
    print ('new_releases : ', new_releases)
    
    # Return the list of new releases
    return jsonify(new_releases)

#------------------------------------

  
@app.route('/recommend', methods=['GET','POST'])
def recommend():
    print (' request.args : ' , request.args)
    print (' request : ' , request)
    # Use the country from the query parameters, if provided
    if 'artist' in request.args:
        artist_ = request.args['artist']
    else:
        artist_ = 'HONNE'

    artist_id = get_artist(artist_)['id']
    print ('artist_ : ', artist_)
    print ('artist_id : ', artist_id)
    
    """

    Send request to the Spotify API
    https://spotipy.readthedocs.io/en/latest/
    https://github.com/plamere/spotipy/blob/4c2c1d763a3653aa225c4af848409ec31286a6bf/spotipy/client.py#L797
    recommend_ = sp.recommendations(seed_artists=None, seed_genres=None, seed_tracks=None, limit=20, country=None, **kwargs)
    
    """
    recommend_ =  sp.recommendations(seed_artists = [artist_id],seed_genres=['dubstep','deep-house','edm'],country='FR',limit=100)
    #print ('recommendation : ', recommend_)  
    print ('type : ', type(jsonify(recommend_['tracks'])))
    print ('artist_ : ', artist_)

    data = request.get_json()
    current_genre = request.__dict__['args']
    current_genre_dict = request.__dict__['args'].to_dict(flat=False)

    # in case user update current genre 
    if len(fix_genre_dict(current_genre_dict)) > 0:
        recommend_ =  sp.recommendations(seed_artists = [artist_id],seed_genres=fix_genre_dict(current_genre_dict),country='FR',limit=5)
    else:
        pass 

    print (' 1) current request_get_status  : ', jsonify(request.get_json()) )
    print (' 2) current request_get_json : ',  (request.__dict__) )
    print (' 3) current genres  (ImmutableMultiDict) : ',  current_genre)
    print (' 4) current genres  (dict) : ',  current_genre_dict)
    print (' 5) fixed current genres  (dict) : ',  fix_genre_dict(current_genre_dict))

    return jsonify(recommend_['tracks'])


#------------------------------------


if __name__ == '__main__':
    app.run(port=7777)




    