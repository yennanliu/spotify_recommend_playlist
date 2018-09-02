# python 3 
import sys
import spotipy
import requests
import pandas as pd 
from spotipy.oauth2 import SpotifyClientCredentials



''' 

credit 
https://github.com/plamere/spotipy/blob/master/examples/artist_recommendations.py

'''

# config 
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False



# op func 
def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None


def show_recommendations_for_artist(artist):
    albums = []
    results = sp.recommendations(seed_artists = [artist['id']])
    for track in results['tracks']:
        print (track['name'], '-', track['artists'][0]['name'])



def get_recommend_spotify_api(dynamic_access_token=False):
    """ will get spotify API access token dynamically later """
    if dynamic_access_token==True:
        pass 
    else:
        scrape_data=requests.get("https://api.spotify.com/v1/recommendations?market=US&seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_tracks=0c6xIDDpzE81m2q797ordA&min_energy=0.4&min_popularity=50", headers={"Authorization": "Bearer BQCLdpYgXePKDnD1TVckG8Odw-mtjdNw4qU-IScSst0445TiytFMhPdr2ikq_s-uONGtn0KdmIFRpr7NWS5DgdM0bqAQ07GItB6nV7wxEZTH0vjZNzq16kxsFn5q6LJeYUSn5gm8ldtvblLnXVWV7_pvnZCJPhqcx0EvyhLcRTVI1JHFA4Ft54eopIqV_WZFSGB8OrNW76fppsY"})
    scrape_json = scrape_data.json()
    print ('scrape_json  : ' , scrape_json)
    # transform json to dataframe 
    name=[]
    external_urls=[]
    id_=[]
    album_type=[]
    for i in range(len(scrape_json['tracks'])):
        #print (scrape_json['tracks'][i]['album'])
        name.append(scrape_json['tracks'][i]['album']['artists'][0]['name'])
        external_urls.append(scrape_json['tracks'][i]['album']['artists'][0]['external_urls']['spotify'])
        id_.append(scrape_json['tracks'][i]['album']['artists'][0]['id'])
        album_type.append(scrape_json['tracks'][i]['album']['type'])
    data=pd.DataFrame({ 'name' : name,
                        'external_urls' : external_urls,
                        'id' : id_,
                        'album_type' : album_type})
    print (data)




        
