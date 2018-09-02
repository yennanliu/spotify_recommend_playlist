# spotify_recommend_playlist





## Quick start 

- Step 1 
	- Get the spotofy SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET (you MUST have spotify Premium account )
	- https://developer.spotify.com/dashboard/applications
- Step 2 
	- Create an APP at developer.spotify.com dashboard with created SPOTIPY_CLIENT_ID

- Step 3 
	- Run the recommendation web APP locally 

```bash 

$ git clone https://github.com/yennanliu/spotify_recommend_playlist.git
$ cd ~ && cd spotify_recommend_playlist
$ export SPOTIPY_CLIENT_ID=<your_CLIENT_ID> 
$ export SPOTIPY_CLIENT_SECRET=<your_CLIENT_SECRET>
#$ export CLIENT_ID=<your_CLIENT_ID> && export CLIENT_SECRET=<your_CLIENT_SECRET>
$ python server.py 

```

## Inspired by 
- https://github.com/arirawr/nelson
- https://nelson.glitch.me/#


## Ref 

- Projects 
	- https://medium.com/deep-learning-turkey/build-your-own-spotify-playlist-of-best-playlist-recommendations-fc9ebe92826a
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

