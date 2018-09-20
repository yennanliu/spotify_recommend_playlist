# spotify_recommend_playlist

<img src ="https://github.com/yennanliu/spotify_recommend_playlist/blob/master/ref/app_1.png" width="800" height="400">

## Quick start 

- Step 1 
	- Get the spotify SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET 
	- https://developer.spotify.com/dashboard/applications
	- (You MUST have the spotify Premium account )
- Step 2 
	- Create an APP at developer page with created SPOTIPY_CLIENT_ID
	- https://developer.spotify.com

- Step 3 
	- Execute the following commands then run the web APP locally 

```bash 

$ cd ~ && git clone https://github.com/yennanliu/spotify_recommend_playlist.git
$ cd ~ && cd spotify_recommend_playlist
$ bash install.sh 
$ export SPOTIPY_CLIENT_ID=<your_CLIENT_ID> 
$ export SPOTIPY_CLIENT_SECRET=<your_CLIENT_SECRET>
$ python server.py 

```

## Tech
- Backend : Python3 flask, spotipy 
- Frontend : Javascript, HTML, CSS 


## Inspired by 
- https://nelson.glitch.me/#


## Ref 

- Projects 
	- https://github.com/arirawr/nelson
	- https://glitch.com/~spotify-web-playback
	- https://glitch.com/@spotify
	- https://glitch.com/@a

- SDK / API doc. 
	- https://beta.developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/
	- https://developer.spotify.com/documentation/web-playback-sdk/reference/
	- https://developer.spotify.com/console/get-recommendations 

- Access token  
	- https://ericdaat.github.io/scraping-kshe-radio-to-spotify-playlist.html
	- https://github.com/drshrey/spotify-flask-auth-example

- ML
	- http://smarterplaylists.playlistmachinery.com/go.html
	- https://medium.com/deep-learning-turkey/build-your-own-spotify-playlist-of-best-playlist-recommendations-fc9ebe92826a



