# -*- coding: utf-8 -*-
# python 3 

import os
from flask import Flask, request, render_template, jsonify

# Spotify API wrapper, documentation here: http://spotipy.readthedocs.io/en/latest/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authenticate with Spotify using the Client Credentials flow
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__, static_folder='templates', template_folder='templates')

@app.route('/')
def homepage():
    # Displays homepage
    return render_template('index.html')
  
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


  
@app.route('/recommend', methods=['GET'])
def recommend():
  
    # Use the country from the query parameters, if provided
    if 'country' in request.args:
        country = request.args['country']
    else:
        country = 'SE'
    
    # Send request to the Spotify API
    recommend_ =  sp.recommendations( seed_artists = ['0O0hxUrO2PKxZknken3R24'] ,country=country)
    print ('recommendation : ', recommend_)
    
    # Return the list of new releases
    #return jsonify(recommendation_['tracks'][0])
    print ('type : ', type(jsonify(recommend_['tracks'])))
    return jsonify(recommend_['tracks'])



if __name__ == '__main__':
    app.run(port=7777)




    