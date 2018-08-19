# python 3 

import json
from flask import Flask, request, redirect, g, render_template,session
from flask_session import Session
import requests
import base64
import urllib
import urllib.parse
import os


"""

# Authentication Steps, paramaters, and responses are defined at https://developer.spotify.com/web-api/authorization-guide/
# Visit this url to see all the steps, parameters, and expected response. 


modify from 
https://github.com/drshrey/spotify-flask-auth-example

"""


app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


#  Client Keys
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET'] 

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)


# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
SCOPE = "playlist-modify-public playlist-modify-private"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()


auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}




@app.route("/recommend_V1")
def get_recommend_spotify_V1():
    #access_token = "BQCne_YqAu5eOGS8Y_ghvFdMjaNEvYDdyOkMUKmEJoAo8LV16DwISNBMKTgzUt4fGhfdTiOXcAylgxO_iotv52yy8eZpVgeXfPXf0EEEThCnqymyuAbAHxQ-nlmAfkp28XIKXvYepNSs6UBaYr93GAEMx60kSXvR5NI6yGOQqzZEZVjLLyA761qsl3ydPUfYea1XEBL84AAoLFw"
    access_token = session["access_token"]
    print ('session["access_token"] :' , session["access_token"])
    scrape_data=requests.get("https://api.spotify.com/v1/recommendations?market=US&seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_tracks=0c6xIDDpzE81m2q797ordA&min_energy=0.4&min_popularity=50", headers={"Authorization": "Bearer {}".format(access_token)})
    scrape_json = scrape_data.json()
    print ('scrape_json  : ' , scrape_json)
    return (json.dumps(scrape_json))


@app.route("/recommend_V2")
def get_recommend_spotify_V2(market='JP',seed_genres='j-pop'):
    print(' market : ', market)
    print(' seed_genres : ', seed_genres)
    access_token = session["access_token"]
    print ('session["access_token"] :' , session["access_token"])
    scrape_data=requests.get("https://api.spotify.com/v1/recommendations?market={}&seed_genres={}&min_energy=0.4&min_popularity=50".format(market,seed_genres), headers={"Authorization": "Bearer {}".format(access_token)})
    scrape_json = scrape_data.json()
    print ('scrape_json  : ' , scrape_json)
    return (json.dumps(scrape_json))



@app.route("/")
def index():
    # Auth Step 1: Authorization
    url_args = "&".join(["{}={}".format(key,urllib.parse.quote(val)) for key,val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)


@app.route("/callback/q")
def callback():
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }
    #base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))
    """ hack the base64encoded crendential for python 3 fix here """
    base64encoded = base64.b64encode(( CLIENT_ID + ":").encode('utf-8')).decode('utf-8') + base64.b64encode(CLIENT_SECRET.encode('utf-8')).decode('utf-8')
    headers = {"Authorization": "Basic {}".format(base64encoded)}
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    print (' ----- response_data : -----', response_data)
    access_token = response_data["access_token"]
    print (' ----- access_token : -----', response_data["access_token"])
    session["access_token"] = response_data["access_token"]
    return response_data["access_token"]





if __name__ == "__main__":
    app.run(debug=True,port=PORT)



